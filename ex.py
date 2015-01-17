from main import *
import main
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
import urllib

class ExercisesHandler(webapp2.RequestHandler):
	def get(self):
		renderedHeader = header.getHeader(currUser == "Patient")
		template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))

class ProgressHandler(webapp2.RequestHandler):
	def get(self):
		renderedHeader = header.getHeader(currUser == "Patient")
		template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))

class TrackHandler(webapp2.RequestHandler):
	def get(self):
		renderedHeader = header.getHeader(currUser == "Patient")
		template_values = {"header": renderedHeader, "footer":header.getFooter()}
    template = jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))
