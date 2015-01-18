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
  complete = ndb.StringProperty(repeated=True)
  incomplete = ndb.StringProperty(repeated=True)

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

    etQuery = ExerciseTrack.query().filter(currUser.user == ExerciseTrack.user)
    etQuery.order(ExerciseTrack.timestamp)
    track = etQuery.fetch()
    if not track:
      template_values['numProgs'] = 0
    else:
      template_values['program'] = track[0].exProgram

    #TODO: parse and send program to javascript

    template = main.jinja_environment.get_template('patientPage.html')
    self.response.out.write(template.render(template_values))

class ProgressHandler(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}

    patientID = self.request.get('pid')
    if not patientID:
      patientUser = users.get_current_user()
    else:
      patientUser = users.User(_user_id = 'validuserid')
    template_values["pid"] = patientID
    logging.info(patientID)

    #TODO: load data specific for this patient ID from the results datastore model
    rQuery = Result.query().filter(Result.user == patientUser)
    rQuery.order(ExerciseTrack.timestamp)
    patientResults = rQuery.fetch()
    if not patientResults:
      template_values['results'] = []
    else:
      template_values['results'] = patientResults

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
    template = main.jinja_environment.get_template('therapistPage.html')

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

class ResultRecorder(webapp2.RequestHandler):
  def get(self):
    query = PTUser.query().filter(PTUser.user == users.get_current_user())
    currUser = query.fetch()[0]
    renderedHeader = header.getHeader(currUser.PTType)
    template_values = {"header": renderedHeader, "footer":header.getFooter()}

    hits = self.request.get('complete')
    misses = self.request.get('incomplete')

    complete = hits.split(",")
    incomplete = misses.split(",")

    r = Result(user=users.get_current_user(), timestamp=datetime.datetime.now(), complete=complete, incomplete=incomplete)
    r.put()

