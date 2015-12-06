#!/usr/bin/env python

import sys
import json
import urllib2

##
# @file dict.py
# @translation  
# @author Feei(wufeifei@wufeifei.com)
# @update by tang45, support translate chinese
# @version 1.0
# @date 2015-12-06



class Dict:
    api = 'http://fanyi.youdao.com/openapi.do?keyfrom=bortherland&key=876662865&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        if len(argv) == 1:
            self.api = self.api + argv[0]
            self.translate()
        else:
            print 'NO QUERY'

    def translate(self):
        content = urllib2.urlopen(self.api).read()
        self.content = json.loads(content)
        self.parse()

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            try:
                u = self.content['basic']['us-phonetic']
                e = self.content['basic']['uk-phonetic']
                explains = self.content['basic']['explains']
            except KeyError:
                u = 'None'
                e = 'None'
                explains = 'None'
            print '\033[1;31m################################### \033[0m'
            print '\033[1;31m# \033[0m', self.content['query'], self.content['translation'][0], '(U:', u, 'E:', e, ')'
            if explains != 'None':
                for i in range(0, len(explains)):
                    print '\033[1;31m# \033[0m', explains[i]
            else:
                print '\033[1;31m# \033[0m Explains None'
            print '\033[1;31m################################### \033[0m'
            # Phrase
            # for i in range(0, len(self.content['web'])):
            #     print self.content['web'][i]['key'], ':'
            #     for j in range(0, len(self.content['web'][i]['value'])):
            #         print self.content['web'][i]['value'][j]
        elif code == 20:  # Text to long
            print 'TEXT TO LONG'
        elif code == 30:  # Trans error
            print 'TRANSLATE ERROR'
        elif code == 40:  # Don't support this language
            print 'NOTT SUPPORT THIS LANGUAGE'
        elif code == 50:  # Key failed
            print 'KEY FAILED'
        elif code == 60:  # Don't have this word
            print 'NO RESULT'

if __name__ == '__main__':
    Dict(sys.argv[1:])
