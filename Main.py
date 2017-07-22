#HTTPサーバーシンプル実行
import http.server
server_address = ("", 8000)
handler_class = http.server.CGIHTTPRequestHandler #1 ハンドラを設定
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()

#HTTPSサーバーシンプル実行
#from http.server import HTTPServer, CGIHTTPRequestHandler
#import ssl
#httpd = HTTPServer(("", 443),CGIHTTPRequestHandler)
#httpd.socket = ssl.wrap_socket(httpd.socket,
#	keyfile="/home/web/path/to/key.pem",
#	certfile="/home/web/path/to/cent.pem", server_side=True)
#CGIHTTPRequestHandler.have_fork=False # Force the use of a subprocess
#httpd.serve_forever()

