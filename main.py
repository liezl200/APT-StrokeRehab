#!/usr/bin/env python
import webapp2
import jinja2
import os
import logging
import random
import header
import ex
from google.appengine.ext import ndb
from google.appengine.api import users

import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):
    renderedHeader = header.getHeader('/')
    if(users.get_current_user() == None):
      renderedHeader = renderedHeader.replace('<li><a href="/settings">SETTINGS</a></li>', '')
      renderedHeader = renderedHeader.replace('Logout', 'Login')
      renderedHeader = renderedHeader.replace('LOGOUT', 'LOGIN')
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template_values['randomImg'] = "/static/201.jpg"
    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    loginurl = users.create_login_url(dest_url='/', _auth_domain=None, federated_identity=None)
    self.redirect(loginurl)

class LogoutHandler(webapp2.RequestHandler):
  def get(self):
    dest_url = '/'
    logouturl = users.create_logout_url(dest_url)
    self.redirect(logouturl)
    logging.info(logouturl)

# Therapist-use only
class DashboardHandler(webapp2.RequestHandler):
	def get(self):
		query = PTUser.query().filter(PTUser.userID == users.get_current_user().user_id())
		currUser = query.fetch()
		#if currUser == "Patient": TODO -- prevent unauthorized access
		renderedHeader = header.getHeader(currUser == "Patient")
		template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('dashboard.html')
    self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(loader=
  jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/Logout', LogoutHandler),
  ('/Login', LoginHandler),
  ('/exercises', ex.ExercisesHandler), # patient
  ('/progress', ex.ProgressHandler), # patient + therapist (direct access through patient userID)
  ('/createTrack', ex.TrackHandler), # therapist
  ('/dashboard', DashboardHandler), # therapist
], debug=True)
