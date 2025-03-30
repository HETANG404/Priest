import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


BASE_PATH = r"E:/Priest/data/images"



url = 'https://www.pixiv.net/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63',
    'Cookie': os.getenv("PIXIV_COOKIE")
}