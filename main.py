#!/usr/bin/env python
import webapp2
import jinja2
import os
import logging
import random
import header
from ex import *
import ex
from google.appengine.ext import ndb
from google.appengine.api import users

import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):
    if(users.get_current_user() == None):
      renderedHeader = header.getHomeHeader("None")
      renderedHeader = renderedHeader.replace('<li><a href="/settings">SETTINGS</a></li>', '')
      renderedHeader = renderedHeader.replace('Logout', 'Login')
      renderedHeader = renderedHeader.replace('LOGOUT', 'LOGIN')
    else:
      query = PTUser.query().filter(PTUser.user == users.get_current_user())
      if len(query.fetch()) == 0:
        renderedHeader = header.getHomeHeader("None")
      else:
        currUser = query.fetch()[0]
        renderedHeader = header.getHomeHeader(currUser.PTType)
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
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    if len(query.fetch()) == 0:
      renderedHeader = header.getHeader("None")
    else:
      currUser = query.fetch()[0]
      renderedHeader = header.getHeader(currUser.PTType)
    #if currUser == "Patient": TODO -- prevent unauthorized access
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('dashboard.html')
    self.response.out.write(template.render(template_values))

class SettingsHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    if len(query.fetch()) == 0:
      renderedHeader = header.getHeader("None")
    else:
      currUser = query.fetch()[0]
      renderedHeader = header.getHeader(currUser.PTType)

    allTherapistsQ = PTUser.query().filter(PTUser.PTType == "Therapist")
    allTherapists = allTherapistsQ.fetch()
    logging.info(allTherapists)
    template_values = {"header": renderedHeader, "footer":header.getFooter(), "therapists":allTherapists, "currEmail":users.get_current_user().email()}
    template = jinja_environment.get_template('settings.html')
    self.response.out.write(template.render(template_values))
# TODO: create new handler to update settings based on a simple binary radio button
# form which is selected by the user in settings.

class SettingsUpdateHandler(webapp2.RequestHandler):
  def get(self):
    userrole = self.request.get('role')
    logging.info(userrole)
    logging.info(userrole == "Therapist")
    therapistEmail = self.request.get('therapist')
    user = users.get_current_user()
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()
    therapistUser = None
    if userrole == "Patient":
      therapistUser = users.User(therapistEmail)
    if len(currUser) == 0:
      p = PTUser(user=user, PTType=userrole, therapist=therapistUser)
    else:
      p = currUser[0]
      p.PTType=userrole
      p.therapist = therapistUser

    logging.info(p)
    p.put()
    self.redirect('/dashboard')
    # template_values = {'header': header.getHeader(userrole), 'footer': header.getFooter()}
    # template = main.jinja_environment.get_template('settings.html')
    # self.response.out.write(template.render(template_values))

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
  ('/settings', SettingsHandler), #patient + therapist
  ('/settingsUpdate', SettingsUpdateHandler), #patient + therapist
  ('/newPlan', ex.IntermHandler), #intermediate page displaying new plan
], debug=True)
