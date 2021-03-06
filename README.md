# tools
なんか便利なツールを作って溜め込んでるだけ

## aifc2wav
AIFC, AIFFをwaveに変換する

実行は，`aifc2wav.py sample.aifc`となるように（$1が変換対象のファイル名）．

変換後のwaveファイルは，変換元ファイルと同じ名前，同じ場所に出力される．

## brew_update
`brew_update.py`を実行したら，

- `brew update`
- `brew upgrade`
- `brew prune`
- `brew cleanup`
- `brew doctor`

が勝手に実行される．

## cmt_txt
英文から単語数をカウントする．ただし，"-"でつながった熟語は1単語として扱う．

実行するときは，`$cnt_txt.py textfile.txt`，となるようにする．第一引数が読み込む英文が入力されたtxtファイル．
txtファイル以外でも開けると思うが，それはPythonが自力でopenできるものに限る．

## convert_color

## convert_encoding
指定したディレクトリ内のファイルの文字コードを，全てUTF-8で**上書き**する．元の文字コードのデータは残らないので要注意！

実行するときは，`$convert_encoding.py target_directory`となるようにする．第一引数が変換対象のディレクトリ．

## hof

## LIS3DH
I2C通信を使った，3軸加速度センサ[LIS3DH](http://akizukidenshi.com/catalog/g/gK-06791/)を実行するArudinoのスケッチと，[回線図](./LIS3DH/wiring.jpg)．

ArudinoでLIS3DHを使うためには電圧の変換が必要なので，回路図では[PCA306](http://akizukidenshi.com/catalog/g/gM-05452/)を使用．

回路図では，<font color="Red">**赤**が5V</font>，<font color="Orange">**オレンジ**が3.3V</font>，**黒**がGND，<font color="PeachPuff">**黄色**がSCL</font>，<font color="LimeGreen">**緑**がSDL</font>となっている．

## qrcode
引数で入力したテキストをQRコード（.png）に変換する．

実行するときは，`$make_qr.py text QR-image's name`とする．

## md2pdf
node.jsの[markdown-pdf](https://github.com/alanshaw/markdown-pdf)を使って，.mdファイルを.pdfに変換する．

markdown-pdfの出力時の文字サイズは0.625emと小さいので，それを設定可能（初期値は1em）に変更

実行時は，`python md2pdf markdown-name fontsize output-name`となる．

- markdown-name: 変換したいmarkdownファイル
- fontsize: 文字サイズ（デフォルトは1em）
- output-name: 出力するPDFの名前（デフォルトはmarkdownのファイル名と一緒）