#!/bin/bash

source activate cam2

if [ "$#" -lt 2 ]; then
  echo "usage: ./downloader.sh part number-of-parts"
  exit 1
fi

DATETIME=`date +%Y-%m-%d_%H_%M_%S`
echo="RUNNING!"
n=$1;
wc=($(wc -l streamlink_master_id.txt))
num=${wc[0]}
videodir=downloaded-videos
mkdir -p $videodir
echo $num
echo "$BASH_VERSION"
readarray -t a < streamlink_master_id.txt
while IFS="" read -r p || [ -n "$p" ]
do
       if [ $n -gt $num ]; then
		break
       fi
       thisvideodir=$videodir/"${a[n]}"
       echo ${a[n]} "-> downloads to $thisvideodir"
       mkdir -p "$thisvideodir"
       echo $n
       timeout -sHUP 60s streamlink "$p" best -o "$thisvideodir"/$DATETIME.mp4
       n=$(($n+$2))
done < streamlink_master_list.txt
#EOF
