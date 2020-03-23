#!/bin/bash
DATETIME=`date +%Y-%m-%d_%H_%M_%S`
echo="RUNNING!"
n=0;
echo "$BASH_VERSION"
readarray -t a < streamlink_master_id.txt
while IFS="" read -r p || [ -n "$p" ]
do
       echo ${a[n]}
       mkdir -p "${a[n]}"
       timeout -sHUP 60s streamlink "$p" best -o "${a[n]}/$DATETIME.mp4"
       n=$(($n+1))
done < streamlink_master_list.txt
#EOF