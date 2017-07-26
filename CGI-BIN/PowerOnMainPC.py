#!/usr/bin.env python3
# conding: utf-8
from RssReader.RssParser import parse_rss
from Framework.OSControl import CommandControl
from RssReader.HttpHandler import Request, Response
import cgitb; cgitb.enable()            # (1)

res=Response()
cmd=CommandControl()
body=cmd.PowerOnMainPC()
res.set_body(Response.get_htmltemplate() % body)
print(res)
