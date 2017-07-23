#!/usr/bin.env python3
# conding: utf-8
import os

class CommandControl(object):

    def __init__(self, command=''):
        self.command = command

    def PowerOnMainPC(self):
        ret = os.system('sudo etherwake -i eth0 1C:87:2C:40:FE:2F')
        return ('Success!!' if (ret == 0) else "Failed ...")

    def MakeThumbnail(self, file_path, def_dir):
        ret = os.system('sudo convert -thumbnail 100 \"%s\" \"%s\"' \
                        % file_path \
                        % os.path.join(def_dir, os.path.basename(file_path)) \
                        )
        return ret

