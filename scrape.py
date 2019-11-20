import requests
from bs4 import BeautifulSoup
import unicodecsv as csv

url = "https://www.spotrac.com/epl/afc-bournemouth/payroll/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

data = [["Player", "Position", "Age", "Annual Salary", "Weekly Salary", "Club"]]
rows = soup.find_all('tr')

for tr in soup.find_all('tr'): #goes through tr elements
    rowData = []
    tdC = 0 #this will get rid of name duplicate
    for td in tr.find_all('td'):
        col = td.text.strip()
        if (tdC == 0):
            newCol = col.split('\n')
            try:
                if len(newCol[1]) > 0:
                    rowData.append(newCol[1])
            except:
                continue
        else:
            col.strip('"');
            if tdC < 3:
                rowData.append(col) #appends data to column
            if tdC > 3:
                col = col[1:].replace(",", "")
                try:
                    col = int(col)
                    rowData.append(int(col))
                except:
                    continue
        tdC +=1
    if len(rowData) > 0:
        if type(rowData[-1]) is int:
            rowData.append("BOU") 
            data.append(rowData)

with open("output.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)


