"""
Google Calendar 連携モジュール

タスクが承認されたら、Google カレンダーに予定を自動登録します。
初回実行時にブラウザが開いて Google アカウントの認証が求められます。
"""

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import config

# Google Calendar API に必要な権限（スコープ）
# この権限で「カレンダーの予定を読み書き」できます
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
      """
          Google Calendar API に接続するためのサービスオブジェクトを取得します。

              初回は credentials.json を使ってブラウザ認証が必要。
                  認証後は token.json に保存され、次回からは自動的にログインします。
                      """
      creds = None

    # 以前の認証トークンが保存されていれば読み込む
      if os.path.exists("token.json"):
                creds = Credentials.from_authorized_user_file("token.json", SCOPES)

      # トークンがない、または期限切れの場合
      if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                              # トークンをリフレッシュ（更新）する
                              creds.refresh(Request())
      else:
                    # 新規認証（ブラウザが開きます）
                    flow = InstalledAppFlow.from_client_secrets_file(
                                      config.GOOGLE_CREDENTIALS_FILE, SCOPES
                    )
                    creds = flow.run_local_server(port=0)

          # 次回のために認証情報を保存
                with open("token.json", "w") as token:
                              token.write(creds.to_json())

    # Calendar API のサービスオブジェクトを作成して返す
    service = build("calendar", "v3", credentials=creds)
    return service


def create_task_event(
      task_title: str,
     """
Google Calendar 連携モジュール

タスクが承認されたら、Google カレンダーに予定を自動登録します。
初回実行時にブラウザが開いて Google アカウントの認証が求められます。
"""

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import config

# Google Calendar API に必要な権限（スコープ）
# この権限で「カレンダーの予定を読み書き」できます
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
      """
          Google Calendar API に接続するためのサービスオブジェクトを取得します。

              初回は credentials.json を使ってブラウザ認証が必要。
                  認証後は token.json に保存され、次回からは自動的にログインします。
                      """
    creds = None

    # 以前の認証トークンが保存されていれば読み込む
    if os.path.exists("token.json"):
              creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # トークンがない、または期限切れの場合
    if not creds or not creds.valid:
              if creds and creds.expired and creds.refresh_token:
                            # トークンをリフレッシュ（更新）する
                            creds.refresh(Request())
    else:
            # 新規認証（ブラウザが開きます）
                  flow = InstalledAppFlow.from_client_secrets_file(
                                    config.GOOGLE_CREDENTIALS_FILE, SCOPES
                  )
                  creds = flow.run_local_server(port=0)

        # 次回のために認証情報を保存
              with open("token.json", "w") as token:
                            token.write(creds.to_json())

    # Calendar API のサービスオブジェクトを作成して返す
    service = build("calendar", "v3", credentials=creds)
    return service


def create_task_event(
      task_title: str,
      description: str,
      deadline: str,
      assignee: str,
      requester: str,
):
      """
          Google カレンダーにタスクの予定を登録します。

              引数:
                      task_title: タスクのタイトル（例: "在庫チェック"）
                              description: タスクの詳しい内容
                                      deadline: 納期の日付（例: "2026-03-15"）
                                              assignee: 担当者の名前（例: "島崎美奈"）
                                                      requester: 依頼者の名前（例: "島崎龍"）

                                                          戻り値:
                                                                  作成されたイベントのURL（Google カレンダーで開けるリンク）
                                                                      """
    service = get_calendar_service()

    # カレンダーに登録するイベントの内容を組み立てる
    event = {
              "summary": f"【タスク】{task_title}（担当: {assignee}）",
              "description": (
                            f"📋 タスク内容:\n{description}\n\n"
                            f"👤 依頼者: {requester}\n"
                            f"👤 担当者: {assignee}\n"
                            f"📅 納期: {deadline}\n\n"
                            f"--- プラグ社内タスク管理Bot により自動登録 ---"
              ),
              # 終日イベントとして登録（時間指定なし）
              "start": {
                            "date": deadline,
                            
