import requests
from bs4 import BeautifulSoup


nyTimes = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(nyTimes.text, 'html.parser')

for story_heading in soup.find_all('h2'):
    print(story_heading.text)
