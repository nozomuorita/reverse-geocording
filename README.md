<h1>Overview</h1>
<ul>
<li>国土交通省・国土数値情報ダウンロードサイトから取得した位置参照情報を用いて、特定の緯度経度の住所を特定する</li>
</ul>
<br>
<h1>Tools</h1>
<ul>
    <li>Windows11</li>
    <li>Python 3.11.4</li>
    <li>Visual Studio Code</li>
</ul>
<br>
<h1>Python Library ver</h1>
<ul>
    <li>pandas：v2.0.3</li>
    <li>urllib3：v2.0.4</li>
</ul>
<br>
<h1>Directory Structure</h1>
<ul>
    <li>data：データ管理ディレクトリ</li>
    <ul>
        <li>address：アドレス情報管理</li>
        <li>prefecture：都道府県情報管理</li>
        <li>origin：元データ管理</li>
    </ul>
    <li>src：ソースファイル管理ディレクトリ</li>
</ul>
<br>
<h1>File Structure</h1>
<ul>
    <li>data</li>
    <ul>
        <li>address-data.csv：各都道府県のアドレス情報</li>
        <li>address-data2.csv：各都道府県の最高(最低)緯度・経度情報</li>
        <li>prefecture-code.csv：都道府県コード情報</li>
        <li>data_origin.csv：元データ</li>
        <li>data_origin_add_address：元データ+アドレス情報データ</li>
    </ul>
    <li>src</li>
    <ul>
        <li>address-data.py：各都道府県のアドレス情報取得</li>
        <li>address-data2.py：各都道府県の最高(最低)緯度・経度情報取得</li>
        <li>reverse-geocording.py：都道府県特定、データ追加</li>
    </ul>
</ul>
<br>
<h1>特定の緯度・経度から都道府県市区町村を特定する</h1>
<p><b>とりあえず実行してみる用</b></p>
<ol>
    <li>このリポジトリをダウンロードする</li>
    <li>data/origin/data_origin.csvを自分の車両データに置き換える</li>
    <li>src/reverse-geocording.pyを実行する</li>
    <li>data_origin_add_address.csvが作成され、データの最後の列にアドレス情報(都道府県名)が追加される</li>
    <li>※時間の差分については考慮していないので、時刻が大きく異なるデータ間であっても同じ住所が記載されている場合がある(要改善)</li>
</ol>
<p><b>補足(要改善)</b></p>
<ul>
    <li>都道府県の特定は20行間隔で行っている。間のデータは同じ都道府県で補完</li>
    <li>文字コードの影響により、Excelでcsvファイルを開くと文字化けする。pandasで開けば見れる。データ書き込み時に文字化け対策する必要あり</li>
    <li>時間の差分については考慮していないので、時刻差の大きいデータ間であっても同じ都道府県となっている可能性がある。(対策)データ間の時刻差が一定以上なら優先処理するなど</li>
</ul>

<h1>References</h1>
<ul>
    <li><a href='https://nlftp.mlit.go.jp/', target="_blank">国土交通省国土数値情報ダウンロードサイト(データ取得元)</a></li>
    <!-- <li><a href='#'>XML形式からのデータ取得参考サイト</a></li>
    <li><a href='#'>任意の位置の海岸線からの距離計測</a></li>
    <li><a href='#'>任意の位置の都道府県・市区町村特定</a></li> -->
</ul>