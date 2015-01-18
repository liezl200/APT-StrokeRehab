import urllib2
import json
header = '''
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
<div class="container">
  <div class="navbar-header page-scroll">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand page-scroll" href="/">
          Automated Physical Therapy</a>
      </div>
      <div class="collapse navbar-collapse navbar-ex1-collapse">
      <ul class="nav navbar-nav" >
        <li>
            <a class="page-scroll" href="/#about">ABOUT</a>
        </li>
        <li>
            <a class="page-scroll" href="/#contact">CONTACT</a>
        </li>
        <<PATIENT/THERAPIST>>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="/settings">SETTINGS</a></li>
        <li><a href="/Logout">LOGOUT</a></li>
      </ul>
    </div>
    <!-- /.navbar-collapse -->
  </div>
  <!-- /.container -->
</nav>
'''

homeHeader = '''
<!-- Navigation -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
    <div class="container">
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand page-scroll" href="#page-top">
            Automatic Physical Therapy</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
            <ul class="nav navbar-nav">
                <li class="hidden">
                    <a class="page-scroll" href="#page-top"></a>
                </li>
                <li>
                    <a class="page-scroll" href="#about">ABOUT</a>
                </li>
                <li>
                    <a class="page-scroll" href="#contact">CONTACT</a>
                </li>
                <<PATIENT/THERAPIST>>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="/settings">SETTINGS</a></li>
              <li><a href="/Logout">LOGOUT</a></li>
            </ul>
        </div>
        <!-- /.navbar-collapse -->
    </div>
    <!-- /.container -->
</nav>
'''

patientHeader = '''
<li><a href="/progress">PROGRESS</a></li>
<li><a href="/exercises">EXERCISES</a></li>
'''

therapistHeader = '''
<li><a href="/dashboard">THERAPIST DASHBOARD</a></li>
'''

footer = '''
<script src="/static/bootstrap.min.js"></script>
'''

def getHeader(userType):
  # Patient Type
  if userType == "Patient":
    return header.replace("<<PATIENT/THERAPIST>>", patientHeader)
  elif userType == "Therapist":
    return header.replace("<<PATIENT/THERAPIST>>", therapistHeader)
  else:
    return header.replace("<<PATIENT/THERAPIST>>", "")

def getHomeHeader(userType):
  # Patient Type
  if userType == "Patient":
    return homeHeader.replace("<<PATIENT/THERAPIST>>", patientHeader)
  elif userType == "Therapist":
    return homeHeader.replace("<<PATIENT/THERAPIST>>", therapistHeader)
  else:
    return homeHeader.replace("<<PATIENT/THERAPIST>>", "")

def getFooter(pageRoute="/"):
  return footer