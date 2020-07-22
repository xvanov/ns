
'''
curl command to get all raw scores for natio
 curl "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score” -A "UserAgent Example"
'''

import requests


def get_nation_stats(url=str, headers=dict):
    response = requests.get(url, headers=headers)
    # TODO: parse stats and create dictionary
    if response:
        return response.text
    else:
        return f'Response status code: {response.status_code}'

def get_nation_issues(url=str, headers=dict):
     response = requests.get(url, headers=headers)
     # TODO: parse issues, return issue id
    if response:
        return response.text
    else:
        return f'Response status code: {response.status_code}'

if __name__ == '__main__':
    headers = {'User-Agent':'UserAgent Example', "X-Password": "koraxhun123"}
    urlStats = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score"
    urlIssues = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=issues"
    stats = get_nation_stats(urlIssues, headers)
    print(stats)
