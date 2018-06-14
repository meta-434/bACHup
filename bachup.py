#created by Alex Hapgood
#Started 02/2018
import boto3
import os
import platform
import datetime
import textwrap
import string
import random
import distutils

build = 'v0.2a1(inc)'
now = datetime.datetime.now()

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

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
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
    idHistory = []
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response ['Buckets']]

    existPrefs = input('Would you like to use an exiting prefs.txt file? y/n ')
    if existPrefs == "y" or existPrefs == "Y":
        with open('prefs.txt') as ins:
            history = [line.rstrip('\n') for line in ins]
            for item in history:
                idHistory.append(item[:6])

        print("\nBucket list: %s" % buckets)
        print("idHistory list: %s" % idHistory)

        #print(set(idHistory).intersection(set(buckets)))
        if bool(set(idHistory).intersection(set(buckets))):
            print("SUCCESS - MATCH FOUND.\n")
        else:
            print("NO MATCHING BUCKETS FOUND.\n")
        ins.close()

    inOrOut = input('[B]ackup / [R]estore? ')
    if inOrOut == "B" or inOrOut == "b":
        payloadPath = input('Enter the full filepath to the source enclosing folder or single file: ')

    else:
        restoreBucket = input("Enter id of bucket to preview contents for restore: ")
        sys.exit(1)


def payloadLocate():
    if os.path.exists(payloadPath) and os.path.isdir(payloadPath):
        print(os.listdir(source))
        return os.listdir(source)
    else:
        print('no such file or directory.')

def main():
    startUp()
    init()
    payloadLocate()

if __name__ == "__main__":
    print(main())
