#!/usr/bin.env python3
# conding: utf-8
from Framework.OSControl import CommandControl
import os, sys, cgi

class FileControl(object):

    def __init__(self):
        return

    def save_uploaded_file(self, upload_dir):

        form = cgi.FieldStorage()
        if not 'File' in form:
            return "ファイルを入力してください"

        fileitem = form["File"]

        if not fileitem.file:
            return "ファイルを入力してください"

        if not fileitem.filename:
            return "ファイルを入力してください"

        if form["name"].value is "":
            return "名前を入力してください"

        fout = file(os.path.join(upload_dir, form["name"].value + os.path.basename(fileitem.filename)), 'wb')
        while 1:
            chunk = fileitem.file.read(100000)
            if not chunk: break
            fout.write (chunk)
        fout.close()
        return "アップロードしました"

