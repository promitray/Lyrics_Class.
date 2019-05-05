import sys
import urllib2
import re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

url_general = "https://www.lyrics.com"

songs_html = urllib2.urlopen('https://www.lyrics.com/artist/Michael+Jackson/4576')

my_html = songs_html.read()
my_html_soup = BeautifulSoup(my_html, 'html.parser').prettify()

song_urls = re.findall("\"(/lyric/[^\"]+)\">", my_html_soup)

url = [url_general + a for a in song_urls]
index = 0

for url in url:
    index = index + 1
    song_1 = urllib2.urlopen(url)
    song_1_html = song_1.read()
    song_1_html_soup = BeautifulSoup(song_1_html, 'html.parser')
    #song_1_html_soup = song_1_html_soup.prettify()
    lyrics = song_1_html_soup.find("pre", class_="lyric-body").get_text()
    with open('MJ_{}.txt'.format(index), 'w') as output:
          output.write(lyrics)
    #with open('song_all_MJ.txt'.format(index), 'a') as output_new:
     #        output_new.write(lyrics)
     #        output_new.write('\n')
     #        output_new.write('\n')
