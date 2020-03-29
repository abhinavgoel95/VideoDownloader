import os
import time
import sys
import datetime
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description='Covid19 video downloader')
parser.add_argument('--part-number', dest='M', type = int,
                    default=0,
                    help='part number (M)')

parser.add_argument('--number-of-parts', dest='N', type = int,
                    default=8,
                    help='number of parts (N)')

parser.add_argument('--download-to', dest='path',
                    default='.',
                    help='download path')

args = parser.parse_args()
print(args)

with open('streamlink_master_id.txt') as f:
    ids = f.read().splitlines()

with open('streamlink_master_list.txt') as f:
    links = f.read().splitlines()

id_map = dict(zip(ids, links))


index = args.M
while index < len(ids):
        key = ids[index]
        print(index+1, key)
        try:
            os.makedirs(args.path+'/'+key)
        except FileExistsError:
            pass    
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        call("timeout -sHUP 10s streamlink \""+id_map[key]+"\" best -o "+args.path+"/"+key+"/"+now+".mp4", shell = True)
        index += args.N