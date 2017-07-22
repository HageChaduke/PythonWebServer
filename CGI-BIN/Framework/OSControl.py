#!/usr/bin.env python3
# conding: utf-8
import os

class CommandControl(object):

    def __init__(self, command=''):
        self.command = command

    def PowerOnMainPC(self):
        ret = os.system('sudo etherwake -i eth0 1C:87:2C:40:FE:2F')
        return ('Success!!' if (ret == 0) else "Failed ...")
