#!/usr/bin/env python
#coding=utf-8
import json;
import subprocess

torrent = 'd:/project/GitHub/aria2/d.torrent'

def mkJsonFile(_dict, _idx, _path, _len):
    for x in _path.split('/'):
        if x == '.':
            continue
        _dict = _dict.setdefault(x,{})
    _dict['idx'] = _idx
    _dict['len'] = _len

def showFiles(torrent):
    cmd = ''.join( ('aria2c -S "', torrent, '"') )
    file_out = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _list = {'Files':{}}
    begin = False
    keys = ['Mode','Info Hash','Total Length','Name','Files']
    files = ''
    while True:
        if subprocess.Popen.poll(file_out)==0: #判断子进程是否结束
            break
        line = file_out.stdout.readline().decode('utf-8').rstrip('\n')
        if begin:
            if line.startswith('===+'):
                files = ''
                continue
            elif line.startswith('---+'):
                file = files.split('|')
                # _list['Files'].append({
                #     'idx' : file[0].strip(),
                #     'path': file[1].strip(),
                #     'len' : file[2].strip()
                # })
                mkJsonFile(_list['Files'], file[0].strip(), file[1].strip(), file[2].strip() )
                files = ''
                continue
            files = ''.join( (files, line.strip()) )
        else:
            slt = line.split(':', 1)
            if slt[0] in keys:
                if slt[0] == 'Files':
                    begin = True
                else:
                    _list[slt[0]] = slt[1].lstrip()
    return _list

# print( showFiles(torrent) )
print( json.dumps(showFiles(torrent), indent=4) )