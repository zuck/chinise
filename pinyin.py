#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re

def pinyinize(text):
    """Return pinyin reading of a string of traditional or simplified Hanzi.
    """
    data_path = 'cedict_ts.u8'
    dictionary = {}
    for line in open(data_path):
        if line[0] == '#':
            continue
        r = re.search('^\s*(.+)\s+(.+)\s+\[(.+)\]\s+\/(.+)\/\s*$', line)
        k1 = r.group(1)
        k2 = r.group(2)
        p = r.group(3).replace(" ", "")
        m = r.group(4)
        dictionary[k1] = (p, m)
        dictionary[k2] = (p, m)

    output = []
    buff = text
    while len(buff) > 0:
        found = False
        buff2 = buff
        while len(buff2) > 0:
            if dictionary.has_key(buff2):
                output.append(dictionary[buff2][0])
                buff = buff[len(buff2):]
                found = True
                buff2 = ""
            else:
                buff2 = buff2[:-1]
        if not found and buff:
            output.append(buff[0])
            buff = buff[1:]
             
    return output
