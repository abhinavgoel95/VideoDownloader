# VideoDownloader

### Scripts to download videos for covid-19 project


streamlink_master_id.txt contains the IDs of the different video streams.

streamlink_master_list.txt contains the links to the different video streams.

downloader.sh is the script that downloads a 1-minute long video from each link and saves the video in a folder. The folder name is the link ID.

#### To run:
```
  bash downloader.sh <current division> <total number of divisions>
```

#### For example:

```
  bash downloader.sh 0 8
  bash downloader.sh 1 8
  bash downloader.sh 2 8
  bash downloader.sh 3 8
  bash downloader.sh 4 8
  bash downloader.sh 5 8
  bash downloader.sh 6 8
  bash downloader.sh 7 8
```

#### To run:
```
  python3 download.py --part-number 0 --number of parts 8 --download-to path/to/dir --remove-failed True
```
usage: downloader.py [-h] [--part-number M] [--number-of-parts N]
                     [--download-to PATH] [--remove-failed REMOVE]

Covid19 video downloader

optional arguments:
  -h, --help              show this help message and exit
  --part-number M         part number (M)
  --number-of-parts N     number of parts (N)
  --download-to PATH      download path
  --remove-failed REMOVE  delete failed downloads
