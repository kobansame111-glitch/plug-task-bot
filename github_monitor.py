"""
GitHub 監視モジュール

指定したリポジトリの以下の変更を定期的にチェックして、
Discord に通知を送ります：
  - 新しいコミット（Push）
    - プルリクエスト（PR）の作成・更新
      - Issue の作成・更新
        - 新しいリリース
        """

import datetime
from github import Github

import config


class GitHubMonitor:
      """
          GitHub リポジトリを監視するクラス。

              使い方:
                      monitor = GitHubMonitor()
                              updates = monitor.check_all_repos()
                                      # updates にはリポジトリごとの変更情報が入っている
                                          """

    def __init__(self):
              """
                      GitHubMonitor を初期化します。
                              GitHub トークンを使って API に接続します。
                                      """
              self.github = Github(config.GITHUB_TOKEN)

        # 最後にチェックした時刻（起動時は「5分前」からスタート）
              self.last_check = datetime.datetime.now(
                  datetime.timezone.utc
              ) - datetime.timedelta(minutes=config.GITHUB_CHECK_INTERVAL)

    def check_all_repos(self) -> list[dict]:
              """
                      設定されたすべてのリポジトリをチェックして、
                              新しい変更があれば通知用データのリストを返します。

                                      戻り値:
                                                  通知データのリスト。各要素は以下の形式:
                                                              {
                                                                              "type": "commit" | "pull_request" | "issue" | "release",
                                                                                              "repo": "owner/repo",
                                                                                                              "title": "タイトル",
                                                                                                                              "url": "GitHubのURL",
                                                                                                                                              "author": "作成者",
                                                                                                                                                              "description": "説明文"
                  }
                          """
              all_updates = []

        for repo_name in config.GITHUB_REPOS:
                      try:
                                        repo = self.github.get_repo(repo_name)

                          # 各種チェックを実行
                                        all_updates.extend(self._check_commits(repo))
                                        all_updates.extend(self._check_pull_requests(repo))
                                        all_up"""
                        GitHub 監視モジュール

                        指定したリポジトリの以下の変更を定期的にチェックして、
                        Discord に通知を送ります：
                          - 新しいコミット（Push）
                          - プルリクエスト（PR）の作成・更新
                          - Issue の作成・更新
                          - 新しいリリース
                        """

          import datetime
from github import Github

import config


class GitHubMonitor:
      """
          GitHub リポジトリを監視するクラス。

              使い方:
                      monitor = GitHubMonitor()
                              updates = monitor.check_all_repos()
                                      # updates にはリポジトリごとの変更情報が入っている
                                          """

 
