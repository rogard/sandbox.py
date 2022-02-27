#! /usr/bin/python3
# https://stackoverflow.com/a/54076684/9243116
import requests as r
import re

# url = "EntervideoURLhere"
url = "https://video-mia3-1.xx.fbcdn.net/v/t42.1790-2/274847687_250458373959645_1027004098317227738_n.mp4?_nc_cat=104&amp;ccb=1-5&amp;_nc_sid=985c63&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&amp;_nc_ohc=276M9NvaXEMAX-XGG2y&amp;_nc_rml=0&amp;_nc_ht=video-mia3-1.xx&amp;oh=00_AT9W0lVSUrhtC_KwLna9kx3tf7ik4hJtREzApPHM1UeK1A&amp;oe=621BF289"
html = r.get(url)
# for low Quality version
video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
print(video_url)

# for HD version
video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
print(video_url)

# https://stackoverflow.com/a/46813221/9243116
# https://m.facebook.com/groups/394380391741990/posts/698763561303670/
# https://video-mia3-1.xx.fbcdn.net/v/t42.1790-2/274847687_250458373959645_1027004098317227738_n.mp4?_nc_cat=104&amp;ccb=1-5&amp;_nc_sid=985c63&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&amp;_nc_ohc=276M9NvaXEMAX-XGG2y&amp;_nc_rml=0&amp;_nc_ht=video-mia3-1.xx&amp;oh=00_AT9W0lVSUrhtC_KwLna9kx3tf7ik4hJtREzApPHM1UeK1A&amp;oe=621BF289
