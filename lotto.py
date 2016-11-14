#!/usr/bin/env python

# [START imports]
import os
import sys
import random

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
   
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())


    def post(self):
        data = self.request.get('roster')

        # print "DEBUG:" + data

        dter = '\r\n'
        players = [x.replace('+', ' ').strip() for x in data[data.find('=')+1:].split(dter) if x] 
        players = [x for x in players if x]

        # Strong random number
        r = random.SystemRandom()
        r.shuffle(players)

        # even position
        team0 = players[0::2]
        # odd position
        team1 = players[1::2]
        teams = [team0, team1]
        random_bit = int(r.getrandbits(1))
        white_west_facing = bool(r.getrandbits(1)) 

        # template values
        team_white = teams[random_bit]
        team_dark  = teams[1 - random_bit]
        field_selection = ''
        if len(players):
            if white_west_facing:
                field_selection = 'WHITE TEAM FACES WEST AT GAME START'
            else:
                field_selection = 'DARK TEAM FACES WEST AT GAME START'

        template_values = {
            'team_white': team_white,
            'team_dark': team_dark,
            'field_selection': field_selection,
        }
   
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_values))

# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=False)

# [END app]

