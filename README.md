# SlashCommandTest_Py

# Japanese
## 概要
本プロジェクトは、discord.py を用いたスラッシュコマンド実装の検証を目的とした、シンプルな Discord Bot です。
起動時にグローバルコマンドを同期し、動作確認用の test コマンドを提供します。

## 使用技術
- 言語: Python
- ライブラリ/フレームワーク: discord.py, python-dotenv
- データベース: なし
- その他: Discord Application Commands（Slash Commands）, .env による環境変数管理

## 使い方
### 前提条件
- Python 3.10 以上
- Discord Developer Portal で作成した Bot トークン

### インストール方法
```bash
git clone https://github.com/username/project.git
cd SlashCommandTest_Py
pip install discord.py python-dotenv
```

### 基本的な使い方
1. プロジェクト直下に .env ファイルを作成してください。
2. 以下の形式で Bot トークンを設定してください。

```env
token=YOUR_BOT_TOKEN
```

3. Bot を起動してください。

```bash
python Program/main.py
```

4. Discord 上で /test を実行し、文字列引数を渡して応答を確認してください。

## 主な機能
- 起動時のグローバルスラッシュコマンド同期
- /test コマンドによるエコー応答
- 最小構成でのコマンド追加・検証がしやすい構造

## 設定
- 環境変数
	- token: Discord Bot トークン
- 実装ファイル
	- Program/main.py: コマンド定義と Bot の起動処理

## 参考サイト

* PDFをページ内に埋め込んで表示するGoogle Docs Viewer(スマホ, PC): https://webbibouroku.com/Blog/Article/google-docs-viewer
* JavaDrive | switch文を使った条件分岐: https://www.javadrive.jp/start/if/index4.html
* ぺんたん | 文字列の部分一致検索を行う方法: https://pentan.info/java/sample/str_search.html
* POTEPAN STYLE | 【Java】URLをエンコード・デコードする方法についてサンプル付きで解説！: https://style.potepan.com/articles/28793.html
* Oracle | URLEncoder (Java Platform SE 8 ): https://docs.oracle.com/javase/jp/8/docs/api/java/net/URLEncoder.html
* Qiita | Javaの例外処理について: https://qiita.com/pitan109/items/c9910edddc007126df41

## ライセンス
Unlicense license

# English
## Overview
This project is a simple Discord bot for testing and learning slash command implementation with discord.py.
It connects to Discord, synchronizes global application commands, and provides a basic `/test` command that echoes input text.

## Tech Stack
- Language: Python
- Libraries/Frameworks: discord.py, python-dotenv
- Database: None
- Others: Discord Application Commands (Slash Commands), `.env`-based secret management

## Quick Start
### Prerequisites
- Python 3.10 or later
- A Discord bot application and token

### Installation
```bash
git clone https://github.com/username/project.git
cd SlashCommandTest_Py
pip install discord.py python-dotenv
```

### Basic Usage
1. Create a `.env` file in the project root.
2. Add your bot token:
```env
token=YOUR_BOT_TOKEN
```
3. Run the bot:
```bash
python Program/main.py
```
4. In Discord, execute `/test` with a text argument.

## Key Features
- Global slash command synchronization on startup
- `/test` command for simple text echo
- Lightweight structure for command testing and extension

## Configuration
- Environment variable:
  - `token`: Discord bot token used by `client.run(...)`
- File to edit:
  - `Program/main.py`: command definitions and bot behavior

## Refer sites

* PDFをページ内に埋め込んで表示するGoogle Docs Viewer(スマホ, PC): https://webbibouroku.com/Blog/Article/google-docs-viewer
* JavaDrive | switch文を使った条件分岐: https://www.javadrive.jp/start/if/index4.html
* ぺんたん | 文字列の部分一致検索を行う方法: https://pentan.info/java/sample/str_search.html
* POTEPAN STYLE | 【Java】URLをエンコード・デコードする方法についてサンプル付きで解説！: https://style.potepan.com/articles/28793.html
* Oracle | URLEncoder (Java Platform SE 8 ): https://docs.oracle.com/javase/jp/8/docs/api/java/net/URLEncoder.html
* Qiita | Javaの例外処理について: https://qiita.com/pitan109/items/c9910edddc007126df41

## License
Unlicense license
