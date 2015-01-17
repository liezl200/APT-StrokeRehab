import urllib2
import json
header = '''
<header class="navbar navbar-static-top bs-docs-nav" id="top" role="banner" style="background-color:rgba(2,132,130,0.7); z-index: 9;">
  <div class="container">
    <div class="navbar-header">
      <a href="../" class="navbar-brand">APT</a>
    </div>
    <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
      <ul class="nav navbar-nav" >
        <<PATIENT/THERAPIST>>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="/Logout">LOGOUT</a></li>
      </ul>
    </nav>
  </div>
</header>
'''

patientHeader = '''
<li><a href="/progress">PROGRESS</a></li>
<li><a href="/exercises">EXERCISES</a></li>
'''

therapistHeader = '''
<li><a href="/dashboard">DASHBOARD</a></li>
'''

footer = '''
<script src="/static/bootstrap.min.js"></script>
'''

def getHeader(isPatient):
  if isPatient:
    return string.replace(header, "<<PATIENT/THERAPIST>>", patientHeader)
  else:
    return string.replace(header, "<<PATIENT/THERAPIST>>", therapistHeader)


def getFooter(pageRoute="/"):
  return footer