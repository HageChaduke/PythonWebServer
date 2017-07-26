#!/usr/bin.env python3
# conding: utf-8
from RssReader.RssParser import parse_rss
from RssReader.HttpHandler import Request, Response
from Framework.UploadManager import FileControl
import cgitb; cgitb.enable()            # (1)

res=Response()
fctrl = FileControl()
body=fctrl.save_uploaded_file('Images_otayori')
res.set_body(Response.get_htmltemplate() % body)
print(res)
