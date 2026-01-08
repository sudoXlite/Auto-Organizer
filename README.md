```
# Auto-Organizer PRO

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v5.0-brightgreen)

**Avtomatik fayl tartiblagich** – Downloads papkasini (yoki boshqa istalgan papkani) kengaytmaga qarab avtomatik tartibga soluvchi professional Python skripti.

Fayllarni Images, Documents, Videos, Music, Archives va boshqa kategoriyalarga ajratadi. To'liq moslashuvchan, xavfsiz va qulay CLI bilan ishlaydi.

## Xususiyatlar

- **Flatten yoki Preserve strukturani saqlash** – fayllarni root papkaga yig'ish yoki asl subpapkalarda kategoriya papkalar yaratish
- **Rekursiv tartiblash** (default: yoqilgan, `--no-recursive` bilan o'chirish mumkin)
- **Bo'sh papkalarni avtomatik o'chirish** (`--clean-empty`)
- **Dry-run rejimi** – hech narsa o'zgartirmasdan nima bo'lishini oldindan ko'rish (`--dry-run`)
- **Fayl nomi to'qnashuvi** – agar bir xil nom bo'lsa avtomatik `(1)`, `(2)` qo'shadi (multi-dot kengaytmalar to'g'ri ishlaydi: `.tar.gz` va h.k.)
- **JSON konfiguratsiya** – fayl turlarini oson o'zgartirish (birinchi ishlatishda avtomatik yaratiladi)
- **To'liq logging** – faylga yoziladi (append), `--verbose` bilan terminalga ham chiqadi
- **Unicode-safe** – o'zbekcha, ruscha, arabcha fayl nomlari bilan muammosiz ishlaydi
- **Professional CLI** – `argparse` bilan qulay opsiyalar

## O'rnatish va ishlatish

### 1. Reponi klonlash
```bash
git clone https://github.com/sudoxlite/auto-organizer.git
cd auto-organizer
```

### 2. Python 3.8+ kerak (standart kutubxonalar bilan ishlaydi, qo'shimcha package yo'q)

### 3. Ishlatish
```bash
# Oddiy tartiblash (Downloads papkasi, recursive, preserve structure)
python auto_organizer.py

# Flatten rejimida (hamma fayllarni root'ga yig'ish)
python auto_organizer.py --flatten

# Muayyan papkani tartiblash
python auto_organizer.py --path /yo'l/ga/papka

# Dry-run (faqat ko'rsatadi, hech narsa o'zgartirmaydi)
python auto_organizer.py --dry-run

# Bo'sh papkalarni o'chirish bilan
python auto_organizer.py --clean-empty

# Terminalga ham log chiqarish
python auto_organizer.py --verbose

# Rekursivni o'chirish (faqat bitta daraja)
python auto_organizer.py --no-recursive
```

Barcha opsiyalarni ko'rish uchun:
```bash
python auto_organizer.py --help
```

## Konfiguratsiya

Birinchi ishlatishda loyiha papkasida `file_types.json` avtomatik yaratiladi. Uni ochib, o'zingizga kerakli kengaytmalarni qo'shing yoki o'zgartiring.

Misol:
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "MyFolder": [".log", ".tmp", ".bak"]
}
```

## Fayl nomi

