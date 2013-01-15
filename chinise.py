#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This file is part of the Chinise project.

http://code.google.com/p/chinise/
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Emanuele Bertoldi'
__version__ = '0.0.1'

import sys

import pinyin

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if args[0] == "pinyinize":
        text = args[1]
        print pinyin.pinyinize(text)

    else:
        print "python chinise.py <function> [<args>]"
        print ""
        print "<function> could be one of the following:"
        print ""
        print "pinyinize        Return the pinyin of the specified string"
        print "                 ex: python chinise.py pinyinize \"你好\""
