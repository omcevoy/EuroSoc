import requests
from bs4 import BeautifulSoup
import unicodecsv as csv

url = "https://www.spotrac.com/epl/afc-bournemouth/payroll/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

data = [["Player", "Position", "Age", "Annual Salary", "Weekly Salary"]]
rows = soup.find_all('tr')

for tr in soup.find_all('tr'): #goes through tr elements
    rowData = []
    tdC = 0 #this will get rid of name duplicate
    for td in tr.find_all('td'):
        col = td.text.strip()
        if (tdC == 0):
            newCol = col.split('\n')
            try:
                rowData.append(newCol[1])
            except:
                continue
        else:
            rowData.append(col) #appends data to column
        tdC +=1
    data.append(rowData)

with open("output.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)


