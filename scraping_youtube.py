from requests_html import HTMLSession
import pandas as pd
import time



base_url = "https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg"
s = HTMLSession()
r = s.get(base_url)
r.html.render( sleep=1, keep_page=True, scrolldown=1)

videos = r.html.find('#video-title')

for item in videos:
    video={ "title": item.text,
            "link": item.absolute_links}
    print(video)        
