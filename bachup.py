#created by Alex Hapgood
#Started 02/2018
import boto3
import os
import platform
import datetime
import textwrap
import string
import random

build = 'v0.2a1(inc)'
global now = datetime.datetime.now()

class payload:
    def __init__(self, id, source, time):
        self.source = source
        self.id = id
        self.time = date

#Takes a payload instance, assigns variables, and writes to prefs.txt
def writeToPrefs(payloadInstance):
    payloadInstance.id = id_generator()
    payloadInstance.time = str(now)
    payloadInstance.source = input('Enter target source: ')

    with open('prefs.txt', 'a') as f:
        f.write('\n' + self.id  + ' | ' + self.source + ' | ' + self.time)
        f.close()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def startUp():
    global build

    print('#' * 80)
    print('#     '' _             ______ _     _                       ______  __       ''    #\n'
          '#     ''| |      /\   / _____) |   | |                     / __   |/  |      ''    #\n'
          '#     ''| | _   /  \ | /     | |___| |_   _ ____      ____| | //| /_/ | ____ ''    #\n'
          '#     ''| || \ / /\ \| |     |  ___  | | | |  _ \    / ___) |// | | | |/ _  |''    #\n'
          '#     ''| |_) ) |__| | \_____| |   | | |_| | | | |  | |   |  /__| | | ( ( | |''    #\n'
          '#     ''|____/|______|\______)_|   |_|\____| ||_/   |_|    \_____(_)|_|\_||_|''    #\n'
          '#     ''                                   |_|                               ''    #\n'
          '#     ''                                                                     ''    #')
    print('#                                  By Alex H.                                ''  #')
    print('#' * 80)

    print('\nSystem platform is ++%s++ running release ++%s++.\n' % (platform.system(), platform.release()))
    print('current build is %s' % build)

def init():
    payloadPath = ''

    #existPrefs = bool(distutils.util.strtobool(input('Would you like to use an exiting prefs.txt file?')))
    payloadPath = input('Enter the full filepath to the source enclosing folder or single file: ')







def payloadLocate():
    if os.path.exists(payload.source) and os.path.isdir(payload.source):
        print(os.listdir(source))
        return os.listdir(source)
    else:
        print('no such file or directory.')

def main():
    startUp()
    init()
    getSrcStatus()

if __name__ == "__main__":
    print(main())
