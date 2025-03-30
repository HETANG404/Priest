# 🩸 Priest - Pixiv Illustration Scraper & PDF Archiver

> "Human sacrifice refers to offering a living person as a sacrifice to appease the gods."

**Priest** is a Python-based multi-mode Pixiv image crawler, supporting ranking downloads, artist archives, follow updates, MySQL storage, and PDF generation.

---

## 📁 Project Structure

```
Priest/
├── data/
│   ├── database/              # Database backups (optional)
│   └── images/
│       ├── following/         # Followed users' updates
│       ├── olga/              # Olga advanced download (with DB)
│       ├── pdfs/              # Auto-generated PDFs
│       ├── ranking/           # Rankings by mode
│       │   ├── daily/
│       │   ├── daily_r18/
│       │   ├── weekly/
│       │   ├── weekly_r18/
│       │   ├── r18g/
│       │   └── monthly/
│       └── users/             # Specific user download by ID
├── migrations/                # (if using Alembic)
├── priestvenv/                # Python virtualenv (not included)
├── src/
│   ├── core/
│   │   ├── olga.py            # Advanced downloader (ranking + DB)
│   │   └── spider.py          # Standard downloader
│   ├── db/
│   │   ├── init_db.py         # Create tables
│   │   ├── models.py          # ORM models: Illustration, Tag
│   │   ├── mysql_manager.py   # SQLAlchemy session manager
│   │   ├── query_handler.py   # DB query utilities
│   │   └── redis_manager.py   # (Optional) Redis support
│   └── utils/
│       ├── check_folder.py    # Folder check tools
│       ├── create_folder.py   # Folder creation by mode
│       ├── downloader.py      # Image downloader
│       ├── get_with_retry.py  # Requests with retry logic
│       ├── logger.py
│       ├── pdf_factory.py     # Merge images into PDF
│       └── save_info_to_mysql.py # Save JSON to DB
│   ├── lowentry.py            # ✅ Main Entry: daily / weekly / user / latest_following / following(to be continued)
│   └── olgaentry.py           # ✅ Advanced Entry: with MySQL record
├── tests/                     # (optional tests)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📦 Features

### 📊 Rankings Downloader
Supports Pixiv:
- `daily`, `weekly`, `monthly`, `daily_r18`, `weekly_r18`, `r18g`
- Auto PDF merge by batch

### 👥 Followed Users Update
- Downloads **latest works only**, incrementally
- Image deduplication by ID

### 🧑‍🎨 Specific User Download
- Full download of all illustrations from a given user ID

### 💾 Advanced Mode (olgaentry)
- Save illustration metadata to MySQL
- Save tags to `Tag` table
- Prevent duplicate downloads via DB check

### ⚠️ Notes on Cookie & Rate Limits

- **Ranking downloads** (`daily`, `weekly`, `monthly`) do **not require a Pixiv login cookie**, and can be run anonymously.
- However, images related to **R18 or R18G content require a Pixiv login cookie**

- This project includes built-in retry logic and will **automatically sleep briefly** between requests when encountering rate limits (like HTTP 429 or broken connections). Be patient — it's intentional to avoid triggering Pixiv's anti-bot detection.
---

## 🧰 Folder Naming & Behavior

Users only need to configure **`BASE_PATH`** in `config/settings.py`, such as:

```python
BASE_PATH = "E:/Priest/data/images"
```

All subfolders will be created automatically. The structure is organized as follows:

- `ranking/daily/`, `ranking/weekly_r18/`, `ranking/r18g/` ... etc. depending on mode
- `users/{user_id}_{username}/` — images from specific users
- `following/` — followed user updates (incremental)
- `pdfs/` — PDF files like `merged_daily_1p_2025-03-30.pdf`
- `olga/` — advanced DB-related downloads (`olga_wm/`)

🧹 Old images in folders like `ranking/daily/` are **automatically cleared** before new downloads (if configured).

---

## 🛠 Setup

### 1. Clone Project & Create Environment
```bash
git clone https://github.com/yourname/Priest.git
cd Priest
python -m venv priestvenv
```

### 2. Activate Virtual Environment
- Windows:
```bash
priestvenv\Scripts\activate
```
- macOS/Linux:
```bash
source priestvenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. ✏️ Modify Configuration
Edit `config/settings.py` and **set your Pixiv cookie**:

```python
headers = {
  "User-Agent": ......,
  "Cookie": "your_pixiv_cookie_here"
}

BASE_PATH = "E:/Priest/data/images"  # <- Change this to your desired image storage path
```

---

## 🚀 How to Run

### 🔹 Basic Download Mode (lowentry)
```bash
python src/lowentry.py
```
supports：ranking、users、latest_following，create_PDF.

### 🔸 Advanced Mode with DB (olgaentry)
```bash
python src/olgaentry.py
```
supports：MySQL（illustration + tag），weekly / monthly ranking.

---

## 🧱 Database Schema
Using SQLAlchemy ORM:

### Illustration Table
- 'illustrations'

### Tag Table
- `tags`
- Many-to-many linked with `illustration_tag` table

---

## 📄 PDF Output Example
```bash
📁 data/images/pdfs/
├── merged_daily-1p_2015-03-30.pdf
└── merged_daily_5p_2025-03-30.pdf
```

---

## 🙋‍♂️ Author
**HE TANG (Justin Tang Alin)**  

---

## 📜 License
MIT License. Academic or personal use only. Do not use for commercial scraping.

