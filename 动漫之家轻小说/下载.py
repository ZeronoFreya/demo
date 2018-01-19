#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request, os
from chinese_digits import chineseToDigits
dicts = [
    {
        "url": "http://xs.dmzj.com/1671/6239/6239_GBK.txt",
        "title": "为美好的世界献上祝福！",
        "subtitle": "第二卷 中二病也想当魔女"
    },{
        "url": "http://xs.dmzj.com/1671/6147/6147_GBK.txt",
        "title": "为美好的世界献上祝福！",
        "subtitle": "第一卷 啊啊，没用的女神大人"
    }
]
saveTo = 'd:/a/'
for f in dicts:
    data = urllib.request.urlopen(f['url']).read()
    subtitle = f['subtitle'].split(' ',1)
    name = '{title}( {number} )[{subtitle}].txt'.format(
        title = f['title'],
        number = chineseToDigits(subtitle[0], 2, 0),
        subtitle = subtitle[1]
    )
    with open(os.path.join(saveTo, name), "wb") as txt:
        txt.write(data)