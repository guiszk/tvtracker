import requests
import datetime
from sendalert import sendalert
from bs4 import BeautifulSoup as bs

with open('series.txt', 'r') as f:
    l = f.readlines()

d = {}
def getnext(show):
    url = 'https://next-episode.net/' + show
    page = requests.get(url)
    if(page.status_code == 200):
        soup = bs(page.text, 'html.parser')
        nextid = soup.find('div', {'id': 'next_episode'})
        if(nextid):
            if not('Sorry, no info about' in nextid.text):
                for line in nextid.text.split('\n'):
                    line = line.strip()
                    if('Name:' in line):
                        name = line.split(':')[1]
                    elif('Date:' in line):
                        date = line.split(':')[1]
                    elif('Season:' in line):
                        season = int(line.split(':')[1])
                    elif('Episode:' in line):
                        episode = int(line.split(':')[1].split(',')[0])
                eid = "S%02d" % season + "E%02d" % episode
                return(show, name, date, eid)

log = open('log.txt', 'a+')

for line in l:
    line = line.strip()
    nextep = getnext(line)
    if(nextep):
        show, name, date, eid = nextep
        wr = ':'.join(nextep)
        log.seek(0)
        if not any(wr == line.rstrip('\r\n') for line in log):
            log.write(wr)
            log.write('\n')

now = datetime.datetime.now()
now = now.strftime('%a %b %d, %Y')

log.seek(0)
for line in log:
    date = line.strip().split(':')[-2]
    if(date == now):
        sendalert(show.replace('-', ' '), eid + ' ' + name)
log.close()
