#!/usr/bin/env python3

"""
Panopto Video Downloader
Downloads videos from Panopto as a .ts stream.

How to use:
1. Go to the video specified in your web browser, e.g. https://uniofbath.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cf3a64a1-936c-45b3-92de-72f8fecdb08b
2. Open the network tab in your developer console (Ctrl + Shift + E)
3. Refresh the page, select the 'media' filter, and play the video.
4. Look for files e.g. 00000.ts, 00001.ts. Double click on one.
5. Copy the url you are taken to, and remove the trailing '#####.ts'
6. Run download_video.py with the url as the video parameter.
7. Optionally specify the filename with -n "FILENAME.ts".

XDGFX, 2020
"""

import argparse
import os

import requests

parser = argparse.ArgumentParser(description='Download videos from Panopto')
parser.add_argument('url', type=str, help='the video url')
parser.add_argument('-n', dest='filename', type=str,
                    help='optional filename')

args = parser.parse_args()

base_url = args.url.rstrip("/") + "/"
filename = (args.filename or "video_file.ts").rstrip(".ts") + ".ts"

media = True
n = 0


def stream_complete():
    """
    End program when file is finished downloading.
    """
    print("Stream is complete!")
    print("Exiting now")
    raise SystemExit


# Remove any existing media file
with open(filename, "w") as f:
    print("Removed any existing file")

while media:
    print(f"Downloading file number {n}")
    url = f"{base_url}{n:05}.ts"

    with open(filename, "ab") as f:
        response = requests.get(url, stream=True)

        if response.status_code != 200:
            stream_complete()

        try:
            for block in response.iter_content(1024):
                if not block:
                    break

                f.write(block)

            n += 1
        except requests.exceptions.StreamConsumedError as e:
            stream_complete()
