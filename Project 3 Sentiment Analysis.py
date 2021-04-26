# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:50:40 2021

@author: 19145
"""

import csv

filename = 'simpsons_script.csv'
allRows = []
scriptDict = {}
try:
    with open(filename, 'r') as myCSV:
        data = csv.reader(myCSV)
        for row in data:
            allRows.append(row)
    myCSV.close()
except FileNotFoundError:
    print('no file!')
for line in allRows:
    episodeId = line[0]
    scriptSentence = line[2]
    if episodeId not in scriptDict:
        scriptDict[episodeId] = scriptSentence
    else:
        scriptDict[episodeId] = scriptDict.get(episodeId) + " " + scriptSentence
with open('sentAnaSimpsons.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['episodeId,']+['neg,']+['neu,']+["pos,"]+["compound"])
    for key in scriptDict:
        print(key)
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        line = scriptDict[key]   
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(line) # ss is a dictionary type
        spamwriter.writerow([key+',']+[str(ss['neg'])+',']+[str(ss['neu'])+',']+[str(ss['pos'])+',']+[str(ss['compound'])+','])
csvfile.close()