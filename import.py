import pymysql

db = pymysql.connect(
    host = "ix.cs.uoregon.edu",
    database = "EuroSoc",
    user = "omcevoy",
    passwd = "lion",
    port = 3037
)

mycursor = db.cursor()
sql = "INSERT INTO player(name, position, age, weekly_wage, club_name, country_of_birth) VALUES (%s, %s, %s, %s, %s, %s)"
with open("mscPData.csv") as data:
    for row in data:
        pData = []
        pData = row.split(",")
        values = (pData[0], pData[1], pData[2], pData[3], pData[4], pData[5].rstrip())
        mycursor.execute(sql, values)

db.commit()
print(mycursor.rowcount, "records inserted")
mycursor.close()
db.close()
