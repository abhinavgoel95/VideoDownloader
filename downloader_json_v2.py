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

parser.add_argument('--num_tries', dest='tries', default=1, type=int, help='number of tries to retry download if file size 0 or not downloaded')

args = parser.parse_args()
print(args)

id_map = dict()
with open('ids_links.json', 'r') as f:
    id_map = json.load(f)

ids= list(id_map.keys())

print(json.dumps(id_map, indent=2))

index = args.M
while index < len(ids):
        key = ids[index]
        print("Camera # ", index+1, key)
        try:
            os.makedirs(args.path+'/'+key)
        except FileExistsError:
            pass    
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        returnval = 1
        
        success = False
        for i in range(args.tries):
            if 'skyline' in id_map[key]:
                print('skyline camera')
                command="ffmpeg $(youtube-dl -g \""+id_map[key]+"\" | sed \"s/.*/-i &/\") -t 60 -strict -2 -c copy "+args.path+"/"+key+"/"+now+".mp4"
                print("Running", command)
                returnval = call(command, shell=True)
            else:
                print('non-skyline camera')
                command="timeout -sHUP 60s streamlink \""+id_map[key]+"\" best -o "+args.path+"/"+key+"/"+now+".mp4"
                print("Running", command)
                returnval = call(command, shell = True)

            if args.remove:
                try:
                    filesize = Path(args.path+"/"+key+"/"+now+".mp4").stat().st_size
                    if filesize == 0:
                        print('empty')
                        print('returnval', returnval)
                        print(args.path+"/"+key+"/"+now+".mp4:", "File size 0. File deleted.")
                        os.unlink(args.path+"/"+key+"/"+now+".mp4")
                    else:
                        print("success")
                        success = True
                        print('returnval', returnval)
                except:
                    print('failed to download')
                    print('returnval', returnval)
                    print(args.path+"/"+key+"/"+now+".mp4:", "File not downloaded.")
                    if os.path.exists(args.path+"/"+key) and os.path.isdir(args.path+"/"+key):
                        if not os.listdir(args.path+"/"+key):
                            os.rmdir(args.path+'/'+key)
            if success:
                break
            time.sleep(2)

        index += args.N

# If this line doesn't show in the output, we are not processing all of the cameras (and need to increase job time)
print("all cameras processed")

