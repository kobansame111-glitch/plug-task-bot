"""
╔══════════════════════════════════════════════════╗
║  株式会社プラグ 社内タスク管理 Discord Bot       ║
║  Plug Task Bot v1.0                              ║
╚══════════════════════════════════════════════════╝

機能:
  1. タスク依頼 → 担当者に通知 → 承認/辞退 → Googleカレンダー登録
    2. GitHub リポジトリの変更を定期監視 → Discord に自動通知

    使い方:
      Discordで以下のコマンドを使います:
          /task @担当者 タスク内容 納期
              /tasks  （現在のタスク一覧）
                  /github （GitHub監視の状態を確認）
                  """

import re
import discord
from discord import app_commands
from discord.ext import tasks

import config
from google_calendar import create_task_event
from github_monitor import GitHubMonitor


# ──────────────────────────────────────────────
# Discord Bot の初期設定
# ──────────────────────────────────────────────

# Bot がアクセスできる情報の範囲を設定（intents）
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容の読み取りを許可
intents.members = True          # メンバー情報の取得を許可

# Bot 本体を作成
bot = discord.Client(intents=intents)

# スラッシュコマンド用のツリーを作成
tree = app_commands.CommandTree(bot)

# GitHub 監視インスタンス
github_monitor = GitHubMonitor()

# タスクを保存する辞書（メモリ上で管理）
# キー: タスクID, 値: タスク情報の辞書
pending_tasks: dict[str, dict] = {}
task_counter = 0


# ──────────────────────────────────────────────
# 承認/辞退ボタン付きの View（UI部品）
# ──────────────────────────────────────────────

class TaskApprovalView(discord.ui.View):
      """
          タスク依頼メッセージに付く「承認」「辞退」ボタン"""
  ╔══════════════════════════════════════════════════╗
║  株式会社プラグ 社内タスク管理 Discord Bot       ║
║  Plug Task Bot v1.0                              ║
╚══════════════════════════════════════════════════╝

機能:
  1. タスク依頼 → 担当者に通知 → 承認/辞退 → Googleカレンダー登録
  2. GitHub リポジトリの変更を定期監視 → Discord に自動通知

使い方:
  Discordで以下のコマンドを使います:
    /task @担当者 タスク内容 納期
    /tasks  （現在のタスク一覧）
          /github （GitHub監視の状態を確認）
      """

      import re
      import discord
      from discord import app_commands
from discord.ext import tasks

import config
from google_cal