Asosiy skriptni `auto_organizer.py` deb nomlang (yoki o'zingiz xohlagan nom).

## Muallif

- **GitHub**: [@sudoxlite](https://github.com/sudoxlite)
- **Telegram**: [@pythondev_www](https://t.me/pythondev_www)

Fikr-mulohaza, taklif va yordam uchun bemalol yozing!

## License

Bu loyiha **MIT License** bilan tarqatiladi – erkin ishlatish, o'zgartirish va tarqatish mumkin.

Batafsil: [LICENSE](LICENSE) faylida.
```

### LICENSE fayl (alohida fayl sifatida repo'ga qo'shing)

```plaintext
MIT License

Copyright (c) 2026 sudoxlite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Repo tuzilishi tavsiyasi:
```
auto-organizer/
├── auto_organizer.py     # asosiy skript (v5 kod)
├── README.md             # yuqoridagi
├── LICENSE               # yuqoridagi
└── file_types.json       # (ixtiyoriy, birinchi ishlatishda yaratiladi)
```

Bro, endi GitHub'ga yukla – repo zo'r ko'rinadi, professional darajada!  ```markdown
# Auto-Organizer PRO

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v5.0-brightgreen)

**Avtomatik fayl tartiblagich** – Downloads papkasini (yoki boshqa istalgan papkani) kengaytmaga qarab avtomatik tartibga soluvchi professional Python skripti.

Fayllarni Images, Documents, Videos, Music, Archives va boshqa kategoriyalarga ajratadi. To'liq moslashuvchan, xavfsiz va qulay CLI bilan ishlaydi.

## Xususiyatlar

- **Flatten yoki Preserve strukturani saqlash** – fayllarni root papkaga yig'ish yoki asl subpapkalarda kategoriya papkalar yaratish
- **Rekursiv tartiblash** (default: yoqilgan, `--no-recursive` bilan o'chirish mumkin)
- **Bo'sh papkalarni avtomatik o'chirish** (`--clean-empty`)
- **Dry-run rejimi** – hech narsa o'zgartirmasdan nima bo'lishini oldindan ko'rish (`--dry-run`)
- **Fayl nomi to'qnashuvi** – agar bir xil nom bo'lsa avtomatik `(1)`, `(2)` qo'shadi (multi-dot kengaytmalar to'g'ri ishlaydi: `.tar.gz` va h.k.)
- **JSON konfiguratsiya** – fayl turlarini oson o'zgartirish (birinchi ishlatishda avtomatik yaratiladi)
- **To'liq logging** – faylga yoziladi (append), `--verbose` bilan terminalga ham chiqadi
- **Unicode-safe** – o'zbekcha, ruscha, arabcha fayl nomlari bilan muammosiz ishlaydi
- **Professional CLI** – `argparse` bilan qulay opsiyalar

## O'rnatish va ishlatish

### 1. Reponi klonlash
```bash
git clone https://github.com/sudoxlite/auto-organizer.git
cd auto-organizer
```

### 2. Python 3.8+ kerak (standart kutubxonalar bilan ishlaydi, qo'shimcha package yo'q)

### 3. Ishlatish
```bash
# Oddiy tartiblash (Downloads papkasi, recursive, preserve structure)
python auto_organizer.py

# Flatten rejimida (hamma fayllarni root'ga yig'ish)
python auto_organizer.py --flatten

# Muayyan papkani tartiblash
python auto_organizer.py --path /yo'l/ga/papka

# Dry-run (faqat ko'rsatadi, hech narsa o'zgartirmaydi)
python auto_organizer.py --dry-run

# Bo'sh papkalarni o'chirish bilan
python auto_organizer.py --clean-empty

# Terminalga ham log chiqarish
python auto_organizer.py --verbose

# Rekursivni o'chirish (faqat bitta daraja)
python auto_organizer.py --no-recursive
```

Barcha opsiyalarni ko'rish uchun:
```bash
python auto_organizer.py --help
```

## Konfiguratsiya

Birinchi ishlatishda loyiha papkasida `file_types.json` avtomatik yaratiladi. Uni ochib, o'zingizga kerakli kengaytmalarni qo'shing yoki o'zgartiring.

Misol:
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "MyFolder": [".log", ".tmp", ".bak"]
}
```

## Fayl nomi

Asosiy skriptni `auto_organizer.py` deb nomlang (yoki o'zingiz xohlagan nom).

## Muallif

- **GitHub**: [@sudoxlite](https://github.com/sudoxlite)
- **Telegram**: [@pythondev_www](https://t.me/pythondev_www)

Fikr-mulohaza, taklif va yordam uchun bemalol yozing!

## License

Bu loyiha **MIT License** bilan tarqatiladi – erkin ishlatish, o'zgartirish va tarqatish mumkin.

Batafsil: [LICENSE](LICENSE) faylida.
