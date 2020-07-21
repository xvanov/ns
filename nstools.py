
'''
curl command to get all raw scores for natio
 curl "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score” -A "UserAgent Example"
'''

import requests


def get_nation_stats(url=str, headers=dict):
    response = requests.get(url, headers=headers)
    if response:
        return response.text
    else:
        return f'Response status code: {response.status_code}'

if __name__ == '__main__':
    headers = {'User-Agent':'UserAgent Example'}
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score"
    stats = get_nation_stats(url, headers)
    print(stats)
