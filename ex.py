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
  user = ndb.UserProperty(required=True)
  exProgram = ndb.StringProperty(repeated=True)
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
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer": header.getFooter()}
    template = main.jinja_environment.get_template('exercises.html')
    self.response.out.write(template.render(template_values))

class ProgressHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}

    patientID = self.request.get('pid')
    if not patientID:
      patientID = users.get_current_user().user_id()
    template_values["pid"] = patientID
    logging.info(patientID)
    #TODO: load data specific for this patient ID from the results datastore model

    template = main.jinja_environment.get_template('progress.html')
    self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(loader=
  jinja2.FileSystemLoader(os.path.dirname(__file__)))

class TrackHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}

    patientID = self.request.get('pid')
    template_values["pid"] = patientID
    template = main.jinja_environment.get_template('createTrack.html')

    self.response.out.write(template.render(template_values))

class IntermHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    #get and enter exercise plan into data base
    activities = self.request.get('activities')
    patientID = self.request.get('pid') #TODO : do something with patientID

    #turn activities into an array
    exprog = activities.split(',')

    #add to user's history of exercise programs
    new_plan = ExerciseTrack(timestamp = datetime.datetime.now(), user = users.get_current_user(),
                              exProgram = exprog)
    new_plan.put()

    template_values = {"header": renderedHeader, "footer":header.getFooter(), "planVals": exprog}
    template = main.jinja_environment.get_template('interm.html')
    self.response.out.write(template.render(template_values))

