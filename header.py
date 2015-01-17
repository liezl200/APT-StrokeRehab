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
        <li><a href="/dashboard">DASHBOARD</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="/Logout">LOGOUT</a></li>
      </ul>
    </nav>
  </div>
</header>
'''


footer = '''
<script src="/static/bootstrap.min.js"></script>
'''

def getHeader(pageRoute="/"):
  return header

def getFooter(pageRoute="/"):
  return footer