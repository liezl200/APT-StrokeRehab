from main import *
import main
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
import urllib

class ExercisesHandler(webapp2.RequestHandler):
  def get(self):
    renderedHeader = header.getHeader(users.get_current_user().user_id())
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(loader=
  jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ProgressHandler(webapp2.RequestHandler):
  def get(self):
    renderedHeader = header.getHeader(users.get_current_user().user_id())
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('progress.html')
    self.response.out.write(template.render(template_values))

class TrackHandler(webapp2.RequestHandler):
  def get(self):
    renderedHeader = header.getHeader(users.get_current_user().user_id())
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('createTrack.html')
    self.response.out.write(template.render(template_values))
