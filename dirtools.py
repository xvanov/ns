# external dependencies
import os
import datetime

class Dirs():
    def __init__(self, baseDir, nationName, currentDate=None):
        if not currentDate:
            currentDate = str(datetime.date.today())
        self.nationName = nationName
        self.baseDir = baseDir
        self.nationDir = os.path.join(baseDir, nationName)
        self.dateDir = os.path.join(self.nationDir, currentDate)
        self.statsDir = os.path.join(self.dateDir, 'stats')
        self.issuesDir = os.path.join(self.dateDir, 'issues')
        dirsToCreate = list(self.__dict__.values())
        for directory in dirsToCreate:
            if not os.path.isdir(directory):
                os.mkdir(directory)
                print('creating directory: ', directory)

# run
if __name__ == '__main__':
    baseDir = os.getcwd()
    nationName = 'north_kalandia'
    dirs = Dirs(baseDir, nationName)
    print(dir(dirs))

