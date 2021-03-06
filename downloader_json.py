import os
import time
import sys
import datetime
from subprocess import call
import argparse
from pathlib import Path
import json

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

parser.add_argument('--remove-failed', dest='remove',
                    default=True,
                    help='delete failed downloads')

args = parser.parse_args()
print(args)

id_map = dict()
with open('ids_links.json', 'r') as f:
    id_map = json.load(f)

ids= list(id_map.keys())

print(json.dumps(id_map, indent=2))

errorfile = open('errorfile.txt', 'a+')

index = args.M
while index < len(ids):
        key = ids[index]
        print(index+1, key)
        try:
            os.makedirs(args.path+'/'+key)
        except FileExistsError:
            pass    
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        call("timeout -sHUP 60s streamlink \""+id_map[key]+"\" best -o "+args.path+"/"+key+"/"+now+".mp4", shell = True)
        if args.remove:
            try:
                filesize = Path(args.path+"/"+key+"/"+now+".mp4").stat().st_size
                if filesize == 0:
                    print(args.path+"/"+key+"/"+now+".mp4:", "File size 0. File deleted.", file = errorfile)
                    os.unlink(args.path+"/"+key+"/"+now+".mp4")
            except:
                print(args.path+"/"+key+"/"+now+".mp4:", "File not downloaded.", file = errorfile)
                if os.path.exists(args.path+"/"+key) and os.path.isdir(args.path+"/"+key):
                    if not os.listdir(args.path+"/"+key):
                        os.rmdir(args.path+'/'+key)

        index += args.N