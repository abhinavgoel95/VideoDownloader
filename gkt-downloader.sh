#!/bin/bash

# This is only to check for George's Anaconda CAM2 environment at ANL
if [ -x "$(command -v conda)" ]; then
  if [ "$(conda env list | grep ^cam2)" != "" ]; then 
      echo "Found GKT environment at ANL."
      source activate cam2
   fi
fi

# This makes sure we have the required args
if [ "$#" -lt 2 ]; then
  echo "usage: ./downloader.sh part number-of-parts"
  exit 1
fi

part=$1
num_parts=$2
download_to=/projects/SE_HPC/downloaded-videos

python3 downloader_json.py --download-to "$download_to" --number-of-parts "$num_parts" --part-number "$part"
