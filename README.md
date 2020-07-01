# Django
Django開発環境

## Prerequisites

[Docker](https://www.docker.com/) と [Docker Compose](https://docs.docker.com/compose/install/)をインストールしてください

## Installation

**Django/.env** ファイルを下記のように作成します
```vim
DB_NAME=django
DB_USER=admin
DB_PASS=admin
DB_PORT=3306
TZ=Asia/Tokyo
SECRET_KEY=qawsedrftgyhujikolp;@:[]
```

下記コマンドで起動します。
```bash
docker-compose -f docker-compose.dev.yml up -d --build
```

成功したらHello Worldが表示されます http://localhost


## エイリアスの設定例

bashを使っている場合、下記のようにエイリアスを設定しておくと開発時に楽です。

**~/.bashrc**を下記のように作成
```vim
alias dcdev='docker-compose -f docker-compose.dev.yml'
```
もし必要なら **~/.bash_profile** も下記のように作成してください。
```vim
if [ -f ~/.bashrc ] ; then
  . ~/.bashrc
fi
```

すると、下記のように短いコマンドでdockerを使用できます。
```vim
dcdev up -d --build
```
