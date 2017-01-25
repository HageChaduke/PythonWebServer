# 標準モジュールをimportする #
import cgi
import os
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
