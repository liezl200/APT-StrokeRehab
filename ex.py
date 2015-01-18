from main import *
import main
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
import urllib

class Movement(ndb.Model):
  name = ndb.StringProperty(required=True)
  pose = ndb.StringProperty(required=True)

class ExerciseTrack(ndb.Model):
  timestamp = ndb.DateTimeProperty(required=True)
  ETID = ndb.StringProperty(required=True)
  pass
  #TODO: IMPLEMENT WITH LISTS -- exercise list

class Result(ndb.Model):
  user = ndb.UserProperty(required=True)
  timestamp = ndb.DateTimeProperty(required=True)
  ETID = ndb.StringProperty(required=True)
  #TODO: IMPLEMENT WITH LISTS -- exercise result list for each day

class PTUser(ndb.Model):
  user = ndb.UserProperty(required=True)
  PTType = ndb.StringProperty(required=True)
  therapist = ndb.UserProperty()

class ExercisesHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.userID == users.get_current_user().user_id())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = main.jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))

class ProgressHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.userID == users.get_current_user().user_id())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = main.jinja_environment.get_template('progress.html')
    self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(loader=
  jinja2.FileSystemLoader(os.path.dirname(__file__)))

class TrackHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.userID == users.get_current_user().user_id())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = main.jinja_environment.get_template('createTrack.html')
    self.response.out.write(template.render(template_values))
