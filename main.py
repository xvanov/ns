# external dependencies
import os

# local dependencies
import nstools
import getpass
import dirtools
import issue_results_api
# main class
class MainPipeline():

    def __init__(self, dirs, nsClass, ipa):
        self.nsClass = nsClass
        self.dirs = dirs
        self.issues = []
        self.issuesPredictions = {}
        self.issuePredictionAPI = ipa

    def run(self):
        self.get_issues()
        self.get_issues_predictions()

    def get_issues(self):
        # urlIssues = self.nsClass.generate_issues_url()
        issuesList = self.nsClass.get_nation_issues(dirs.issuesDir) #, urlIssues)
        self.issues = issuesList

    def get_issues_predictions(self):
        for issue in self.issues:
            ipa.get_predictions(issue)
            predictionsList = ipa.process_predictions()
            print(predictionsList)
            # TODO: weather and non-mean parameters

    def get_stats(self):
        pass
        # TODO: get stats and compare to predictions raw numbers to see percent change


# run
if __name__ == '__main__':
    nationName = 'north_kalandia'
    baseDir = os.getcwd()
    password = getpass.getpass(prompt='Enter your password: ')
    headers = {'User-Agent':'Nation Info Getter', "X-Password": password}         
    dirs = dirtools.Dirs(baseDir, nationName)
    nsClass = nstools.NationStatesAPI(dirs, headers)
    ipa = issue_results_api.IssuePredictionAPI(dirs)

    mp = MainPipeline(dirs, nsClass, ipa)
    mp.run()
