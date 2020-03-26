#!/bin/bash
DATETIME=`date +%Y-%m-%d_%H_%M_%S`
echo="RUNNING!"
n=$1;
wc=($(wc -l streamlink_master_id.txt))
num=${wc[0]}
echo $num
echo "$BASH_VERSION"
readarray -t a < streamlink_master_id.txt
while IFS="" read -r p || [ -n "$p" ]
do
       if [ $n -gt $num ]; then
		break
       fi
       echo ${a[n]}
       mkdir -p "${a[n]}"
       echo $n
       timeout -sHUP 60s streamlink "$p" best -o "${a[n]}/$DATETIME.mp4"
       n=$(($n+$2))
done < streamlink_master_list.txt
#EOF