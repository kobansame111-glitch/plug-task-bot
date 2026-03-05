"""
設定ファイル
.env から環境変数を読み込んで、プログラム全体で使える形にします。
"""

import os
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()


# ─── Discord の設定 ───
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_TASK_CHANNEL_ID = int(os.getenv("DISCORD_TASK_CHANNEL_ID", "0"))
DISCORD_GITHUB_CHANNEL_ID = int(os.getenv("DISCORD_GITHUB_CHANNEL_ID", "0"))

# ─── Google Calendar の設定 ───
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json")
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")

# ─── GitHub の設定 ───
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# カンマ区切りのリポジトリ名をリストに変換
GITHUB_REPOS = [
      repo.strip()
      for repo in os.getenv("GITHUB_REPOS", "").split(",")
      if repo.strip()
]
GITHUB_CHECK_INTERVAL = int(os.getenv("GITHUB_CHECK_INTERVAL", "5"))
