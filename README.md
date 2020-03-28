# フロントマターを含めてMarkdownファイルを作成するスクリプト

Gridsomeで作ったポートフォリオサイトのブログ記事を書くときに、ディレクトリ作成やフロントマターの諸設定を含むMarkdownファイルをサクッと作るためのスクリプトです。

▶︎[nnamm works](https://portfolio.nnamm.com)

## 機能

config.iniに設定した任意のディレクトリに、以下の記事単位のディレクトリ（001、002以降昇順）を作成します。

```
/User/hogehoge/blog/ 配下に

|__001
|    |__img/
|    |__001_YYMMDD.md
|
|__002
|    |__img/
|    |__002_YYMMDD.md
|
```

## その他

サイトのポストタイプは3種類ありますが（blog/graphic/photo）、現在はblogのためだけに使いますので拡張性は考慮していません。
