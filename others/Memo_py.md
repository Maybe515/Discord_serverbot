## Python + IDE導入
### 参考文献
- [Pythonの開発環境を用意しよう！（Windows）](https://prog-8.com/docs/python-env-win)
- [PyCharmインストール手順＜Windows向け＞](https://sukkiri.jp/technologies/ides/pycharm/pycharm-win.html)
- [Anaconda完全アンインストール：手順と注意点](https://beginner-engineers.com/uninstall-anaconda/)
- [pythonでimportできない時の調査](https://qiita.com/jmtsn/items/866a601424131c923b75)
- [【Python入門】import ができない！を最速で解決する3ステップ](https://www.sejuku.net/blog/71311)
- [Pythonモジュールのimportができなくなったときの対処記録](https://qiita.com/Kent_recuca/items/349586e9c034535f2991)
- [インストールした外部ライブラリが import 出来ない](https://ja.stackoverflow.com/questions/59693/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%9F%E5%A4%96%E9%83%A8%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%8C-import-%E5%87%BA%E6%9D%A5%E3%81%AA%E3%81%84)
<br>

## def
関数を定義するためのキーワード。<br>

### 基本的な関数定義
```python
def test():
  print("Hello, World!")    # コンソールに「Hello, World!」と出力する

test()    # 関数の呼び出し
```
`def test():`が関数の定義部分となり、`test`が関数名。testの後ろの`()`は引数を指定する部分。  
括弧内に値や変数を入力することで、この関数内に情報を持ち込むことができる。<br>
<br>

### 引数を指定する関数定義
```python
def test(a):
  print(f"Hello, {a}!")    # コンソールに「Hello, ○○!」と出力する

test("Wndows")    # 関数の呼び出し
```
基本的な関数定義に引数`a`を追加して定義。この関数内では関数を呼び出した際に引数で指定した情報が`a`という変数として使用できる。<br>
例では`Windows`という文字列が変数`a`に格納されて、「Hello, Windows!」とコンソール上に出力される。<br>
<br>

### 戻り値を指定する関数定義
```python
def test(a, b):
  return a + b    #  変数aと変数b を加算

result = test(1, 2)    # 関数の呼び出し, 変数result に結果を格納
print(result)          # 変数result に格納されている値を出力
```
基本的な関数定義に引数`a`と`b`を追加して定義。<br>
`return`を指定することによって、関数内の処理で得られた情報を呼び出し元（メインルーチン）へ戻すことができる。<br>
例では、変数`a`に1、変数`b`に2という数字が格納されて関数内に情報が持ち込まれる。<br>
`return a + b`で加算処理されて、呼び出し元に戻り、変数`result`に格納される。<br>
`print(result)`で加算結果(`result`)が出力される。
