
import requests
from bs4 import BeautifulSoup
import string 
import csv
import urllib
import decimal
import re
import numpy as np
import datetime
from datetime import datetime
from threading import Timer

NumberOfTeams = 30
Year = 2018
Time = 0

b = "https://www.numberfire.com/mlb/daily-fantasy/daily-baseball-projections/pitchers"
c = "https://www.numberfire.com/mlb/daily-fantasy/daily-baseball-projections/batters"

x = 40
y = 300

i = datetime.now()

year = "%s" %i.year
month = "%02d" %i.month
day = "%02d" %i.day
# Dates linked to Todays Pitchers


# b = NF pitcher url
# c = NF batter url
# x = number of pitchers limit // y = number of batters limit
# Time Value [0,3+] where [Reg Season, Spring Training, Playoffs, Recent Game Logs..]
# Year Value [1998,Current]
# NumberOfTeams Value [1,30]


csv_file = open('Basic_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'GamesStarted', 'Wins', 'Losses', 'WPCT', 'CG', 'SHO', 'QS', 'SV', 'IP', 'HitsAllowed', 'RunsAllowed', 'EarnedRuns', 'HRsAllowed', 'WalksAllowed', 'SOs', 'ERA'])

# Basic Pitching Data
Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING&group=1&sort=2&time=0&pos=0&qual=0&sortOrder=0&splitType=0&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING&group=1&sort=2&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=0&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		GamesStarted = str(a.find_all("td")).split("<span>")[3]
		if GamesStarted == '[]':
			continue
		else:
			GamesStarted = str(a.find_all("td")).split("<span>")[3]
			GamesStarted = GamesStarted.split('Column">')[2]
			GamesStarted = GamesStarted.split("</td>,")[0]
		Wins = str(a.find_all("td")).split("<span>")[3]
		if Wins == '[]':
			continue
		else:
			Wins = str(a.find_all("td")).split("<span>")[3]
			Wins = Wins.split('Column">')[3]
			Wins = Wins.split("</td>,")[0]
		Losses = str(a.find_all("td")).split("<span>")[3]
		if Losses == '[]':
			continue
		else:
			Losses = str(a.find_all("td")).split("<span>")[3]
			Losses = Losses.split('Column">')[4]
			Losses = Losses.split("</td>,")[0]
		WPCT = str(a.find_all("td")).split("<td>")[0]
		if WPCT == '[]':
			continue
		else:
			WPCT = str(a.find_all("td")).split("<td>")[1]
			WPCT = re.sub("</td>,","",WPCT)
		CG = str(a.find_all("td")).split("<span>")[3]
		if CG == '[]':
			continue
		else:
			CG = str(a.find_all("td")).split("<span>")[3]
			CG = CG.split("<td>")[2]
			CG = re.sub("</td>","",CG).split(",")[0]
		SHO = str(a.find_all("td")).split("<span>")[3]
		if SHO == '[]':
			continue
		else:
			SHO = str(a.find_all("td")).split("<span>")[3]
			SHO = SHO.split("<td>")[3]
			SHO = re.sub("</td>","",SHO).split(",")[0]
		QS = str(a.find_all("td")).split("<span>")[3]
		if QS == '[]':
			continue
		else:
			QS = str(a.find_all("td")).split("<span>")[3]
			QS = QS.split("<td>")[4]
			QS = re.sub("</td>","",QS).split(",")[0]	
		SV = str(a.find_all("td")).split("<span>")[3]
		if SV == '[]':
			continue
		else:
			SV = str(a.find_all("td")).split("<span>")[3]
			SV = SV.split("<td>")[5]
			SV = re.sub("</td>","",SV).split(",")[0]
		IP = str(a.find_all("td")).split("<span>")[3]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<span>")[3]
			IP = IP.split("<td>")[6]
			IP = re.sub("</td>","",IP).split(",")[0]
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[7]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		RunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if RunsAllowed == '[]':
			continue
		else:
			RunsAllowed = str(a.find_all("td")).split("<span>")[3]
			RunsAllowed = RunsAllowed.split("<td>")[8]
			RunsAllowed = re.sub("</td>","",RunsAllowed).split(",")[0]			
		EarnedRuns = str(a.find_all("td")).split("<span>")[3]
		if EarnedRuns == '[]':
			continue
		else:
			EarnedRuns = str(a.find_all("td")).split("<span>")[3]
			EarnedRuns = EarnedRuns.split("<td>")[9]
			EarnedRuns = re.sub("</td>","",EarnedRuns).split(",")[0]	
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split("<td>")[10]
			HRsAllowed = re.sub("</td>","",HRsAllowed).split(",")[0]
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[11]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[12]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split("<td>")[13]
			ERA = re.sub("</td>]","",ERA).split(",")[0]
		print Names, Pos, GamesPitched, GamesStarted, Wins, Losses, WPCT, CG, SHO, QS, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA
		csv_writer.writerow([Names, Pos, GamesPitched, GamesStarted, Wins, Losses, WPCT, CG, SHO, QS, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA])
csv_file.close()

print  

# Home Basic Pitching Data 	

csv_file = open('Home_Basic_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'GamesStarted', 'Wins', 'Losses', 'CG', 'SHO', 'SV', 'IP', 'HitsAllowed', 'RunsAllowed', 'EarnedRuns', 'HRsAllowed', 'WalksAllowed', 'SOs', 'ERA'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING&group=1&sort=2&time=0&pos=0&qual=0&sortOrder=0&splitType=33&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING&group=1&sort=2&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=33&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		GamesStarted = str(a.find_all("td")).split("<span>")[3]
		if GamesStarted == '[]':
			continue
		else:
			GamesStarted = str(a.find_all("td")).split("<span>")[3]
			GamesStarted = GamesStarted.split('Column">')[2]
			GamesStarted = GamesStarted.split("</td>,")[0]
		Wins = str(a.find_all("td")).split("<span>")[3]
		if Wins == '[]':
			continue
		else:
			Wins = str(a.find_all("td")).split("<span>")[3]
			Wins = Wins.split('Column">')[3]
			Wins = Wins.split("</td>,")[0]
		Losses = str(a.find_all("td")).split("<span>")[3]
		if Losses == '[]':
			continue
		else:
			Losses = str(a.find_all("td")).split("<span>")[3]
			Losses = Losses.split('Column">')[4]
			Losses = Losses.split("</td>,")[0]
		CG = str(a.find_all("td")).split("<td>")[0]
		if CG == '[]':
			continue
		else:
			CG = str(a.find_all("td")).split("<td>")[1]
			CG = re.sub("</td>,","",CG)
		SHO = str(a.find_all("td")).split("<span>")[3]
		if SHO == '[]':
			continue
		else:
			SHO = str(a.find_all("td")).split("<span>")[3]
			SHO = SHO.split("<td>")[2]
			SHO = re.sub("</td>","",SHO).split(",")[0]
		SV = str(a.find_all("td")).split("<span>")[3]
		if SV == '[]':
			continue
		else:
			SV = str(a.find_all("td")).split("<span>")[3]
			SV = SV.split("<td>")[3]
			SV = re.sub("</td>","",SV).split(",")[0]
		IP = str(a.find_all("td")).split("<span>")[3]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<span>")[3]
			IP = IP.split("<td>")[4]
			IP = re.sub("</td>","",IP).split(",")[0]	
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[5]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		RunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if RunsAllowed == '[]':
			continue
		else:
			RunsAllowed = str(a.find_all("td")).split("<span>")[3]
			RunsAllowed = RunsAllowed.split("<td>")[6]
			RunsAllowed = re.sub("</td>","",RunsAllowed).split(",")[0]
		EarnedRuns = str(a.find_all("td")).split("<span>")[3]
		if EarnedRuns == '[]':
			continue
		else:
			EarnedRuns = str(a.find_all("td")).split("<span>")[3]
			EarnedRuns = EarnedRuns.split("<td>")[7]
			EarnedRuns = re.sub("</td>","",EarnedRuns).split(",")[0]
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split("<td>")[8]
			HRsAllowed = re.sub("</td>","",HRsAllowed).split(",")[0]			
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[9]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]	
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[10]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split("<td>")[11]
			ERA = re.sub("</td>]","",ERA).split(",")[0].split("</td>")[0]
		print Names, Pos, GamesPitched, GamesStarted, Wins, Losses, CG, SHO, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA
		csv_writer.writerow([Names, Pos, GamesPitched, GamesStarted, Wins, Losses, CG, SHO, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA])
csv_file.close()

print

# Away Basic Pitching Data 	

csv_file = open('Away_Basic_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'GamesStarted', 'Wins', 'Losses', 'CG', 'SHO', 'SV', 'IP', 'HitsAllowed', 'RunsAllowed', 'EarnedRuns', 'HRsAllowed', 'WalksAllowed', 'SOs', 'ERA'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING&group=1&sort=2&time=0&pos=0&qual=0&sortOrder=0&splitType=34&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING&group=1&sort=2&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=34&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		GamesStarted = str(a.find_all("td")).split("<span>")[3]
		if GamesStarted == '[]':
			continue
		else:
			GamesStarted = str(a.find_all("td")).split("<span>")[3]
			GamesStarted = GamesStarted.split('Column">')[2]
			GamesStarted = GamesStarted.split("</td>,")[0]
		Wins = str(a.find_all("td")).split("<span>")[3]
		if Wins == '[]':
			continue
		else:
			Wins = str(a.find_all("td")).split("<span>")[3]
			Wins = Wins.split('Column">')[3]
			Wins = Wins.split("</td>,")[0]
		Losses = str(a.find_all("td")).split("<span>")[3]
		if Losses == '[]':
			continue
		else:
			Losses = str(a.find_all("td")).split("<span>")[3]
			Losses = Losses.split('Column">')[4]
			Losses = Losses.split("</td>,")[0]
		CG = str(a.find_all("td")).split("<td>")[0]
		if CG == '[]':
			continue
		else:
			CG = str(a.find_all("td")).split("<td>")[1]
			CG = re.sub("</td>,","",CG)
		SHO = str(a.find_all("td")).split("<span>")[3]
		if SHO == '[]':
			continue
		else:
			SHO = str(a.find_all("td")).split("<span>")[3]
			SHO = SHO.split("<td>")[2]
			SHO = re.sub("</td>","",SHO).split(",")[0]
		SV = str(a.find_all("td")).split("<span>")[3]
		if SV == '[]':
			continue
		else:
			SV = str(a.find_all("td")).split("<span>")[3]
			SV = SV.split("<td>")[3]
			SV = re.sub("</td>","",SV).split(",")[0]
		IP = str(a.find_all("td")).split("<span>")[3]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<span>")[3]
			IP = IP.split("<td>")[4]
			IP = re.sub("</td>","",IP).split(",")[0]	
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[5]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		RunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if RunsAllowed == '[]':
			continue
		else:
			RunsAllowed = str(a.find_all("td")).split("<span>")[3]
			RunsAllowed = RunsAllowed.split("<td>")[6]
			RunsAllowed = re.sub("</td>","",RunsAllowed).split(",")[0]
		EarnedRuns = str(a.find_all("td")).split("<span>")[3]
		if EarnedRuns == '[]':
			continue
		else:
			EarnedRuns = str(a.find_all("td")).split("<span>")[3]
			EarnedRuns = EarnedRuns.split("<td>")[7]
			EarnedRuns = re.sub("</td>","",EarnedRuns).split(",")[0]
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split("<td>")[8]
			HRsAllowed = re.sub("</td>","",HRsAllowed).split(",")[0]			
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[9]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]	
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[10]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split("<td>")[11]
			ERA = re.sub("</td>]","",ERA).split(",")[0].split("</td>")[0]
		print Names, Pos, GamesPitched, GamesStarted, Wins, Losses, CG, SHO, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA		
		csv_writer.writerow([Names, Pos, GamesPitched, GamesStarted, Wins, Losses, CG, SHO, SV, IP, HitsAllowed, RunsAllowed, EarnedRuns, HRsAllowed, WalksAllowed, SOs, ERA])
csv_file.close()

print

# Advanced Pitching Data 	

csv_file = open('Advanced_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'IP', 'HitsAllowed', 'EarnedRunsAllowed', 'HRsAllowed', 'WalksAllowed', 'SOs', 'WHIP', 'HitsPerNine', 'WalksPerNine', 'BaseRunnersPerNine', 'HRsPerNine', 'SOsPerNine', 'SOsPerBBs', 'GBtoFBratio', 'HRsPerFlyBall', 'BABIP', 'ERC', 'ERA'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING+RATIOS&group=1&sort=7&time=0&pos=0&qual=0&sortOrder=0&splitType=0&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING+RATIOS&group=1&sort=7&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=0&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		IP = str(a.find_all("td")).split("<td>")[0]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<td>")[1]
			IP = re.sub("</td>,","",IP)
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[2]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if EarnedRunsAllowed == '[]':
			continue
		else:
			EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
			EarnedRunsAllowed = EarnedRunsAllowed.split("<td>")[3]
			EarnedRunsAllowed = re.sub("</td>","",EarnedRunsAllowed).split(",")[0]	
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split('Column">')[2]
			HRsAllowed = HRsAllowed.split("</td>,")[0]
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[4]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]		
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split('Column">')[3]
			SOs = SOs.split("</td>,")[0]
		WHIP = str(a.find_all("td")).split("<span>")[3]
		if WHIP == '[]':
			continue
		else:
			WHIP = str(a.find_all("td")).split("<span>")[3]
			WHIP = WHIP.split('Column">')[4]
			WHIP = WHIP.split("</td>,")[0]
		HitsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HitsPerNine == '[]':
			continue
		else:
			HitsPerNine = str(a.find_all("td")).split("<span>")[3]
			HitsPerNine = HitsPerNine.split("<td>")[5]
			HitsPerNine = re.sub("</td>","",HitsPerNine).split(",")[0]
		WalksPerNine = str(a.find_all("td")).split("<span>")[3]
		if WalksPerNine == '[]':
			continue
		else:
			WalksPerNine = str(a.find_all("td")).split("<span>")[3]
			WalksPerNine = WalksPerNine.split("<td>")[6]
			WalksPerNine = re.sub("</td>","",WalksPerNine).split(",")[0]
		BaseRunnersPerNine = str(a.find_all("td")).split("<span>")[3]
		if BaseRunnersPerNine == '[]':
			continue
		else:
			BaseRunnersPerNine = str(a.find_all("td")).split("<span>")[3]
			BaseRunnersPerNine = BaseRunnersPerNine.split("<td>")[7]
			BaseRunnersPerNine = re.sub("</td>","",BaseRunnersPerNine).split(",")[0]
		HRsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HRsPerNine == '[]':
			continue
		else:
			HRsPerNine = str(a.find_all("td")).split("<span>")[3]
			HRsPerNine = HRsPerNine.split("<td>")[8]
			HRsPerNine = re.sub("</td>","",HRsPerNine).split(",")[0]			
		SOsPerNine = str(a.find_all("td")).split("<span>")[3]
		if SOsPerNine == '[]':
			continue
		else:
			SOsPerNine = str(a.find_all("td")).split("<span>")[3]
			SOsPerNine = SOsPerNine.split("<td>")[9]
			SOsPerNine = re.sub("</td>","",SOsPerNine).split(",")[0]	
		SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
		if SOsPerBBs == '[]':
			continue
		else:
			SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
			SOsPerBBs = SOsPerBBs.split("<td>")[10]
			SOsPerBBs = re.sub("</td>","",SOsPerBBs).split(",")[0]
		GBtoFBratio = str(a.find_all("td")).split("<span>")[3]
		if GBtoFBratio == '[]':
			continue
		else:
			GBtoFBratio = str(a.find_all("td")).split("<span>")[3]
			GBtoFBratio = GBtoFBratio.split("<td>")[11]
			GBtoFBratio = re.sub("</td>","",GBtoFBratio).split(",")[0]
		HRsPerFlyBall = str(a.find_all("td")).split("<span>")[3]
		if HRsPerFlyBall == '[]':
			continue
		else:
			HRsPerFlyBall = str(a.find_all("td")).split("<span>")[3]
			HRsPerFlyBall = HRsPerFlyBall.split("<td>")[12]
			HRsPerFlyBall = re.sub("</td>","",HRsPerFlyBall).split(",")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[13]
			BABIP = re.sub("</td>","",BABIP).split(",")[0]
		ERC = str(a.find_all("td")).split("<span>")[3]
		if ERC == '[]':
			continue
		else:
			ERC = str(a.find_all("td")).split("<span>")[3]
			ERC = ERC.split("<td>")[14]
			ERC = re.sub("</td>","",ERC).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split("<td>")[15]
			ERA = re.sub("</td>]","",ERA).split(",")[0]
		print Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, BaseRunnersPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, GBtoFBratio, HRsPerFlyBall, BABIP, ERC, ERA
		csv_writer.writerow([Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, BaseRunnersPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, GBtoFBratio, HRsPerFlyBall, BABIP, ERC, ERA])
csv_file.close()

print 

# Home Advanced Pitching Data 	

csv_file = open('Home_Advanced_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'IP', 'HitsAllowed', 'EarnedRunsAllowed', 'HRsAllowed', 'WalksAllowed', 'SOs', 'WHIP', 'HitsPerNine', 'WalksPerNine', 'HRsPerNine', 'SOsPerNine', 'SOsPerBBs', 'BABIP', 'ERA'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING+RATIOS&group=1&sort=7&time=0&pos=0&qual=0&sortOrder=0&splitType=33&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING+RATIOS&group=1&sort=7&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=33&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)		
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		IP = str(a.find_all("td")).split("<td>")[0]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<td>")[1]
			IP = re.sub("</td>,","",IP)
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[2]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if EarnedRunsAllowed == '[]':
			continue
		else:
			EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
			EarnedRunsAllowed = EarnedRunsAllowed.split("<td>")[3]
			EarnedRunsAllowed = re.sub("</td>","",EarnedRunsAllowed).split(",")[0]	
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split("<td>")[4]
			HRsAllowed = re.sub("</td>","",HRsAllowed).split(",")[0]	
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[5]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]	
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[6]
			SOs = re.sub("</td>","",SOs).split(",")[0]							
		WHIP = str(a.find_all("td")).split("<span>")[3]
		if WHIP == '[]':
			continue
		else:
			WHIP = str(a.find_all("td")).split("<span>")[3]
			WHIP = WHIP.split('Column">')[2]
			WHIP = WHIP.split("</td>,")[0]		
		HitsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HitsPerNine == '[]':
			continue
		else:
			HitsPerNine = str(a.find_all("td")).split("<span>")[3]
			HitsPerNine = HitsPerNine.split('Column">')[3]
			HitsPerNine = HitsPerNine.split("</td>,")[0]
		WalksPerNine = str(a.find_all("td")).split("<span>")[3]
		if WalksPerNine == '[]':
			continue
		else:
			WalksPerNine = str(a.find_all("td")).split("<span>")[3]
			WalksPerNine = WalksPerNine.split("<td>")[7]
			WalksPerNine = re.sub("</td>","",WalksPerNine).split(",")[0]
		HRsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HRsPerNine == '[]':
			continue
		else:
			HRsPerNine = str(a.find_all("td")).split("<span>")[3]
			HRsPerNine = HRsPerNine.split("<td>")[8]
			HRsPerNine = re.sub("</td>","",HRsPerNine).split(",")[0]			
		SOsPerNine = str(a.find_all("td")).split("<span>")[3]
		if SOsPerNine == '[]':
			continue
		else:
			SOsPerNine = str(a.find_all("td")).split("<span>")[3]
			SOsPerNine = SOsPerNine.split("<td>")[9]
			SOsPerNine = re.sub("</td>","",SOsPerNine).split(",")[0]	
		SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
		if SOsPerBBs == '[]':
			continue
		else:
			SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
			SOsPerBBs = SOsPerBBs.split("<td>")[10]
			SOsPerBBs = re.sub("</td>","",SOsPerBBs).split(",")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[11]
			BABIP = re.sub("</td>","",BABIP).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split('Column">')[4]
			ERA = ERA.split("</td>]")[0]	
		print Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, BABIP, ERA
		csv_writer.writerow([Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, BABIP, ERA])
csv_file.close()

print

# Away Advanced Pitching Data 	

csv_file = open('Away_Advanced_Pitching_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'GamesPitched', 'IP', 'HitsAllowed', 'EarnedRunsAllowed', 'HRsAllowed', 'WalksAllowed', 'SOs', 'WHIP', 'HitsPerNine', 'WalksPerNine', 'HRsPerNine', 'SOsPerNine', 'SOsPerBBs', 'BABIP', 'ERA'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=PITCHING+RATIOS&group=1&sort=7&time=0&pos=0&qual=0&sortOrder=0&splitType=34&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=PITCHING+RATIOS&group=1&sort=7&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=34&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		GamesPitched = str(a.find_all("td")).split("<span>")[3]
		if GamesPitched == '[]':
			continue
		else:
			GamesPitched = str(a.find_all("td")).split("<span>")[3]
			GamesPitched = GamesPitched.split('Column">')[1]
			GamesPitched = GamesPitched.split("</td>,")[0]			
		IP = str(a.find_all("td")).split("<td>")[0]
		if IP == '[]':
			continue
		else:
			IP = str(a.find_all("td")).split("<td>")[1]
			IP = re.sub("</td>,","",IP)
		HitsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HitsAllowed == '[]':
			continue
		else:
			HitsAllowed = str(a.find_all("td")).split("<span>")[3]
			HitsAllowed = HitsAllowed.split("<td>")[2]
			HitsAllowed = re.sub("</td>","",HitsAllowed).split(",")[0]
		EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
		if EarnedRunsAllowed == '[]':
			continue
		else:
			EarnedRunsAllowed = str(a.find_all("td")).split("<span>")[3]
			EarnedRunsAllowed = EarnedRunsAllowed.split("<td>")[3]
			EarnedRunsAllowed = re.sub("</td>","",EarnedRunsAllowed).split(",")[0]	
		HRsAllowed = str(a.find_all("td")).split("<span>")[3]
		if HRsAllowed == '[]':
			continue
		else:
			HRsAllowed = str(a.find_all("td")).split("<span>")[3]
			HRsAllowed = HRsAllowed.split("<td>")[4]
			HRsAllowed = re.sub("</td>","",HRsAllowed).split(",")[0]	
		WalksAllowed = str(a.find_all("td")).split("<span>")[3]
		if WalksAllowed == '[]':
			continue
		else:
			WalksAllowed = str(a.find_all("td")).split("<span>")[3]
			WalksAllowed = WalksAllowed.split("<td>")[5]
			WalksAllowed = re.sub("</td>","",WalksAllowed).split(",")[0]	
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[6]
			SOs = re.sub("</td>","",SOs).split(",")[0]							
		WHIP = str(a.find_all("td")).split("<span>")[3]
		if WHIP == '[]':
			continue
		else:
			WHIP = str(a.find_all("td")).split("<span>")[3]
			WHIP = WHIP.split('Column">')[2]
			WHIP = WHIP.split("</td>,")[0]		
		HitsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HitsPerNine == '[]':
			continue
		else:
			HitsPerNine = str(a.find_all("td")).split("<span>")[3]
			HitsPerNine = HitsPerNine.split('Column">')[3]
			HitsPerNine = HitsPerNine.split("</td>,")[0]
		WalksPerNine = str(a.find_all("td")).split("<span>")[3]
		if WalksPerNine == '[]':
			continue
		else:
			WalksPerNine = str(a.find_all("td")).split("<span>")[3]
			WalksPerNine = WalksPerNine.split("<td>")[7]
			WalksPerNine = re.sub("</td>","",WalksPerNine).split(",")[0]
		HRsPerNine = str(a.find_all("td")).split("<span>")[3]
		if HRsPerNine == '[]':
			continue
		else:
			HRsPerNine = str(a.find_all("td")).split("<span>")[3]
			HRsPerNine = HRsPerNine.split("<td>")[8]
			HRsPerNine = re.sub("</td>","",HRsPerNine).split(",")[0]			
		SOsPerNine = str(a.find_all("td")).split("<span>")[3]
		if SOsPerNine == '[]':
			continue
		else:
			SOsPerNine = str(a.find_all("td")).split("<span>")[3]
			SOsPerNine = SOsPerNine.split("<td>")[9]
			SOsPerNine = re.sub("</td>","",SOsPerNine).split(",")[0]	
		SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
		if SOsPerBBs == '[]':
			continue
		else:
			SOsPerBBs = str(a.find_all("td")).split("<span>")[3]
			SOsPerBBs = SOsPerBBs.split("<td>")[10]
			SOsPerBBs = re.sub("</td>","",SOsPerBBs).split(",")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[11]
			BABIP = re.sub("</td>","",BABIP).split(",")[0]
		ERA = str(a.find_all("td")).split("<span>")[3]
		if ERA == '[]':
			continue
		else:
			ERA = str(a.find_all("td")).split("<span>")[3]
			ERA = ERA.split('Column">')[4]
			ERA = ERA.split("</td>]")[0]	
		print Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, BABIP, ERA
		csv_writer.writerow([Names, Pos, GamesPitched, IP, HitsAllowed, EarnedRunsAllowed, HRsAllowed, WalksAllowed, SOs, WHIP, HitsPerNine, WalksPerNine, HRsPerNine, SOsPerNine, SOsPerBBs, BABIP, ERA])
csv_file.close()

print

# Basic Hitting Data

csv_file = open('Basic_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'PA', 'AB', 'Runs', 'Hits', 'Doubles', 'Triples', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'AVG', 'OBP', 'SLG', 'OPS'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING&group=1&sort=13&time=0&pos=0&qual=0&splitType=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING&group=1&sort=13&time=" + "{}".format(Time) + "&pos=0&qual=0&splitType=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = re.sub("</td>,","",Games)
		PA = str(a.find_all("td")).split("<span>")[3]
		if PA == '[]':
			continue
		else:
			PA = str(a.find_all("td")).split("<span>")[3]
			PA = PA.split("<td>")[2]
			PA = re.sub("</td>","",PA).split(",")[0]
		AB = str(a.find_all("td")).split("<span>")[3]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<span>")[3]
			AB = AB.split("<td>")[2]
			AB = AB.split('Column">')[1]
			AB = re.sub("</td>,","",AB)
		Runs = str(a.find_all("td")).split("<span>")[3]
		if Runs == '[]':
			continue
		else:
			Runs = str(a.find_all("td")).split("<span>")[3]
			Runs = Runs.split("<td>")[3]
			Runs = re.sub("</td>","",Runs).split(",")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[4]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		Doubles = str(a.find_all("td")).split("<span>")[3]
		if Doubles == '[]':
			continue
		else:
			Doubles = str(a.find_all("td")).split("<span>")[3]
			Doubles = Doubles.split("<td>")[5]
			Doubles = re.sub("</td>","",Doubles).split(",")[0]
		Triples = str(a.find_all("td")).split("<span>")[3]
		if Triples == '[]':
			continue
		else:
			Triples = str(a.find_all("td")).split("<span>")[3]
			Triples = Triples.split("<td>")[6]
			Triples = re.sub("</td>","",Triples).split(",")[0]
		HR = str(a.find_all("td")).split("<span>")[3]
		if HR == '[]':
			continue
		else:
			HR = str(a.find_all("td")).split("<span>")[3]
			HR = HR.split("<td>")[6]
			HR = HR.split('Column">')[1].split("</td>,")[0]
		RBI = str(a.find_all("td")).split("<span>")[3]
		if RBI == '[]':
			continue
		else:
			RBI = str(a.find_all("td")).split("<span>")[3]
			RBI = RBI.split("<td>")[6]
			RBI = RBI.split('Column">')[2].split("</td>,")[0]
		SB = str(a.find_all("td")).split("<span>")[3]
		if SB == '[]':
			continue
		else:
			SB = str(a.find_all("td")).split("<span>")[3]
			SB = SB.split("<td>")[7]
			SB = SB.split('Column">')[0].split("</td>,")[0]			
		CS = str(a.find_all("td")).split("<span>")[3]
		if CS == '[]':
			continue
		else:
			CS = str(a.find_all("td")).split("<span>")[3]
			CS = CS.split("<td>")[8]
			CS = CS.split('Column">')[0].split("</td>,")[0]	
		BB = str(a.find_all("td")).split("<span>")[3]
		if BB == '[]':
			continue
		else:
			BB = str(a.find_all("td")).split("<span>")[3]
			BB = BB.split("<td>")[9]
			BB = BB.split('Column">')[0].split("</td>,")[0]	
		SO = str(a.find_all("td")).split("<span>")[3]
		if SO == '[]':
			continue
		else:
			SO = str(a.find_all("td")).split("<span>")[3]
			SO = SO.split("<td>")[10]
			SO = SO.split('Column">')[0].split("</td>,")[0]	
		AVG = str(a.find_all("td")).split("<span>")[3]
		if AVG == '[]':
			continue
		else:
			AVG = str(a.find_all("td")).split("<span>")[3]
			AVG = AVG.split("<td>")[10]
			AVG = AVG.split('Column">')[1].split("</td>,")[0]	
		OBP = str(a.find_all("td")).split("<span>")[3]
		if OBP == '[]':
			continue
		else:
			OBP = str(a.find_all("td")).split("<span>")[3]
			OBP = OBP.split("<td>")[11]
			OBP = OBP.split('Column">')[0].split("</td>,")[0]	
		SLG = str(a.find_all("td")).split("<span>")[3]
		if SLG == '[]':
			continue
		else:
			SLG = str(a.find_all("td")).split("<span>")[3]
			SLG = SLG.split("<td>")[12]
			SLG = SLG.split('Column">')[0].split("</td>,")[0]
		OPS = str(a.find_all("td")).split("<span>")[3]
		if OPS == '[]':
			continue
		else:
			OPS = str(a.find_all("td")).split("<span>")[3]
			OPS = OPS.split("<td>")[13]
			OPS = re.sub("</td>]","",OPS)
		print Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS
		csv_writer.writerow([Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS])
csv_file.close()

print

# Home Basic Hitting Data

csv_file = open('Home_Basic_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'PA', 'AB', 'Runs', 'Hits', 'Doubles', 'Triples', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'AVG', 'OBP', 'SLG', 'OPS'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING&group=1&sort=13&time=0&pos=0&qual=0&sortOrder=0&splitType=33&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING&group=1&sort=13&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=33&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = re.sub("</td>,","",Games)
		PA = str(a.find_all("td")).split("<span>")[3]
		if PA == '[]':
			continue
		else:
			PA = str(a.find_all("td")).split("<span>")[3]
			PA = PA.split("<td>")[2]
			PA = re.sub("</td>","",PA).split(",")[0]
		AB = str(a.find_all("td")).split("<span>")[3]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<span>")[3]
			AB = AB.split("<td>")[2]
			AB = AB.split('Column">')[1]
			AB = re.sub("</td>,","",AB)
		Runs = str(a.find_all("td")).split("<span>")[3]
		if Runs == '[]':
			continue
		else:
			Runs = str(a.find_all("td")).split("<span>")[3]
			Runs = Runs.split("<td>")[3]
			Runs = re.sub("</td>","",Runs).split(",")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[4]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		Doubles = str(a.find_all("td")).split("<span>")[3]
		if Doubles == '[]':
			continue
		else:
			Doubles = str(a.find_all("td")).split("<span>")[3]
			Doubles = Doubles.split("<td>")[5]
			Doubles = re.sub("</td>","",Doubles).split(",")[0]
		Triples = str(a.find_all("td")).split("<span>")[3]
		if Triples == '[]':
			continue
		else:
			Triples = str(a.find_all("td")).split("<span>")[3]
			Triples = Triples.split("<td>")[6]
			Triples = re.sub("</td>","",Triples).split(",")[0]
		HR = str(a.find_all("td")).split("<span>")[3]
		if HR == '[]':
			continue
		else:
			HR = str(a.find_all("td")).split("<span>")[3]
			HR = HR.split("<td>")[6]
			HR = HR.split('Column">')[1].split("</td>,")[0]
		RBI = str(a.find_all("td")).split("<span>")[3]
		if RBI == '[]':
			continue
		else:
			RBI = str(a.find_all("td")).split("<span>")[3]
			RBI = RBI.split("<td>")[6]
			RBI = RBI.split('Column">')[2].split("</td>,")[0]
		SB = str(a.find_all("td")).split("<span>")[3]
		if SB == '[]':
			continue
		else:
			SB = str(a.find_all("td")).split("<span>")[3]
			SB = SB.split("<td>")[7]
			SB = SB.split('Column">')[0].split("</td>,")[0]			
		CS = str(a.find_all("td")).split("<span>")[3]
		if CS == '[]':
			continue
		else:
			CS = str(a.find_all("td")).split("<span>")[3]
			CS = CS.split("<td>")[8]
			CS = CS.split('Column">')[0].split("</td>,")[0]	
		BB = str(a.find_all("td")).split("<span>")[3]
		if BB == '[]':
			continue
		else:
			BB = str(a.find_all("td")).split("<span>")[3]
			BB = BB.split("<td>")[9]
			BB = BB.split('Column">')[0].split("</td>,")[0]	
		SO = str(a.find_all("td")).split("<span>")[3]
		if SO == '[]':
			continue
		else:
			SO = str(a.find_all("td")).split("<span>")[3]
			SO = SO.split("<td>")[10]
			SO = SO.split('Column">')[0].split("</td>,")[0]	
		AVG = str(a.find_all("td")).split("<span>")[3]
		if AVG == '[]':
			continue
		else:
			AVG = str(a.find_all("td")).split("<span>")[3]
			AVG = AVG.split("<td>")[10]
			AVG = AVG.split('Column">')[1].split("</td>,")[0]	
		OBP = str(a.find_all("td")).split("<span>")[3]
		if OBP == '[]':
			continue
		else:
			OBP = str(a.find_all("td")).split("<span>")[3]
			OBP = OBP.split("<td>")[11]
			OBP = OBP.split('Column">')[0].split("</td>,")[0]	
		SLG = str(a.find_all("td")).split("<span>")[3]
		if SLG == '[]':
			continue
		else:
			SLG = str(a.find_all("td")).split("<span>")[3]
			SLG = SLG.split("<td>")[12]
			SLG = SLG.split('Column">')[0].split("</td>,")[0]
		OPS = str(a.find_all("td")).split("<span>")[3]
		if OPS == '[]':
			continue
		else:
			OPS = str(a.find_all("td")).split("<span>")[3]
			OPS = OPS.split("<td>")[13]
			OPS = re.sub("</td>]","",OPS)
		print Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS			
		csv_writer.writerow([Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS])
csv_file.close()

print

# Away Basic Hitting Data

csv_file = open('Away_Basic_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'PA', 'AB', 'Runs', 'Hits', 'Doubles', 'Triples', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'AVG', 'OBP', 'SLG', 'OPS'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING&group=1&sort=13&time=0&pos=0&qual=0&sortOrder=0&splitType=34&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING&group=1&sort=13&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=34&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = re.sub("</td>,","",Games)
		PA = str(a.find_all("td")).split("<span>")[3]
		if PA == '[]':
			continue
		else:
			PA = str(a.find_all("td")).split("<span>")[3]
			PA = PA.split("<td>")[2]
			PA = re.sub("</td>","",PA).split(",")[0]
		AB = str(a.find_all("td")).split("<span>")[3]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<span>")[3]
			AB = AB.split("<td>")[2]
			AB = AB.split('Column">')[1]
			AB = re.sub("</td>,","",AB)
		Runs = str(a.find_all("td")).split("<span>")[3]
		if Runs == '[]':
			continue
		else:
			Runs = str(a.find_all("td")).split("<span>")[3]
			Runs = Runs.split("<td>")[3]
			Runs = re.sub("</td>","",Runs).split(",")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[4]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		Doubles = str(a.find_all("td")).split("<span>")[3]
		if Doubles == '[]':
			continue
		else:
			Doubles = str(a.find_all("td")).split("<span>")[3]
			Doubles = Doubles.split("<td>")[5]
			Doubles = re.sub("</td>","",Doubles).split(",")[0]
		Triples = str(a.find_all("td")).split("<span>")[3]
		if Triples == '[]':
			continue
		else:
			Triples = str(a.find_all("td")).split("<span>")[3]
			Triples = Triples.split("<td>")[6]
			Triples = re.sub("</td>","",Triples).split(",")[0]
		HR = str(a.find_all("td")).split("<span>")[3]
		if HR == '[]':
			continue
		else:
			HR = str(a.find_all("td")).split("<span>")[3]
			HR = HR.split("<td>")[6]
			HR = HR.split('Column">')[1].split("</td>,")[0]
		RBI = str(a.find_all("td")).split("<span>")[3]
		if RBI == '[]':
			continue
		else:
			RBI = str(a.find_all("td")).split("<span>")[3]
			RBI = RBI.split("<td>")[6]
			RBI = RBI.split('Column">')[2].split("</td>,")[0]
		SB = str(a.find_all("td")).split("<span>")[3]
		if SB == '[]':
			continue
		else:
			SB = str(a.find_all("td")).split("<span>")[3]
			SB = SB.split("<td>")[7]
			SB = SB.split('Column">')[0].split("</td>,")[0]			
		CS = str(a.find_all("td")).split("<span>")[3]
		if CS == '[]':
			continue
		else:
			CS = str(a.find_all("td")).split("<span>")[3]
			CS = CS.split("<td>")[8]
			CS = CS.split('Column">')[0].split("</td>,")[0]	
		BB = str(a.find_all("td")).split("<span>")[3]
		if BB == '[]':
			continue
		else:
			BB = str(a.find_all("td")).split("<span>")[3]
			BB = BB.split("<td>")[9]
			BB = BB.split('Column">')[0].split("</td>,")[0]	
		SO = str(a.find_all("td")).split("<span>")[3]
		if SO == '[]':
			continue
		else:
			SO = str(a.find_all("td")).split("<span>")[3]
			SO = SO.split("<td>")[10]
			SO = SO.split('Column">')[0].split("</td>,")[0]	
		AVG = str(a.find_all("td")).split("<span>")[3]
		if AVG == '[]':
			continue
		else:
			AVG = str(a.find_all("td")).split("<span>")[3]
			AVG = AVG.split("<td>")[10]
			AVG = AVG.split('Column">')[1].split("</td>,")[0]	
		OBP = str(a.find_all("td")).split("<span>")[3]
		if OBP == '[]':
			continue
		else:
			OBP = str(a.find_all("td")).split("<span>")[3]
			OBP = OBP.split("<td>")[11]
			OBP = OBP.split('Column">')[0].split("</td>,")[0]	
		SLG = str(a.find_all("td")).split("<span>")[3]
		if SLG == '[]':
			continue
		else:
			SLG = str(a.find_all("td")).split("<span>")[3]
			SLG = SLG.split("<td>")[12]
			SLG = SLG.split('Column">')[0].split("</td>,")[0]
		OPS = str(a.find_all("td")).split("<span>")[3]
		if OPS == '[]':
			continue
		else:
			OPS = str(a.find_all("td")).split("<span>")[3]
			OPS = OPS.split("<td>")[13]
			OPS = re.sub("</td>]","",OPS)
		print Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS	
		csv_writer.writerow([Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS])
csv_file.close()

print

# Lefty Basic Hitting Data

csv_file = open('vsLefties_Basic_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'PA', 'AB', 'Runs', 'Hits', 'Doubles', 'Triples', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'AVG', 'OBP', 'SLG', 'OPS'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING&group=1&sort=13&time=0&pos=0&qual=0&sortOrder=0&splitType=31&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING&group=1&sort=13&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=31&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = re.sub("</td>,","",Games)
		PA = str(a.find_all("td")).split("<span>")[3]
		if PA == '[]':
			continue
		else:
			PA = str(a.find_all("td")).split("<span>")[3]
			PA = PA.split("<td>")[2]
			PA = re.sub("</td>","",PA).split(",")[0]
		AB = str(a.find_all("td")).split("<span>")[3]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<span>")[3]
			AB = AB.split("<td>")[2]
			AB = AB.split('Column">')[1]
			AB = re.sub("</td>,","",AB)
		Runs = str(a.find_all("td")).split("<span>")[3]
		if Runs == '[]':
			continue
		else:
			Runs = str(a.find_all("td")).split("<span>")[3]
			Runs = Runs.split("<td>")[3]
			Runs = re.sub("</td>","",Runs).split(",")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[4]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		Doubles = str(a.find_all("td")).split("<span>")[3]
		if Doubles == '[]':
			continue
		else:
			Doubles = str(a.find_all("td")).split("<span>")[3]
			Doubles = Doubles.split("<td>")[5]
			Doubles = re.sub("</td>","",Doubles).split(",")[0]
		Triples = str(a.find_all("td")).split("<span>")[3]
		if Triples == '[]':
			continue
		else:
			Triples = str(a.find_all("td")).split("<span>")[3]
			Triples = Triples.split("<td>")[6]
			Triples = re.sub("</td>","",Triples).split(",")[0]
		HR = str(a.find_all("td")).split("<span>")[3]
		if HR == '[]':
			continue
		else:
			HR = str(a.find_all("td")).split("<span>")[3]
			HR = HR.split("<td>")[6]
			HR = HR.split('Column">')[1].split("</td>,")[0]
		RBI = str(a.find_all("td")).split("<span>")[3]
		if RBI == '[]':
			continue
		else:
			RBI = str(a.find_all("td")).split("<span>")[3]
			RBI = RBI.split("<td>")[6]
			RBI = RBI.split('Column">')[2].split("</td>,")[0]
		SB = str(a.find_all("td")).split("<span>")[3]
		if SB == '[]':
			continue
		else:
			SB = str(a.find_all("td")).split("<span>")[3]
			SB = SB.split("<td>")[7]
			SB = SB.split('Column">')[0].split("</td>,")[0]			
		CS = str(a.find_all("td")).split("<span>")[3]
		if CS == '[]':
			continue
		else:
			CS = str(a.find_all("td")).split("<span>")[3]
			CS = CS.split("<td>")[8]
			CS = CS.split('Column">')[0].split("</td>,")[0]	
		BB = str(a.find_all("td")).split("<span>")[3]
		if BB == '[]':
			continue
		else:
			BB = str(a.find_all("td")).split("<span>")[3]
			BB = BB.split("<td>")[9]
			BB = BB.split('Column">')[0].split("</td>,")[0]	
		SO = str(a.find_all("td")).split("<span>")[3]
		if SO == '[]':
			continue
		else:
			SO = str(a.find_all("td")).split("<span>")[3]
			SO = SO.split("<td>")[10]
			SO = SO.split('Column">')[0].split("</td>,")[0]	
		AVG = str(a.find_all("td")).split("<span>")[3]
		if AVG == '[]':
			continue
		else:
			AVG = str(a.find_all("td")).split("<span>")[3]
			AVG = AVG.split("<td>")[10]
			AVG = AVG.split('Column">')[1].split("</td>,")[0]	
		OBP = str(a.find_all("td")).split("<span>")[3]
		if OBP == '[]':
			continue
		else:
			OBP = str(a.find_all("td")).split("<span>")[3]
			OBP = OBP.split("<td>")[11]
			OBP = OBP.split('Column">')[0].split("</td>,")[0]	
		SLG = str(a.find_all("td")).split("<span>")[3]
		if SLG == '[]':
			continue
		else:
			SLG = str(a.find_all("td")).split("<span>")[3]
			SLG = SLG.split("<td>")[12]
			SLG = SLG.split('Column">')[0].split("</td>,")[0]
		OPS = str(a.find_all("td")).split("<span>")[3]
		if OPS == '[]':
			continue
		else:
			OPS = str(a.find_all("td")).split("<span>")[3]
			OPS = OPS.split("<td>")[13]
			OPS = re.sub("</td>]","",OPS)
		print Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS	
		csv_writer.writerow([Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS])
csv_file.close()

print

# Righty Basic Hitting Data

csv_file = open('vsRighties_Basic_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'PA', 'AB', 'Runs', 'Hits', 'Doubles', 'Triples', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'AVG', 'OBP', 'SLG', 'OPS'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING&group=1&sort=13&time=0&pos=0&qual=0&sortOrder=0&splitType=32&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING&group=1&sort=13&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=32&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = re.sub("</td>,","",Games)
		PA = str(a.find_all("td")).split("<span>")[3]
		if PA == '[]':
			continue
		else:
			PA = str(a.find_all("td")).split("<span>")[3]
			PA = PA.split("<td>")[2]
			PA = re.sub("</td>","",PA).split(",")[0]
		AB = str(a.find_all("td")).split("<span>")[3]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<span>")[3]
			AB = AB.split("<td>")[2]
			AB = AB.split('Column">')[1]
			AB = re.sub("</td>,","",AB)
		Runs = str(a.find_all("td")).split("<span>")[3]
		if Runs == '[]':
			continue
		else:
			Runs = str(a.find_all("td")).split("<span>")[3]
			Runs = Runs.split("<td>")[3]
			Runs = re.sub("</td>","",Runs).split(",")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[4]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		Doubles = str(a.find_all("td")).split("<span>")[3]
		if Doubles == '[]':
			continue
		else:
			Doubles = str(a.find_all("td")).split("<span>")[3]
			Doubles = Doubles.split("<td>")[5]
			Doubles = re.sub("</td>","",Doubles).split(",")[0]
		Triples = str(a.find_all("td")).split("<span>")[3]
		if Triples == '[]':
			continue
		else:
			Triples = str(a.find_all("td")).split("<span>")[3]
			Triples = Triples.split("<td>")[6]
			Triples = re.sub("</td>","",Triples).split(",")[0]
		HR = str(a.find_all("td")).split("<span>")[3]
		if HR == '[]':
			continue
		else:
			HR = str(a.find_all("td")).split("<span>")[3]
			HR = HR.split("<td>")[6]
			HR = HR.split('Column">')[1].split("</td>,")[0]
		RBI = str(a.find_all("td")).split("<span>")[3]
		if RBI == '[]':
			continue
		else:
			RBI = str(a.find_all("td")).split("<span>")[3]
			RBI = RBI.split("<td>")[6]
			RBI = RBI.split('Column">')[2].split("</td>,")[0]
		SB = str(a.find_all("td")).split("<span>")[3]
		if SB == '[]':
			continue
		else:
			SB = str(a.find_all("td")).split("<span>")[3]
			SB = SB.split("<td>")[7]
			SB = SB.split('Column">')[0].split("</td>,")[0]			
		CS = str(a.find_all("td")).split("<span>")[3]
		if CS == '[]':
			continue
		else:
			CS = str(a.find_all("td")).split("<span>")[3]
			CS = CS.split("<td>")[8]
			CS = CS.split('Column">')[0].split("</td>,")[0]	
		BB = str(a.find_all("td")).split("<span>")[3]
		if BB == '[]':
			continue
		else:
			BB = str(a.find_all("td")).split("<span>")[3]
			BB = BB.split("<td>")[9]
			BB = BB.split('Column">')[0].split("</td>,")[0]	
		SO = str(a.find_all("td")).split("<span>")[3]
		if SO == '[]':
			continue
		else:
			SO = str(a.find_all("td")).split("<span>")[3]
			SO = SO.split("<td>")[10]
			SO = SO.split('Column">')[0].split("</td>,")[0]	
		AVG = str(a.find_all("td")).split("<span>")[3]
		if AVG == '[]':
			continue
		else:
			AVG = str(a.find_all("td")).split("<span>")[3]
			AVG = AVG.split("<td>")[10]
			AVG = AVG.split('Column">')[1].split("</td>,")[0]	
		OBP = str(a.find_all("td")).split("<span>")[3]
		if OBP == '[]':
			continue
		else:
			OBP = str(a.find_all("td")).split("<span>")[3]
			OBP = OBP.split("<td>")[11]
			OBP = OBP.split('Column">')[0].split("</td>,")[0]	
		SLG = str(a.find_all("td")).split("<span>")[3]
		if SLG == '[]':
			continue
		else:
			SLG = str(a.find_all("td")).split("<span>")[3]
			SLG = SLG.split("<td>")[12]
			SLG = SLG.split('Column">')[0].split("</td>,")[0]
		OPS = str(a.find_all("td")).split("<span>")[3]
		if OPS == '[]':
			continue
		else:
			OPS = str(a.find_all("td")).split("<span>")[3]
			OPS = OPS.split("<td>")[13]
			OPS = re.sub("</td>]","",OPS)
		print Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS	
		csv_writer.writerow([Names, Pos, Games, PA, AB, Runs, Hits, Doubles, Triples, HR, RBI, SB, CS, BB, SO, AVG, OBP, SLG, OPS])
csv_file.close()

print

# Hitting II Data

csv_file = open('Hitting_II_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'XBH', 'TotalBases', 'RunsCreated', 'RunsCreatedPer27', 'TotalPitches', 'PitchesPerPlateAppearance'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+II&group=1&sort=4&time=0&pos=0&qual=0&sortOrder=0&splitType=0&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+II&group=1&sort=4&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=0&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("</td>")[0]
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1]	
			AB = AB.split("<td")[0]
			AB = re.sub("</td>,","",AB)
		XBH = str(a.find_all("td")).split("<span>")[3]
		if XBH == '[]':
			continue
		else:
			XBH = str(a.find_all("td")).split("<td>")[1]
			XBH = XBH.split('Column">')[2]	
			XBH = XBH.split("<td")[0]
			XBH = re.sub("</td>,","",XBH)
		TotalBases = str(a.find_all("td")).split("<span>")[3]
		if TotalBases == '[]':
			continue
		else:
			TotalBases = str(a.find_all("td")).split("<td>")[2]	
			TotalBases = TotalBases.split("<td")[0]
			TotalBases = re.sub("</td>,","",TotalBases)
		RunsCreated = str(a.find_all("td")).split("<span>")[3]
		if RunsCreated == '[]':
			continue
		else:
			RunsCreated = str(a.find_all("td")).split("<span>")[3]
			RunsCreated = RunsCreated.split("<td>")[2]
			RunsCreated = RunsCreated.split('Column">')[1]
			RunsCreated = re.sub("</td>,","",RunsCreated)
		RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
		if RunsCreatedPer27 == '[]':
			continue
		else:
			RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
			RunsCreatedPer27 = RunsCreatedPer27.split("<td>")[3]
			RunsCreatedPer27 = re.sub("</td>","",RunsCreatedPer27).split(",")[0]
		TotalPitches = str(a.find_all("td")).split("<span>")[3]
		if TotalPitches == '[]':
			continue
		else:
			TotalPitches = str(a.find_all("td")).split("<span>")[3]
			TotalPitches = TotalPitches.split("<td>")[11]
			TotalPitches = TotalPitches.split('Column">')[0].split("</td>,")[0]	
		PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
		if PitchesPerPlateAppearance == '[]':
			continue
		else:
			PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split("<td>")[12]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split('Column">')[0].split("</td>]")[0]
		print Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance
		csv_writer.writerow([Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance])
csv_file.close()

print

# Righty Hitting II Data

csv_file = open('vsRighties_Hitting_II_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'XBH', 'TotalBases', 'RunsCreated', 'RunsCreatedPer27', 'TotalPitches', 'PitchesPerPlateAppearance'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+II&group=1&sort=4&time=0&pos=0&qual=0&sortOrder=0&splitType=32&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+II&group=1&sort=4&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=32&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("</td>")[0]
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1]	
			AB = AB.split("<td")[0]
			AB = re.sub("</td>,","",AB)
		XBH = str(a.find_all("td")).split("<span>")[3]
		if XBH == '[]':
			continue
		else:
			XBH = str(a.find_all("td")).split("<td>")[1]
			XBH = XBH.split('Column">')[2]	
			XBH = XBH.split("<td")[0]
			XBH = re.sub("</td>,","",XBH)
		TotalBases = str(a.find_all("td")).split("<span>")[3]
		if TotalBases == '[]':
			continue
		else:
			TotalBases = str(a.find_all("td")).split("<td>")[2]	
			TotalBases = TotalBases.split("<td")[0]
			TotalBases = re.sub("</td>,","",TotalBases)
		RunsCreated = str(a.find_all("td")).split("<span>")[3]
		if RunsCreated == '[]':
			continue
		else:
			RunsCreated = str(a.find_all("td")).split("<span>")[3]
			RunsCreated = RunsCreated.split("<td>")[2]
			RunsCreated = RunsCreated.split('Column">')[1]
			RunsCreated = re.sub("</td>,","",RunsCreated)
		RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
		if RunsCreatedPer27 == '[]':
			continue
		else:
			RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
			RunsCreatedPer27 = RunsCreatedPer27.split("<td>")[3]
			RunsCreatedPer27 = re.sub("</td>","",RunsCreatedPer27).split(",")[0]
		TotalPitches = str(a.find_all("td")).split("<span>")[3]
		if TotalPitches == '[]':
			continue
		else:
			TotalPitches = str(a.find_all("td")).split("<span>")[3]
			TotalPitches = TotalPitches.split("<td>")[8]
			TotalPitches = TotalPitches.split('Column">')[0].split("</td>,")[0]	
		PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
		if PitchesPerPlateAppearance == '[]':
			continue
		else:
			PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split("<td>")[9]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split('Column">')[0].split("</td>]")[0]
		print Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance
		csv_writer.writerow([Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance])
csv_file.close()

print

# Lefty Hitting II Data

csv_file = open('vsLefties_Hitting_II_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'XBH', 'TotalBases', 'RunsCreated', 'RunsCreatedPer27', 'TotalPitches', 'PitchesPerPlateAppearance'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+II&group=1&sort=4&time=0&pos=0&qual=0&sortOrder=0&splitType=31&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+II&group=1&sort=4&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=31&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("</td>")[0]
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1]	
			AB = AB.split("<td")[0]
			AB = re.sub("</td>,","",AB)
		XBH = str(a.find_all("td")).split("<span>")[3]
		if XBH == '[]':
			continue
		else:
			XBH = str(a.find_all("td")).split("<td>")[1]
			XBH = XBH.split('Column">')[2]	
			XBH = XBH.split("<td")[0]
			XBH = re.sub("</td>,","",XBH)
		TotalBases = str(a.find_all("td")).split("<span>")[3]
		if TotalBases == '[]':
			continue
		else:
			TotalBases = str(a.find_all("td")).split("<td>")[2]	
			TotalBases = TotalBases.split("<td")[0]
			TotalBases = re.sub("</td>,","",TotalBases)
		RunsCreated = str(a.find_all("td")).split("<span>")[3]
		if RunsCreated == '[]':
			continue
		else:
			RunsCreated = str(a.find_all("td")).split("<span>")[3]
			RunsCreated = RunsCreated.split("<td>")[2]
			RunsCreated = RunsCreated.split('Column">')[1]
			RunsCreated = re.sub("</td>,","",RunsCreated)
		RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
		if RunsCreatedPer27 == '[]':
			continue
		else:
			RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
			RunsCreatedPer27 = RunsCreatedPer27.split("<td>")[3]
			RunsCreatedPer27 = re.sub("</td>","",RunsCreatedPer27).split(",")[0]
		TotalPitches = str(a.find_all("td")).split("<span>")[3]
		if TotalPitches == '[]':
			continue
		else:
			TotalPitches = str(a.find_all("td")).split("<span>")[3]
			TotalPitches = TotalPitches.split("<td>")[8]
			TotalPitches = TotalPitches.split('Column">')[0].split("</td>,")[0]	
		PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
		if PitchesPerPlateAppearance == '[]':
			continue
		else:
			PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split("<td>")[9]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split('Column">')[0].split("</td>]")[0]
		print Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance
		csv_writer.writerow([Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance])
csv_file.close()

print

# Home Hitting II Data

csv_file = open('Home_Hitting_II_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'XBH', 'TotalBases', 'RunsCreated', 'RunsCreatedPer27', 'TotalPitches', 'PitchesPerPlateAppearance'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+II&group=1&sort=4&time=0&pos=0&qual=0&sortOrder=0&splitType=33&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+II&group=1&sort=4&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=33&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("</td>")[0]
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1]	
			AB = AB.split("<td")[0]
			AB = re.sub("</td>,","",AB)
		XBH = str(a.find_all("td")).split("<span>")[3]
		if XBH == '[]':
			continue
		else:
			XBH = str(a.find_all("td")).split("<td>")[1]
			XBH = XBH.split('Column">')[2]	
			XBH = XBH.split("<td")[0]
			XBH = re.sub("</td>,","",XBH)
		TotalBases = str(a.find_all("td")).split("<span>")[3]
		if TotalBases == '[]':
			continue
		else:
			TotalBases = str(a.find_all("td")).split("<td>")[2]	
			TotalBases = TotalBases.split("<td")[0]
			TotalBases = re.sub("</td>,","",TotalBases)
		RunsCreated = str(a.find_all("td")).split("<span>")[3]
		if RunsCreated == '[]':
			continue
		else:
			RunsCreated = str(a.find_all("td")).split("<span>")[3]
			RunsCreated = RunsCreated.split("<td>")[2]
			RunsCreated = RunsCreated.split('Column">')[1]
			RunsCreated = re.sub("</td>,","",RunsCreated)
		RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
		if RunsCreatedPer27 == '[]':
			continue
		else:
			RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
			RunsCreatedPer27 = RunsCreatedPer27.split("<td>")[3]
			RunsCreatedPer27 = re.sub("</td>","",RunsCreatedPer27).split(",")[0]
		TotalPitches = str(a.find_all("td")).split("<span>")[3]
		if TotalPitches == '[]':
			continue
		else:
			TotalPitches = str(a.find_all("td")).split("<span>")[3]
			TotalPitches = TotalPitches.split("<td>")[8]
			TotalPitches = TotalPitches.split('Column">')[0].split("</td>,")[0]	
		PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
		if PitchesPerPlateAppearance == '[]':
			continue
		else:
			PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split("<td>")[9]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split('Column">')[0].split("</td>]")[0]
		print Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance
		csv_writer.writerow([Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance])
csv_file.close()

print

# Away Hitting II Data

csv_file = open('Away_Hitting_II_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'XBH', 'TotalBases', 'RunsCreated', 'RunsCreatedPer27', 'TotalPitches', 'PitchesPerPlateAppearance'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+II&group=1&sort=4&time=0&pos=0&qual=0&sortOrder=0&splitType=34&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+II&group=1&sort=4&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=34&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("</td>")[0]
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1]	
			AB = AB.split("<td")[0]
			AB = re.sub("</td>,","",AB)
		XBH = str(a.find_all("td")).split("<span>")[3]
		if XBH == '[]':
			continue
		else:
			XBH = str(a.find_all("td")).split("<td>")[1]
			XBH = XBH.split('Column">')[2]	
			XBH = XBH.split("<td")[0]
			XBH = re.sub("</td>,","",XBH)
		TotalBases = str(a.find_all("td")).split("<span>")[3]
		if TotalBases == '[]':
			continue
		else:
			TotalBases = str(a.find_all("td")).split("<td>")[2]	
			TotalBases = TotalBases.split("<td")[0]
			TotalBases = re.sub("</td>,","",TotalBases)
		RunsCreated = str(a.find_all("td")).split("<span>")[3]
		if RunsCreated == '[]':
			continue
		else:
			RunsCreated = str(a.find_all("td")).split("<span>")[3]
			RunsCreated = RunsCreated.split("<td>")[2]
			RunsCreated = RunsCreated.split('Column">')[1]
			RunsCreated = re.sub("</td>,","",RunsCreated)
		RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
		if RunsCreatedPer27 == '[]':
			continue
		else:
			RunsCreatedPer27 = str(a.find_all("td")).split("<span>")[3]
			RunsCreatedPer27 = RunsCreatedPer27.split("<td>")[3]
			RunsCreatedPer27 = re.sub("</td>","",RunsCreatedPer27).split(",")[0]
		TotalPitches = str(a.find_all("td")).split("<span>")[3]
		if TotalPitches == '[]':
			continue
		else:
			TotalPitches = str(a.find_all("td")).split("<span>")[3]
			TotalPitches = TotalPitches.split("<td>")[8]
			TotalPitches = TotalPitches.split('Column">')[0].split("</td>,")[0]	
		PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
		if PitchesPerPlateAppearance == '[]':
			continue
		else:
			PitchesPerPlateAppearance = str(a.find_all("td")).split("<span>")[3]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split("<td>")[9]
			PitchesPerPlateAppearance = PitchesPerPlateAppearance.split('Column">')[0].split("</td>]")[0]
		print Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance
		csv_writer.writerow([Names, Pos, Games, AB, XBH, TotalBases, RunsCreated, RunsCreatedPer27, TotalPitches, PitchesPerPlateAppearance])
csv_file.close()

print

# Advanced Hitting Data

csv_file = open('Advanced_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'Hits', 'HRs', 'BBs', 'SOs', 'ContactRate', 'WalkRate', 'WalksPerSO', 'HRsPerFlyBall', 'FlyBallPercentage', 'GroundBallPercentage', 'IsolatedPower', 'SecondaryAVG', 'BABIP'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+RATIOS&group=1&time=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+RATIOS&group=1&time=" + "{}".format(Time) + "")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("<td")[0]
			Games = re.sub("</td>,","",Games)
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[0]
			AB = AB.split("</td>,")[0]	
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[2]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		HRs = str(a.find_all("td")).split("<span>")[3]
		if HRs == '[]':
			continue
		else:
			HRs = str(a.find_all("td")).split("<span>")[3]
			HRs = HRs.split("<td>")[3]
			HRs = re.sub("</td>","",HRs).split(",")[0]	
		BBs = str(a.find_all("td")).split("<span>")[3]
		if BBs == '[]':
			continue
		else:
			BBs = str(a.find_all("td")).split("<span>")[3]
			BBs = BBs.split("<td>")[4]
			BBs = re.sub("</td>","",BBs).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[5]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ContactRate = str(a.find_all("td")).split("<span>")[3]
		if ContactRate == '[]':
			continue
		else:
			ContactRate = str(a.find_all("td")).split("<span>")[3]
			ContactRate = ContactRate.split("<td>")[5]
			ContactRate = ContactRate.split('Column">')[1].split('</td>')[0]		
		WalkRate = str(a.find_all("td")).split("<span>")[3]
		if WalkRate == '[]':
			continue
		else:
			WalkRate = str(a.find_all("td")).split("<span>")[3]
			WalkRate = WalkRate.split("<td>")[6]
			WalkRate = WalkRate.split('</td>')[0]
		WalksPerSO = str(a.find_all("td")).split("<span>")[3]
		if WalksPerSO == '[]':
			continue
		else:
			WalksPerSO = str(a.find_all("td")).split("<span>")[3]
			WalksPerSO = WalksPerSO.split("<td>")[7]
			WalksPerSO = WalksPerSO.split('Column">')[0].split("</td>,")[0]
		HRsPerFlyBall = str(a.find_all("td")).split("<span>")[3]
		if HRsPerFlyBall == '[]':
			continue
		else:
			HRsPerFlyBall = str(a.find_all("td")).split("<span>")[3]
			HRsPerFlyBall = HRsPerFlyBall.split("<td>")[8]
			HRsPerFlyBall = HRsPerFlyBall.split('Column">')[0].split("</td>,")[0]			
		FlyBallPercentage = str(a.find_all("td")).split("<span>")[3]
		if FlyBallPercentage == '[]':
			continue
		else:
			FlyBallPercentage = str(a.find_all("td")).split("<span>")[3]
			FlyBallPercentage = FlyBallPercentage.split("<td>")[8]
			FlyBallPercentage = FlyBallPercentage.split('Column">')[1].split("</td>,")[0]
		GroundBallPercentage = str(a.find_all("td")).split("<span>")[3]
		if GroundBallPercentage == '[]':
			continue
		else:
			GroundBallPercentage = str(a.find_all("td")).split("<span>")[3]
			GroundBallPercentage = GroundBallPercentage.split("<td>")[8]
			GroundBallPercentage = GroundBallPercentage.split('Column">')[2].split("</td>,")[0]			
		IsolatedPower = str(a.find_all("td")).split("<span>")[3]
		if IsolatedPower == '[]':
			continue
		else:
			IsolatedPower = str(a.find_all("td")).split("<span>")[3]
			IsolatedPower = IsolatedPower.split("<td>")[9]
			IsolatedPower = IsolatedPower.split('Column">')[0].split("</td>,")[0]	
		SecondaryAVG = str(a.find_all("td")).split("<span>")[3]
		if SecondaryAVG == '[]':
			continue
		else:
			SecondaryAVG = str(a.find_all("td")).split("<span>")[3]
			SecondaryAVG = SecondaryAVG.split("<td>")[10]
			SecondaryAVG = SecondaryAVG.split('Column">')[0].split("</td>,")[0]	
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[11]
			BABIP = BABIP.split('Column">')[0]
			BABIP = BABIP.split("</td>]")[0]	
		print Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, HRsPerFlyBall, FlyBallPercentage, GroundBallPercentage, IsolatedPower, SecondaryAVG, BABIP
		csv_writer.writerow([Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, HRsPerFlyBall, FlyBallPercentage, GroundBallPercentage, IsolatedPower, SecondaryAVG, BABIP])
csv_file.close()

print

# Lefty Advanced Hitting Data

csv_file = open('vsLefties_Advanced_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'Hits', 'HRs', 'BBs', 'SOs', 'ContactRate', 'WalkRate', 'WalksPerSO', 'IsolatedPower', 'SecondaryAverage', 'BABIP'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+RATIOS&group=1&sort=11&time=0&pos=0&qual=0&sortOrder=0&splitType=31&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+RATIOS&group=1&sort=11&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=31&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("<td")[0]
			Games = re.sub("</td>,","",Games)
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1].split("</td>,")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[2]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		HRs = str(a.find_all("td")).split("<span>")[3]
		if HRs == '[]':
			continue
		else:
			HRs = str(a.find_all("td")).split("<span>")[3]
			HRs = HRs.split("<td>")[3]
			HRs = re.sub("</td>","",HRs).split(",")[0]	
		BBs = str(a.find_all("td")).split("<span>")[3]
		if BBs == '[]':
			continue
		else:
			BBs = str(a.find_all("td")).split("<span>")[3]
			BBs = BBs.split("<td>")[4]
			BBs = re.sub("</td>","",BBs).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[5]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ContactRate = str(a.find_all("td")).split("<span>")[3]
		if ContactRate == '[]':
			continue
		else:
			ContactRate = str(a.find_all("td")).split("<span>")[3]
			ContactRate = ContactRate.split("<td>")[5].split('Column">')[1].split('</td>')[0]	
		WalkRate = str(a.find_all("td")).split("<span>")[3]
		if WalkRate == '[]':
			continue
		else:
			WalkRate = str(a.find_all("td")).split("<span>")[3]
			WalkRate = WalkRate.split('Column">')[3].split('</td>')[0]
		WalksPerSO = str(a.find_all("td")).split("<span>")[3]
		if WalksPerSO == '[]':
			continue
		else:
			WalksPerSO = str(a.find_all("td")).split("<span>")[3]
			WalksPerSO = WalksPerSO.split("<td>")[6].split('</td>')[0]
		IsolatedPower = str(a.find_all("td")).split("<span>")[3]
		if IsolatedPower == '[]':
			continue
		else:
			IsolatedPower = str(a.find_all("td")).split("<span>")[3]
			IsolatedPower = IsolatedPower.split("<td>")[7].split('Column">')[0].split("</td>,")[0]
		SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
		if SecondaryAverage == '[]':
			continue
		else:
			SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
			SecondaryAverage = SecondaryAverage.split("<td>")[8].split('Column">')[0].split("</td>,")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[8].split('Column">')[1].split("</td>]")[0]
		print Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP
		csv_writer.writerow([Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP])
csv_file.close()

print

# Righty Advanced Hitting Data

csv_file = open('vsRighties_Advanced_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'Hits', 'HRs', 'BBs', 'SOs', 'ContactRate', 'WalkRate', 'WalksPerSO', 'IsolatedPower', 'SecondaryAverage', 'BABIP'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+RATIOS&group=1&sort=11&time=0&pos=0&qual=0&sortOrder=0&splitType=32&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+RATIOS&group=1&sort=11&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=32&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("<td")[0]
			Games = re.sub("</td>,","",Games)
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1].split("</td>,")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[2]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		HRs = str(a.find_all("td")).split("<span>")[3]
		if HRs == '[]':
			continue
		else:
			HRs = str(a.find_all("td")).split("<span>")[3]
			HRs = HRs.split("<td>")[3]
			HRs = re.sub("</td>","",HRs).split(",")[0]	
		BBs = str(a.find_all("td")).split("<span>")[3]
		if BBs == '[]':
			continue
		else:
			BBs = str(a.find_all("td")).split("<span>")[3]
			BBs = BBs.split("<td>")[4]
			BBs = re.sub("</td>","",BBs).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[5]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ContactRate = str(a.find_all("td")).split("<span>")[3]
		if ContactRate == '[]':
			continue
		else:
			ContactRate = str(a.find_all("td")).split("<span>")[3]
			ContactRate = ContactRate.split("<td>")[5].split('Column">')[1].split('</td>')[0]	
		WalkRate = str(a.find_all("td")).split("<span>")[3]
		if WalkRate == '[]':
			continue
		else:
			WalkRate = str(a.find_all("td")).split("<span>")[3]
			WalkRate = WalkRate.split('Column">')[3].split('</td>')[0]
		WalksPerSO = str(a.find_all("td")).split("<span>")[3]
		if WalksPerSO == '[]':
			continue
		else:
			WalksPerSO = str(a.find_all("td")).split("<span>")[3]
			WalksPerSO = WalksPerSO.split("<td>")[6].split('</td>')[0]
		IsolatedPower = str(a.find_all("td")).split("<span>")[3]
		if IsolatedPower == '[]':
			continue
		else:
			IsolatedPower = str(a.find_all("td")).split("<span>")[3]
			IsolatedPower = IsolatedPower.split("<td>")[7].split('Column">')[0].split("</td>,")[0]
		SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
		if SecondaryAverage == '[]':
			continue
		else:
			SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
			SecondaryAverage = SecondaryAverage.split("<td>")[8].split('Column">')[0].split("</td>,")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[8].split('Column">')[1].split("</td>]")[0]
		print Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP
		csv_writer.writerow([Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP])
csv_file.close()

print

# Home Advanced Hitting Data

csv_file = open('Home_Advanced_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'Hits', 'HRs', 'BBs', 'SOs', 'ContactRate', 'WalkRate', 'WalksPerSO', 'IsolatedPower', 'SecondaryAverage', 'BABIP'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+RATIOS&group=1&sort=11&time=0&pos=0&qual=0&sortOrder=0&splitType=33&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+RATIOS&group=1&sort=11&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=33&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("<td")[0]
			Games = re.sub("</td>,","",Games)
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1].split("</td>,")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[2]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		HRs = str(a.find_all("td")).split("<span>")[3]
		if HRs == '[]':
			continue
		else:
			HRs = str(a.find_all("td")).split("<span>")[3]
			HRs = HRs.split("<td>")[3]
			HRs = re.sub("</td>","",HRs).split(",")[0]	
		BBs = str(a.find_all("td")).split("<span>")[3]
		if BBs == '[]':
			continue
		else:
			BBs = str(a.find_all("td")).split("<span>")[3]
			BBs = BBs.split("<td>")[4]
			BBs = re.sub("</td>","",BBs).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[5]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ContactRate = str(a.find_all("td")).split("<span>")[3]
		if ContactRate == '[]':
			continue
		else:
			ContactRate = str(a.find_all("td")).split("<span>")[3]
			ContactRate = ContactRate.split("<td>")[5].split('Column">')[1].split('</td>')[0]	
		WalkRate = str(a.find_all("td")).split("<span>")[3]
		if WalkRate == '[]':
			continue
		else:
			WalkRate = str(a.find_all("td")).split("<span>")[3]
			WalkRate = WalkRate.split('Column">')[3].split('</td>')[0]
		WalksPerSO = str(a.find_all("td")).split("<span>")[3]
		if WalksPerSO == '[]':
			continue
		else:
			WalksPerSO = str(a.find_all("td")).split("<span>")[3]
			WalksPerSO = WalksPerSO.split("<td>")[6].split('</td>')[0]
		IsolatedPower = str(a.find_all("td")).split("<span>")[3]
		if IsolatedPower == '[]':
			continue
		else:
			IsolatedPower = str(a.find_all("td")).split("<span>")[3]
			IsolatedPower = IsolatedPower.split("<td>")[7].split('Column">')[0].split("</td>,")[0]
		SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
		if SecondaryAverage == '[]':
			continue
		else:
			SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
			SecondaryAverage = SecondaryAverage.split("<td>")[8].split('Column">')[0].split("</td>,")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[8].split('Column">')[1].split("</td>]")[0]
		print Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP
		csv_writer.writerow([Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP])
csv_file.close()

print

# Away Advanced Hitting Data

csv_file = open('Away_Advanced_Hitting_Data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Names', 'Pos', 'Games', 'AB', 'Hits', 'HRs', 'BBs', 'SOs', 'ContactRate', 'WalkRate', 'WalksPerSO', 'IsolatedPower', 'SecondaryAverage', 'BABIP'])

Teams = str("arizona-diamondbacks"),str("atlanta-braves"),str("chicago-cubs"),str("cincinnati-reds"),str("colorado-rockies"),str("los-angeles-dodgers"),str("miami-marlins"),str("milwaukee-brewers"),str("new-york-mets"),str("philadelphia-phillies"),str("pittsburgh-pirates"),str("san-diego-padres"),str("san-francisco-giants"),str("st-louis-cardinals"),str("washington-nationals"),str("baltimore-orioles"),str("boston-red-sox"),str("chicago-white-sox"),str("cleveland-indians"),str("detroit-tigers"),str("houston-astros"),str("kansas-city-royals"),str("los-angeles-angels"),str("minnesota-twins"),str("new-york-yankees"),str("oakland-athletics"),str("seattle-mariners"),str("tampa-bay-rays"),str("texas-rangers"),str("toronto-blue-jays")
Range = range(0,NumberOfTeams)
for i in Range:
	TeamList = Teams[i]
	url = ("https://www.foxsports.com/mlb/")
	#full url = https://www.foxsports.com/mlb/TEAM-NAME-HERE-team-stats?season=2017&category=BATTING+RATIOS&group=1&sort=11&time=0&pos=0&qual=0&sortOrder=0&splitType=34&statID=0
	p = requests.get(url + "{}".format(Teams[i]) + "-team-stats?season=" + "{}".format(Year) + "&category=BATTING+RATIOS&group=1&sort=11&time=" + "{}".format(Time) + "&pos=0&qual=0&sortOrder=0&splitType=34&statID=0")
	soup = BeautifulSoup(p.content, "html.parser")
	Data = soup.find_all("tr",{"class": "wisbb_fvStand "})
	for a in Data:
		Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(a.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		Pos = str(a.find_all("td")).split("span")[8].split(",")[0]
		if Pos == '>\\n</div>\\n</td>':
			continue
		else:
			Pos = str(a.find_all("td")).split("span")[8].split(">")[1].split("</")[0]
		Games = str(a.find_all("td")).split("<td>")[0]
		if Games == '[]':
			continue
		else:
			Games = str(a.find_all("td")).split("<td>")[1]
			Games = Games.split("<td")[0]
			Games = re.sub("</td>,","",Games)
		AB = str(a.find_all("td")).split("<td>")[0]
		if AB == '[]':
			continue
		else:
			AB = str(a.find_all("td")).split("<td>")[1]
			AB = AB.split('Column">')[1].split("</td>,")[0]
		Hits = str(a.find_all("td")).split("<span>")[3]
		if Hits == '[]':
			continue
		else:
			Hits = str(a.find_all("td")).split("<span>")[3]
			Hits = Hits.split("<td>")[2]
			Hits = re.sub("</td>","",Hits).split(",")[0]
		HRs = str(a.find_all("td")).split("<span>")[3]
		if HRs == '[]':
			continue
		else:
			HRs = str(a.find_all("td")).split("<span>")[3]
			HRs = HRs.split("<td>")[3]
			HRs = re.sub("</td>","",HRs).split(",")[0]	
		BBs = str(a.find_all("td")).split("<span>")[3]
		if BBs == '[]':
			continue
		else:
			BBs = str(a.find_all("td")).split("<span>")[3]
			BBs = BBs.split("<td>")[4]
			BBs = re.sub("</td>","",BBs).split(",")[0]
		SOs = str(a.find_all("td")).split("<span>")[3]
		if SOs == '[]':
			continue
		else:
			SOs = str(a.find_all("td")).split("<span>")[3]
			SOs = SOs.split("<td>")[5]
			SOs = re.sub("</td>","",SOs).split(",")[0]
		ContactRate = str(a.find_all("td")).split("<span>")[3]
		if ContactRate == '[]':
			continue
		else:
			ContactRate = str(a.find_all("td")).split("<span>")[3]
			ContactRate = ContactRate.split("<td>")[5].split('Column">')[1].split('</td>')[0]	
		WalkRate = str(a.find_all("td")).split("<span>")[3]
		if WalkRate == '[]':
			continue
		else:
			WalkRate = str(a.find_all("td")).split("<span>")[3]
			WalkRate = WalkRate.split('Column">')[3].split('</td>')[0]
		WalksPerSO = str(a.find_all("td")).split("<span>")[3]
		if WalksPerSO == '[]':
			continue
		else:
			WalksPerSO = str(a.find_all("td")).split("<span>")[3]
			WalksPerSO = WalksPerSO.split("<td>")[6].split('</td>')[0]
		IsolatedPower = str(a.find_all("td")).split("<span>")[3]
		if IsolatedPower == '[]':
			continue
		else:
			IsolatedPower = str(a.find_all("td")).split("<span>")[3]
			IsolatedPower = IsolatedPower.split("<td>")[7].split('Column">')[0].split("</td>,")[0]
		SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
		if SecondaryAverage == '[]':
			continue
		else:
			SecondaryAverage = str(a.find_all("td")).split("<span>")[3]
			SecondaryAverage = SecondaryAverage.split("<td>")[8].split('Column">')[0].split("</td>,")[0]
		BABIP = str(a.find_all("td")).split("<span>")[3]
		if BABIP == '[]':
			continue
		else:
			BABIP = str(a.find_all("td")).split("<span>")[3]
			BABIP = BABIP.split("<td>")[8].split('Column">')[1].split("</td>]")[0]
		print Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP
		csv_writer.writerow([Names, Pos, Games, AB, Hits, HRs, BBs, SOs, ContactRate, WalkRate, WalksPerSO, IsolatedPower, SecondaryAverage, BABIP])
csv_file.close()

print

#NF Pitcher & Batter Projections

p = requests.get(b)
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('pitchers_NF.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Tm', 'Opp', 'Pos', 'fp', 'price', 'value'])

statData = soup.find_all("tbody", {"class": "stat-table__body"})
fullData = str(soup.find_all("a", {"class": "full"}))
fullData = fullData

sub = "href"
count = fullData.count(sub,0,100000)	
count = int(count)
if count < x:
	count = int(count)
else:
	count = x
for a in statData:
	for i in range(count):
		if i > 0:
				pitcherfirstName = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[4]
				pitcherfirstName = pitcherfirstName.split('>')[0]
				pitcherfirstName = re.sub('"', '', pitcherfirstName).split("</a")[0].split(" ")[8][8:]
				pitcherlastName = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[4]
				pitcherlastName = pitcherlastName.split('>')[0]
				pitcherlastName = re.sub('"', '', pitcherlastName).split("</a")[0].split(" ")[9]
				pitcherTm = str(a.find_all("span", {"team-player__team active"})[i-1]).split(' ')[46]
				pitcherOpp = str(a.find_all("span", {"team-player__team "})[i-1]).split(' ')[46]
				pitcherPos = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[6].split('</span')[0]
				pitcherFP = str(a.find_all("td", {"class": "fp active"})[i-1]).split('>')[1].split(" ")[32]
				pitcherPrice = str(a.find_all("td", {"class": "cost"})[i-1]).split('>')[1].split(" ")[32]
				pitcherValue = str(a.find_all("td", {"class": "value"})[i-1]).split('>')[1].split(" ")[32]
			#	WL = str(a.find_all("td", {"class": "wl"})[i-1]).split('>')[1].split(" ")[32]
			#	SV = str(a.find_all("td", {"class": "sv"})[i-1]).split('>')[1].split(" ")[32]
			#	IP = str(a.find_all("td", {"class": "ip"})[i-1]).split('>')[1].split(" ")[32]
			#	H = str(a.find_all("td", {"class": "h"})[i-1]).split('>')[1].split(" ")[32]
			#	ER = str(a.find_all("td", {"class": "er"})[i-1]).split('>')[1].split(" ")[32]
			#	HR = str(a.find_all("td", {"class": "hr"})[i-1]).split('>')[1].split(" ")[32]
			#	K = str(a.find_all("td", {"class": "k"})[i-1]).split('>')[1].split(" ")[32]
			#	BB = str(a.find_all("td", {"class": "bb"})[i-1]).split('>')[1].split(" ")[32]
			#	ERA = str(a.find_all("td", {"class": "era"})[i-1]).split('>')[1].split(" ")[32]
			#	WHIP = str(a.find_all("td", {"class": "whip"})[i-1]).split('>')[1].split(" ")[32]
				
				print pitcherfirstName + " " + pitcherlastName, pitcherTm, pitcherOpp, pitcherPos, pitcherFP, pitcherPrice, pitcherValue
				csv_writer.writerow([pitcherfirstName + " " + pitcherlastName, pitcherTm, pitcherOpp, pitcherPos, pitcherFP, pitcherPrice, pitcherValue])
csv_file.close()

print

# Gets todays pitchers and batters in 1 csv

p = requests.get("http://mlb.mlb.com/news/probable_pitchers/index.jsp?c_id=mlb&date=" + "{}".format(year) + "/" + "{}".format(month) + "/" + "{}".format(day))
# real url: http://mlb.mlb.com/news/probable_pitchers/index.jsp?c_id=mlb&date=2018/02/24
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('PlayersOrder_MLB.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Tm // Arm', 'Opp', 'Pos', 'fp', 'price', 'value'])

data = soup.find_all("div", {"class": "module"})

for item in data:
	Pitcher = str(item.find_all("h5")).split("</a>")[0].split(">")[2]
	Pitcher = re.sub(" Jr.","", Pitcher)
	Pitcher = re.sub("'","", Pitcher)
	Pitcher = re.sub("-"," ", Pitcher)
	Arm =  str(item.find_all("h5")).split("<span>")[1].split("</span>")[0]
	print Pitcher, Arm
	csv_writer.writerow([Pitcher, Arm])

data1 = soup.find_all("div", {"class": "pitcher last"})
for item in data1:
	Pitcher = str(item.find_all("h5")).split("</a>")[0].split(">")[2]
	Pitcher = re.sub(" Jr.","", Pitcher)
	Pitcher = re.sub("'","", Pitcher)
	Pitcher = re.sub("-"," ", Pitcher)
	Arm = str(item.find_all("h5")).split("<span>")[1].split("</span>")[0]	
	print Pitcher, Arm
	csv_writer.writerow([Pitcher, Arm])

p = requests.get(c)
soup = BeautifulSoup(p.content, "html.parser")

statData = soup.find_all("tbody", {"class": "stat-table__body"})
fullData = str(soup.find_all("a", {"class": "full"}))
fullData = fullData

sub = "href"
count = fullData.count(sub,0,100000)	
count = int(count)
if count < y:
	count = int(count)
else:
	count = y
for a in statData:
	for i in range(count):
		if i > 0:
				firstName = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[4]
				firstName = firstName.split('>')[0]
				firstName = re.sub('"', '', firstName).split("</a")[0].split(" ")[36]
				firstName = re.sub("'","", firstName)
				firstName = re.sub("-"," ", firstName)
				lastName = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[4]
				lastName = lastName.split('>')[0]
				lastName = re.sub('"', '', lastName).split("</a")[0].split(" ")[37]
				lastName = re.sub(" Jr.","", lastName)
				lastName = re.sub("'","", lastName)
				lastName = re.sub("-"," ", lastName)
				Tm = str(a.find_all("span", {"team-player__team active"})[i-1]).split(' ')[42]
				Opp = str(a.find_all("span", {"team-player__team "})[i-1]).split(' ')[42]
				Pos = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[6].split('</span')[0]
				fp = str(a.find_all("td", {"class": "fp active"})[i-1]).split('>')[1].split(" ")[28]
				price = str(a.find_all("td", {"class": "cost"})[i-1]).split('>')[1].split(" ")[28]
				value = str(a.find_all("td", {"class": "value"})[i-1]).split('>')[1].split(" ")[28]
			#	PA = str(a.find_all("td", {"class": "pa"})[i-1]).split('>')[1].split(" ")[28]
			#	BB = str(a.find_all("td", {"class": "bb"})[i-1]).split('>')[1].split(" ")[28]
			#	single = str(a.find_all("td", {"class": "1b"})[i-1]).split('>')[1].split(" ")[28]
			#	double = str(a.find_all("td", {"class": "2b"})[i-1]).split('>')[1].split(" ")[28]
			#	triple = str(a.find_all("td", {"class": "3b"})[i-1]).split('>')[1].split(" ")[28]
			#	HR = str(a.find_all("td", {"class": "hr"})[i-1]).split('>')[1].split(" ")[28]
			#	R = str(a.find_all("td", {"class": "r"})[i-1]).split('>')[1].split(" ")[28]
			#	RBI = str(a.find_all("td", {"class": "rbi"})[i-1]).split('>')[1].split(" ")[28]
			#	SB = str(a.find_all("td", {"class": "sb"})[i-1]).split('>')[1].split(" ")[28]
			#	K = str(a.find_all("td", {"class": "k"})[i-1]).split('>')[1].split(" ")[28]
			#	AVG = str(a.find_all("td", {"class": "avg"})[i-1]).split('>')[1].split(" ")[28]
				
				print firstName + " " + lastName, Tm, Opp, Pos, fp, price, value
				csv_writer.writerow([firstName + " " + lastName, Tm, Opp, Pos, fp, price, value])
csv_file.close()

print

# MLB players teams

csv_file = open('mlb_bio.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'team'])

pageNumber = range(1,150)
for count in pageNumber:
	url = ("https://www.foxsports.com/mlb/players?teamId=0&season=2018&position=0&")
	#full url = https://www.foxsports.com/nba/players?teamId=0&season=2017&position=0&page=[loop over # of pages]
	p = requests.get(url + "&page={}".format(count) + "&country=0&grouping=0&weightclass=0")
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all("tr",{"class": "wisbb_fvStand"})
	for item in data:
		Names = str(item.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[0]
		if Names == '[]':
			continue
		else:
			Names = str(item.find_all("a",{"class": "wisbb_fullPlayer"})).split("mlb/")[1].split("-player")[0]
			Names = re.sub('-', " ",Names)
		team = str(item.find("td",{"class": "wisbb_priorityColumn"}))
		if team == 'None':
			continue
		else:
			team = team.split(">")[2]
			team = re.sub("</a",'',team)
			print Names, team
			csv_writer.writerow([Names, team])
csv_file.close()

print

#Batting Lineup

csv_file = open('LU.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Player'])

p = requests.get("https://www.fantasyalarm.com/mlb/lineups/")
soup = BeautifulSoup(p.content, "html.parser")

data = soup.find_all("table", {"class": "text-white display nowrap mlb"})
for item in data:
	for i in range(0,1):
		for a in range(0,15):
			player = str(item.find_all("tr", {"class": "data-row "})).split("Opp Pitcher")[0]
			if player == '[<tr class="data-row "><td class="':
				continue
			else:
				try:
					player = str(item.find_all("tr", {"class": "data-row "})).split("/player/")[a+1].split("/")[0]
					player = re.sub("-jr","",player)
					try:
						if player.find("-") >= 2:
							player = player.replace("-"," ",1)
							player = player.replace("-"," ",1)
							#of "-" at/after the 2nd index, do these actions
						else:
							pass

							if player.count("-") == 3:
								player = player.replace("-","",1)
								player = player.replace("-"," ",1)
								#if 3 "-" occurances, then get rid of first 2
							else:
								player = player.replace("-"," ",1)
								#if 2 "-" occurances, then get rid of first 2
					except:
						break
						#Skip over instances where out of index
				except:
					break
					#Skip over instances where out of index
				print player
				csv_writer.writerow([player])
csv_file.close() 

print

# roto projections for batters and pitchers

csv_file = open('Roto.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Salary', 'Team', 'Position', 'Opponent', 'Ceiling', 'Floor', 'Projected FP'])

url1 = 'https://rotogrinders.com/projected-stats/mlb-pitcher.csv?site=fanduel'
url2 = 'https://rotogrinders.com/projected-stats/mlb-hitter.csv?site=fanduel'
r = requests.get(url1)
text = r.iter_lines()
reader = csv.reader(text, delimiter=',')
for item in reader:
	print item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]
	csv_writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])
r = requests.get(url2)
text2 = r.iter_lines()
reader2 = csv.reader(text2, delimiter=',')
for item in reader2:
	print item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]
 	csv_writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])
csv_file.close() 

print









