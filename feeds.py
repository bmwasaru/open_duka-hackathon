import datetime
from datetime import datetime
import dateutil

import pytz
import requests
import PyRSS2Gen


key = 'f29cafe47a2bd540438d7bc4f34b0fe0'
search_term = ''

def get_data():
    request = requests.get('http://www.openduka.org/index.php/api/search?key={0}&term={1}'.format(key, search_term))
    data_request = request.json()
    for data in data_request:
        id = data['ID']
        title = data['Name']
    return data


def generate_feeds():
    data = get_data()
    rss = PyRSS2Gen.RSS2(
        title= 'Open Duka Feeds',
        description = 'The freely accessible database of information on Kenyan entities',
        link = 'http://www.openduka.org/index.php',
        lastBuildDate = datetime.now(),
        items = [
        PyRSS2Gen.RSSItem(
            # get a way to write the data
            )
        ])
    rss.write_xml(open("rss.xml", "w"))


if __name__ == '__main__':
    generate_feeds()
