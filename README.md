# autogen

Autogen(マルチエージェント)で遊ぶ

## devcontainer で環境構築してみた

※正規のやり方ではない

1. devcontainer.json を準備（コピーした）
2. Dockerfile を準備（コピーした）
3. `vscode>devcontainer: Open Folder in Container ...` を実行して、`.devcontainer`を選択
4. 勝手にコンテナ実行が始まる
   :::note warn
   Warning
   なぜか一度目はエラーが出て再試行させられる（原因不明）
   :::
5. コンテナ環境完成

### memo

- .devcontainer では vscode の拡張機能も.json に記載する
  ⇒ 特に ms-python.python (python の補完は必要)
  ⇒ このあたりのテンプレート的なものは抑えておいた方がいいかも
