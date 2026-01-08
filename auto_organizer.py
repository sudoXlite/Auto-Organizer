#!/usr/bin/env python3
"""
Auto-Organizer PRO v5 – Ultimate
-------------------------------
- Default recursive=True, --no-recursive flag bilan o‘chirish
- Flatten / Preserve, Clean-empty, Dry-run, Verbose, Unicode-safe
- JSON auto-create, Append log
- DRY principle for organize_file
- clean_empty_folders: OSError catch
- argparse help defaults avtomatik
"""

import logging
import json
from pathlib import Path
import shutil
import argparse
import sys

# ---------- Default Config ----------
DEFAULT_FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
    "Executables": [".exe", ".apk", ".iso", ".msi"],
    "Torrents": [".torrent"]
}

# ---------- Utility ----------
def setup_logging(log_file: Path, verbose: bool):
    handlers = [logging.FileHandler(log_file, mode="a", encoding="utf-8")]
    if verbose:
        handlers.append(logging.StreamHandler(sys.stdout))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=handlers
    )

def load_file_types(config_path: Path):
    if not config_path.exists():
        try:
            config_path.parent.mkdir(parents=True, exist_ok=True)
            with config_path.open("w", encoding="utf-8") as f:
                json.dump(DEFAULT_FILE_TYPES, f, indent=4, ensure_ascii=False)
            logging.info(f"Config yaratildi: {config_path}")
        except Exception as e:
            logging.error(f"Config yaratishda xato: {e}")
        return DEFAULT_FILE_TYPES
    try:
        with config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"Config yuklandi: {config_path}")
            return data
    except Exception as e:
        logging.error(f"Config yuklashda xato: {e}")
        return DEFAULT_FILE_TYPES

def get_unique_name(dest_folder: Path, file_path: Path) -> Path:
    stem = file_path.stem
    suffix = file_path.suffix
    counter = 1
    candidate = dest_folder / file_path.name
    while candidate.exists():
        candidate = dest_folder / f"{stem}({counter}){suffix}"
        counter += 1
    return candidate

def move_to_folder(file_path: Path, target_folder: Path, dry_run=False):
    target_folder.mkdir(parents=True, exist_ok=True)
    dest_file = get_unique_name(target_folder, file_path)
    if dry_run:
        logging.info(f"[DRY-RUN] {file_path} → {dest_file}")
    else:
        try:
            shutil.move(str(file_path), str(dest_file))
            logging.info(f"{file_path} → {dest_file}")
        except PermissionError:
            logging.warning(f"Ruxsat yo'q: {file_path}")
        except Exception as e:
            logging.error(f"Xato: {file_path} | {e}")

def organize_file(file_path: Path, file_types: dict, target_folder: Path, dry_run=False):
    if not file_path.is_file():
        return
    ext = file_path.suffix.lower()
    for folder_name, extensions in file_types.items():
        if ext in [e.lower() for e in extensions]:
            move_to_folder(file_path, target_folder / folder_name, dry_run=dry_run)
            return
    move_to_folder(file_path, target_folder / "Others", dry_run=dry_run)

def recursive_organize(folder_path: Path, file_types: dict, flatten=False, recursive=True, dry_run=False):
    paths = folder_path.rglob("*") if recursive else folder_path.glob("*")
    for path in paths:
        if path.is_file():
            target_folder = folder_path if flatten else path.parent
            organize_file(path, file_types, target_folder, dry_run=dry_run)

def clean_empty_folders(folder_path: Path, dry_run=False):
    for subfolder in sorted(folder_path.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if subfolder.is_dir() and not any(subfolder.iterdir()):
            if dry_run:
                logging.info(f"[DRY-RUN] Bo'sh papka o'chiriladi: {subfolder}")
            else:
                try:
                    subfolder.rmdir()
                    logging.info(f"Bo'sh papka o'chirildi: {subfolder}")
                except OSError as e:
                    logging.warning(f"Bo'sh papkani o'chirishda xato: {subfolder} | {e}")

# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Auto-Organizer PRO v5 Ultimate")
    parser.add_argument("-p", "--path", type=Path, default=Path.home() / "Downloads",
                        help="Tartiblash papkasi")
    parser.add_argument("-c", "--config", type=Path, default=Path("file_types.json"),
                        help="JSON konfiguratsiya fayli")
    parser.add_argument("-f", "--flatten", action="store_true",
                        help="Fayllarni top-level ga ko'chirish")
    parser.add_argument("--no-recursive", action="store_false", dest="recursive",
                        help="Subfolders ichidagi fayllarni tartiblashni o'chirish")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Console log")
    parser.add_argument("-e", "--clean-empty", action="store_true",
                        help="Bo'sh papkalarni o'chirish")
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help="Hech narsa o'zgartirmasdan nima bo'lishini ko'rsatish")
    parser.add_argument("-l", "--logfile", type=Path, default=Path("organizer.log"),
                        help="Log fayl nomi")
    args = parser.parse_args()

    setup_logging(args.logfile, args.verbose)
    logging.info(f"Tartiblash boshlandi: {args.path}")
    file_types = load_file_types(args.config)
    recursive_organize(args.path, file_types, flatten=args.flatten,
                       recursive=args.recursive, dry_run=args.dry_run)
    if args.clean_empty:
        clean_empty_folders(args.path, dry_run=args.dry_run)
    logging.info("Tartiblash tugadi")

if __name__ == "__main__":
    main()
