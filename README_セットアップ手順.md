# Plug Task Bot セットアップ手順書

株式会社プラグ 社内タスク管理 Discord Bot

---

## このBotでできること

1. Discord で `@担当者` にタスクを依頼 → ボタンで承認/辞退
2. 2. 承認されたら自動で Google カレンダーに納期を登録
   3. 3. GitHub リポジトリの変更（コミット/PR/Issue/リリース）を自動通知
     
      4. ---
     
      5. ## 必要なもの
     
      6. - Python 3.10 以上がインストールされたPC
         - - Discord アカウント
           - - Google アカウント（無料版Gmail OK）
             - - GitHub アカウント（監視機能を使う場合）
              
               - ---

               ## ステップ1: Python のインストール確認

               ターミナル（Mac）またはコマンドプロンプト（Windows）を開いて、以下を入力:

               \`\`\`bash
               python3 --version
               \`\`\`

               \`Python 3.10.x\` のように表示されればOK。
               もし表示されない場合は https://www.python.org/downloads/ からインストールしてください。

               ---

               ## ステップ2: Discord Bot の作成

               ### 2-1. Discord Developer Portal にアクセス

               1. ブラウザで https://discord.com/developers/applications を開く
               2. 2. Discord アカウントでログイン
                  3. 3. 右上の **「New Application」** をクリック
                     4. 4. 名前を \`Plug Task Bot\` にして **「Create」**
                       
                        5. ### 2-2. Bot ユーザーを作成
                       
                        6. 1. 左メニューの **「Bot」** をクリック
                           2. 2. **「Add Bot」** → **「Yes, do it!」**
                              3. 3. **「TOKEN」** の下にある **「Reset Token」** をクリック
                                 4. 4. 表示されたトークンを **コピーして安全な場所に保存**（後で使います）
                                   
                                    5. **重要**: このトークンは絶対に他人に見せないでください！
                                   
                                    6. ### 2-3. Bot の権限設定
                                   
                                    7. 1. 同じ「Bot」ページで、以下をONにする:
                                       2.    - **Presence Intent** ✅
                                             -    - **Server Members Intent** ✅
                                                  -    - **Message Content Intent** ✅
                                                   
                                                       - ### 2-4. Bot をサーバーに招待
                                                   
                                                       - 1. 左メニューの **「OAuth2」** → **「URL Generator」**
                                                         2. 2. **SCOPES** で \`bot\` と \`applications.commands\` にチェック
                                                            3. 3. **BOT PERMISSIONS** で以下にチェック:
                                                               4.    - Send Messages
                                                                     -    - Send Messages in Threads
                                                                          -    - Embed Links
                                                                               -    - Read Message History
                                                                                    -    - Use Slash Commands
                                                                                         -    - Mention Everyone
                                                                                              - 4. 下に生成されたURLをコピーしてブラウザで開く
                                                                                                5. 5. 招待するサーバーを選んで **「認証」**
                                                                                                  
                                                                                                   6. ---
                                                                                                  
                                                                                                   7. ## ステップ3: Google Calendar API の設定
                                                                                                  
                                                                                                   8. ### 3-1. Google Cloud Console でプロジェクト作成
                                                                                                  
                                                                                                   9. 1. https://console.cloud.google.com/ にアクセス
                                                                                                      2. 2. 上部の **「プロジェクトを選択」** → **「新しいプロジェクト」**
                                                                                                         3. 3. プロジェクト名: \`plug-task-bot\` → **「作成」**
                                                                                                           
                                                                                                            4. ### 3-2. Calendar API を有効化
                                                                                                           
                                                                                                            5. 1. 左メニュー → **「APIとサービス」** → **「ライブラリ」**
                                                                                                               2. 2. 検索バーで \`Google Calendar API\` と検索
                                                                                                                  3. 3. **「Google Calendar API」** をクリック → **「有効にする」**
                                                                                                                    
                                                                                                                     4. ### 3-3. 認証情報（credentials.json）を作成
                                                                                                                    
                                                                                                                     5. 1. 左メニュー → **「APIとサービス」** → **「認証情報」**
                                                                                                                        2. 2. **「認証情報を作成」** → **「OAuthクライアントID」**
                                                                                                                           3. 3. **「同意画面を構成」** が出たら:
                                                                                                                              4.    - User Type: **「外部」** を選択 → **「作成」**
                                                                                                                                    -    - アプリ名: \`Plug Task Bot\`
                                                                                                                                         -    - サポートメール: 自分のメールアドレス
                                                                                                                                              -    - **「保存して続行」** を何度かクリックして完了
                                                                                                                                                   - 4. もう一度 **「認証情報を作成」** → **「OAuthクライアントID」**
                                                                                                                                                     5. 5. アプリケーションの種類: **「デスクトップアプリ」**
                                                                                                                                                        6. 6. 名前: \`Plug Task Bot\`
                                                                                                                                                           7. 7. **「作成」** → JSONファイルを **ダウンロード**
                                                                                                                                                              8. 8. ダウンロードしたファイル名を \`credentials.json\` に変更
                                                                                                                                                                 9. 9. \`plug-task-bot\` フォルダの中に置く
                                                                                                                                                                   
                                                                                                                                                                    10. ---
                                                                                                                                                                   
                                                                                                                                                                    11. ## ステップ4: GitHub Personal Access Token の作成
                                                                                                                                                                   
                                                                                                                                                                    12. （GitHub 監視機能を使う場合のみ）
                                                                                                                                                                   
                                                                                                                                                                    13. 1. GitHub にログイン
                                                                                                                                                                        2. 2. 右上のアイコン → **「Settings」**
                                                                                                                                                                           3. 3. 左メニューの一番下 → **「Developer settings」**
                                                                                                                                                                              4. 4. **「Personal access tokens」** → **「Tokens (classic)」**
                                                                                                                                                                                 5. 5. **「Generate new token」** → **「Generate new token (classic)」**
                                                                                                                                                                                    6. 6. Note: \`plug-task-bot\`
                                                                                                                                                                                       7. 7. Expiration: お好みで（90日など）
                                                                                                                                                                                          8. 8. スコープ（権限）で以下にチェック:
                                                                                                                                                                                             9.    - \`repo\`（リポジトリ全体の読み取り）
                                                                                                                                                                                                   - 9. **「Generate token」** → 表示されたトークンをコピー
                                                                                                                                                                                                   
                                                                                                                                                                                                   ---
                                                                                                                                                                                               
                                                                                                                                                                                               # Plug Task Bot セットアップ手順書
                                                                                                                                                                                             
                                                                                                                                                                                             株式会社プラグ 社内タスク管理 Discord Bot
                                                                                                                                                                                             
                                                                                                                                                                                             ---
                                                                                                                                                                                             
                                                                                                                                                                                             ## このBotでできること
                                                                                                                                                                                             
                                                                                                                                                                                             1. Discord で `@担当者` にタスクを依頼 → ボタンで承認/辞退
                                                                                                                                                                                             2. 2. 承認されたら自動で Google カレンダーに納期を登録
                                                                                                                                                                                                3. 3. GitHub リポジトリの変更（コミット/PR/Issue/リリース）を自動通知
                                                                                                                                                                                                  
                                                                                                                                                                                                   4. ---
                                                                                                                                                                                                  
                                                                                                                                                                                                   5. ## 必要なもの
                                                                                                                                                                                                   6. 
                                                                                                                                                                                                   - Py
