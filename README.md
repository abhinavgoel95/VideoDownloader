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
  bash downloader.sh 1 8
  bash downloader.sh 2 8
  bash downloader.sh 3 8
  bash downloader.sh 4 8
  bash downloader.sh 5 8
  bash downloader.sh 6 8
  bash downloader.sh 7 8
```
