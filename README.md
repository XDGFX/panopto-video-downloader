# Panopto Video Downloader
### Downloads videos from Panopto as a .ts stream.

## Prerequisites
- Python 3
- `requests` module ([pip](https://pypi.org/project/requests/))

## How to use:
1. Go to the video specified in your web browser, e.g. https://uniofbath.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cf3a64a1-936c-45b3-92de-72f8fecdb08b
2. Open the network tab in your developer console (Ctrl + Shift + E)
3. Refresh the page, select the 'media' filter, and play the video.
4. Look for files e.g. 00000.ts, 00001.ts. Double click on one.
5. Copy the url you are taken to, and remove the trailing '#####.ts'
6. Replace that url in base_url below.
7. Run `download_video.py`!