'''
curl command to get all raw scores for natio
 curl "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score” -A "UserAgent Example"
'''
# external dependencies
import requests
import os
import re

# local dependencies
import dirtools

# main class
# TODO: documentation

class NationStatesAPI():
    def __init__(self, dirs, headers):
        self.dirs = dirs
        self.nationName = dirs.nationName
        self.headers = headers

    def get_nation_stats(self, url=str, headers=None):
        response = requests.get(url, headers=headers)
        if response:
            statsPage = response.text
            nationStatsDict = self.parse_nation_stats(statsPage)
            return nationStatsDict
        else:
            return f'Response status code: {response.status_code}'

    def get_nation_issues(self, issuesPath, url=None, headers=None):
        issuesFile = os.path.join(issuesPath, 'raw_issues')
        if headers == None:
            headers = self.headers
        if url:
            response = requests.get(url, headers=headers)
            if response:
                issuesRawPage = response.text
                with open(issuesFile, 'w') as f:
                    print(issuesRawPage, file=f)
            else:
                return f'Response status code: {response.status_code}'

        issuesDict = self.parse_nation_issues(issuesFile)
        return issuesDict

    def parse_nation_issues(self, issuesFile):
        with open(issuesFile, 'r') as f:
            rawIssues = f.read()
        issuesList = []
        breakupOnIssues = rawIssues.split('<ISSUE ')
        breakupOnIssues = breakupOnIssues[1:] # skip first entry with meta info
        for issue in breakupOnIssues:
            issueID = re.findall('id="[0-9]+', issue)
            issueID = issueID[0][4:]
            issuesList.append(issueID)
        return issuesList

    def parse_nation_stats(self, statsPage):
        print(statsPage)
        statsDict = {}
        return statsDict

    def generate_issues_url(self):
        urlIssues = f"https://www.nationstates.net/cgi-bin/api.cgi?nation={self.nationName}&q=issues"
        return urlIssues

    def generate_stats_url(self):
        pass
# run
if __name__ == '__main__':
    # TODO: create a safer way to input password
    nationName = 'north_kalandia'
    headers = {'User-Agent':'Nation Info Getter', "X-Password": "koraxhun123"}

    # TODO: the below urls should be created in functions in nstools.py
    urlStats = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score"
    # TODO: driver code function 

    baseDir = os.getcwd()
    dirs = dirtools.Dirs(baseDir, nationName)
    nationStatesClass = NationStatesAPI(dirs, headers)
    '''
    urlIssues = nationStatesClass.generate_issues_url()
    issuesList = nationStatesClass.get_nation_issues(dirs.issuesDir, urlIssues)
    print(issuesList)
    '''
    stats = nationStatesClass.get_nation_stats(url=urlStats, headers=headers)
    print(stats)
