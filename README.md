# Auto-Organizer PRO v5 – Ultimate

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Auto-Organizer PRO v5 – bu **professional fayllarni avtomatik tartiblovchi vosita**.  
U **Downloads** yoki boshqa papkalardagi fayllarni kengaytmasiga qarab kategoriyalarga ajratadi, bo‘sh papkalarni tozalaydi, dry-run bilan xavfsiz ishlaydi va **Unicode-safe**, **recursive**, **flatten** opsiyalari bilan ishlaydi.

---

## Features

- **Preserve / Flatten folders** – fayllarni asl subfolder strukturasi bilan saqlash yoki top-level ga ko‘chirish.
- **Recursive** – default `True`, faqat `--no-recursive` flag bilan o‘chirish mumkin.
- **Clean empty folders** – bo‘sh papkalarni xavfsiz o‘chirish, dry-run bilan ko‘rish mumkin.
- **Dry-run** – hech narsa o‘zgartirmasdan nima bo‘lishini ko‘rsatadi.
- **Verbose console log & append file log** – terminal va log faylida kuzatish.
- **Unicode-safe & multi-dot filenames** – Pathlib bilan Windows/Linux/UTF-8 xavfsiz.
- **JSON auto-create config** – default fayl turlari bilan, yangi turlarni osongina qo‘shish mumkin.
- **DRY principle** – kategoriya va Others fayllarni birlashtirish orqali toza kod.

---

## Default File Types

```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
    "Executables": [".exe", ".apk", ".iso", ".msi"],
    "Torrents": [".torrent"]
}
