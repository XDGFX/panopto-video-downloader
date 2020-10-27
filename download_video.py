"""
Panopto Video Downloader v1
Downloads videos from Panopto as a .ts stream.

How to use:
1. Go to the video specified in your web browser, e.g. https://uniofbath.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cf3a64a1-936c-45b3-92de-72f8fecdb08b
2. Open the network tab in your developer console (Ctrl + Shift + E)
3. Refresh the page, select the 'media' filter, and play the video.
4. Look for files e.g. 00000.ts, 00001.ts. Double click on one.
5. Copy the url you are taken to, and remove the trailing '#####.ts'
6. Replace that url in base_url below.
7. Run this file!

XDGFX
"""

import requests
import os

number_files = 3
base_url = "https://d2hpwsdp0ihr0w.cloudfront.net/sessions/4029695e-a2d4-4157-9ecc-95bdbafd37a7/192e2a31-4b88-424a-8880372e253-65e6-4a69-8414-586e192067ce.hls/186542/"

for n in range(0, number_files + 1):
    print(f"Downloading file number {n}")
    url = f"{base_url}{n:05}.ts"

    with open("video_file.ts", "ab") as f:
        response = requests.get(url, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break

            f.write(block)