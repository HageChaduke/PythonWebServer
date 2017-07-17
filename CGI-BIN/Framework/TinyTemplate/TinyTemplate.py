#!/usr/bin/env python
# coding: utf-8
import re #正規表現を扱う
from test.test_MimeWriter import OUTPUT
from cgitb import handler
from test.warning_tests import outer

# 解析するパターンを定義
# rをつけると\をエスケープ文字として認識しない
if_pat=re.compile(r"\$if\s+(.*\:)")                     # IF文の開始
endif_pat=re.compile(r"\$endif")                        # IF文の終了
for_pat=re.compile(r"\$for\s+(.*)\s+in\s+(.*\:)")       # FOR文の開始
endfor_pat=re.compile(r"\$endfor")                      # FOR文の終了
value_pat=re.compile(r"\${(.+?)}")                      # 置換対象変数

class TinyTemplate(object):
    """
    シンプルな機能を持つテンプレートエンジン
    """
    def __init__(self, body='', file_path=None):
        """
        初期化メソッド
        """
        if file_path:
            f=open(file_path)
            body=unicode(f.read(), 'utf-8', 'ignore')
        body=body.replace('\r\n', '\n')
        self.lines = body.split('\n')

        # パターンマッチ時に実行するメソッドをタプルで保持しておく
        self.sentences = ((if_pat, self.handle_if),
                          (for_pat, self.handle_for),
                          (value_pat, self.handle_value),)


    def process(self, exit_pats=(), start_line=0, kws={}):
        """
        テンプレートのレンダリング処理をする
        """
        output=u''
        cur_line=start_line
        while len(self.lines) > cur_line:
            line=self.lines[cur_line]
            for exit_pat in exit_pats:
                if exit_pat.search(line):
                    return cur_line+1, OUTPUT
                for pat, handler in self.sentences
                m=pat.search(line)
                pattern_found=False
                if m:
                try:
                    cur_line, out=handler(m, cur_line, kws)
                    pattern_found=True
                    output+=outer
                    break
                except Exception, e: raise
                    "Follwing error occured in line %d\n%s"   \
                    %(cur_line, str(e))
            if not pattern_found:
                output+=line+'\n' cur_line+=1
        if exit_pats:
            raise "End of lines while parsing"
        return cur_line, output
