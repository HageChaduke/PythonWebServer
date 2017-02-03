# 標準モジュールをimportする #
import cgi
import os
from bsddb.test.test_all import charset
class Request(object):

    """
    HTTPのリクエストをハンドリングするクラス
    CGI側でインスタンスを生成することによって利用する
    クエリデータや環境変数へのアクセス、主要ヘッダへの
    アクセス用メソッドを提供
    """
    def __init__(self, environ=os.environ):
        """
        インスタンスの初期化メソッド
        クエリ、環境変数をアトリビュートとして保持する
        """
        self.form=cgi.FieldStorage()
        self.environ=environ

class Response(object):
    """
    HTTPのレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成して利用する
    レスポンスやヘッダの内容の保持、ヘッダを含めたレスポンスの
    送信を行う
    """
    def  __init__(self, charset='utf-8'):
        """
        インスタンスの初期化メソッド
        ヘッダ用の辞書、本文用の文字列などを初期化する
        """
        self.headers=('Content-type' :'text/html;charset=%s' %
                      charset)
        self.body=""
        self.status=200
        self.status_message=''
    def set_header(selfself, name, value):
        """
        レスポンスのヘッダを設定する
        """
        self.headers(name)=value
    def get_header(self, name, value):
        """
        レスポンスのヘッダを設定する
        """
        self.headers(name)=value
    def get_header(selfself, name):
        """
        設定済みのレスポンス用ヘッダを返す
        """
        return self.headers.get(name, None)