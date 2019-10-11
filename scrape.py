import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.premierleague.com/stats/top/players/goals")

src = result.content

soup = BeautifulSoup(src)

players = soup.find("tbody", class_= "statsTableContainer")
leaderboard = str(players)
leaderboard = leaderboard.split("</td>")
for piece in leaderboard:			#removes irrelevant lines
	if "playerName" not in piece:
		del(piece)
	else:
		piece = piece.split(">")
		for part in piece:
			if "</strong" not in part:
				del(part)
			else:
				part = part.replace("</strong", "")
				print part
