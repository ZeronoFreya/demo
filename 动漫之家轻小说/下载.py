#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request, os

dicts = [{
    'url'       : 'http://xs.dmzj.com/2339/8747/8747_GBK.txt',
    'title'     : '精灵所爱的异世界不良少年',
    'number'    : '01',
    'subtitle'    : ''
}]
saveTo = 'd:/a/'
for f in dicts:
    data = urllib.request.urlopen(f['url']).read()
    name = '{title}( {number} )[{subtitle}].txt'.format(
        title = f['title'],
        number = f['number'],
        subtitle = f['subtitle']
    )
    with open(os.path.join(saveTo, name), "wb") as txt:
        txt.write(data)