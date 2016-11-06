import sys
import random

print 'Content-Type: text/html'
print '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

<title>
CV Invitational Soccer Lotto
</title>
</head>
'''
print '<body>'
print '<h1>CV Invitational Soccer Lotto</h1>'
print ''

# Read form textarea data 
data = sys.stdin.read()

dter = '%0D%0A'
players = [x.replace('+', ' ').strip() for x in data[data.find('=')+1:].split(dter) if x] 
players = [x for x in players if x]
print players

random.seed()
random.shuffle(players)

# print players

# even position
team0 = players[0::2]
# odd position
team1 = players[1::2]
teams = [team0, team1]

random_bit = int(random.getrandbits(1))

white_west_facing = bool(random.getrandbits(1)) 

print '<b>WHITE TEAM:</b>'
print '<pre>'
for p in teams[random_bit]:
    print p
print '</pre>'

print '<b>DARK TEAM:</b>'

print '<pre>'
for p in teams[1-random_bit]:
    print p
print '</pre>'

# Who is facing west first
sys.stdout.write('<b>FIELD SELECTION: </b>')
if len(players):
    if white_west_facing:
        print 'WHITE TEAM FACES WEST AT GAME START'
    else:
        print 'DARK TEAM FACES WEST AT GAME START'

print '<br /><br />'

print '''<form method="post" action="/">
Enter Roster (one player per line) <br />
<textarea name="roster", id="textarea", cols="60", rows="20"></textarea>
<br />
<input type="submit", value="Generate">
</form>'''

print '</body>'
print '</html>'

