netname = None
password = None
sourceEmail = None
emailPass = None
toSendText = 0
toSendEmail = 0
toSendDesktopNotification = 0
cellNum = None
provider = None
destEmail = None

import sqlite3
from getpass import getpass

conn = sqlite3.connect('ConcordiaGrades.db')

# Check if the settings table exists, if not then create it
cursor = conn.execute('''SELECT name 
						 FROM sqlite_master 
						 WHERE type='table' 
						 AND name='Settings';''')

settingsExist = not (len(cursor.fetchall()) == 0)

if not settingsExist:
	conn.execute('''CREATE TABLE Settings(
						Netname VARCHAR(7) PRIMARY KEY,
						Password VARCHAR(30) NOT NULL,
						SourceEmail VARCHAR(254) NOT NULL,
						EmailPass VARCHAR(50) NOT NULL,
						ToSendText INTEGER NOT NULL,
						ToSendEmail INTEGER NOT NULL,
						CellNum VARCHAR(11),
						Provider VARCHAR(40),
						DestEmail VARCHAR(254)
					);''')
	print("MyConcordia netname: ")
	netname = input()
	print("MyConcordia password: ")
	password = getpass()
	print("Gmail username to send texts/emails from (create a dummy account if need be): ")
	sourceEmail = input()
	print("Gmail password: ")
	emailPass = getpass()
	
	print("This script can notify you of new grades by text message and email.")
	print("Please note: Choosing to receive texts by email-to-SMS Gateway might result in extra phone bill charges, depending on your carrier. Use at your own discretion.")
	
	print("Do you want to receive text message notifications? (y/n): ")
	toSendText = input()
	while True:
		if toSendText == 'y':
			toSendText = 1
			break
		elif toSendText == 'n':
			toSendText = 0
			break
		else:
			print("Invalid input. Do you want to receive text message notifications? (y/n): ")
			toSendText = input()

	print("Do you want to receive email notifications? (y/n): ")
	toSendEmail = input()
	while True:
		if toSendEmail == 'y':
			toSendEmail = 1
			break
		elif toSendEmail == 'n':
			toSendEmail = 0
			break
		else:
			print("Invalid input. Do you want to receive email notifications? (y/n): ")
			toSendEmail = input()
	
	if toSendText:
		print("Input cell number to receive text messages at: ")
		cellNum = input()
		print("Input cell provider (Select a provider from smsGateways.txt; if yours is not there, add it to file): ")
		provider = input()
	
	if toSendEmail:
		print("Input email to receive notifications at: ")
		destEmail = input()

	conn.execute("INSERT INTO `Settings` " +
	"(`Netname`, `Password`, `SourceEmail`, `EmailPass`, `ToSendText`, `ToSendEmail`, `CellNum`, `Provider`, `DestEmail`)" +
	" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
	(netname, password, sourceEmail, emailPass, toSendText, toSendEmail, cellNum, provider, destEmail))
	conn.commit()
else:
	print("Settings already exist. To input new settings, please delete ConcordiaGrades.db")

conn.close()