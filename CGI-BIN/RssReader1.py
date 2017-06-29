#!/usr/bin.env python
# conding: utf-8
from RssParser import parse_rss
from HttpHandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()            # (1)

form_body=u"""
<form method="POST" action="/cgi-bin/RssReader1.py">
 RSSのURL:
 <input type="text" size="40" name="url" value="%s"/>
 <input type="submit" />
</form>"""
rss_parts=u"""
#<h3><a href="%(link)s">%(title)s</a></h3>
<h3><a href="%(link)s">%(title)s</a></h3>
<p>%(description)s</p>
"""
content=u"URLを入力してください"
req=Request()
if req.form.has_key('url'):
    try:
        rss_list=parse_rss(req.form['url'].value)
        content=""
        for d in rss_list:
            content+=rss_parts%d
    except:
        pass

res=Response()
body=form_body%req.form.getvalue('url', '')
body+=content
rss.set_body(get_htmltemplate()%body)
print(res)
