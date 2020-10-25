# external dependencies
import requests 
import os
import re 

# local dependencies
import dirtools

# main class
class IssuePredictionAPI():
    def __init__(self, dirs):
        self.dirs = dirs

    def get_predictions(self, issueNumber):
        self.predictionFile = os.path.join(self.dirs.issuesDir, f'raw_predictions_{issueNumber}')
        if os.path.exists(self.predictionFile):
            pass
        else:
            url = f'''http://www.mwq.dds.nl/ns/results/{issueNumber}.html'''
            response = requests.get(url)
            if response:
                predictionsRaw = response.text
                with open(self.predictionFile, 'w') as f:
                    print(predictionsRaw, file=f)
            else:
                return f'Response status code: {response.status_code}'
        return self.predictionFile

    def process_predictions(self):
        with open(self.predictionFile, 'r') as f:
            raw = f.read()
        splitted = raw.split('<tr><td>')
        splitted = splitted[1:] # get rid of first part (meta info)
        predictionsList = []
        for option in splitted:
            optionDict = {}
            newlineSplit = option.split('\n')
            for line in newlineSplit:
                if '</td>' == line[-5:] and len(line) > 5:
                    optionDict['result summary'] = line
                if 'mean' in line:
                    minimum = float(re.findall('[^A-Za-z]* to', line)[0][1:-3])
                    maximum = float(re.findall('to [^A-Za-z]*', line)[0][3:-1])
                    mean = float(re.findall('(mean.*)', line)[0][5:-7])
                    meanparam = re.findall('\d[^\d]*\(',line)[0][2:-2]
                    optionDict[meanparam] = [minimum, maximum, mean]
            predictionsList.append(optionDict)
            
        return predictionsList
# run
if __name__ == '__main__':
    natioName = 'north_kalandia'
    baseDir = os.getcwd()
    dirs = dirtools.Dirs(baseDir, nationName)
    ipa = IssuePredictionAPI(dirs)
