#!/usr/bin/env python
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

class WelcomeHandler(webapp2.RequestHandler):
  """Handler for / and to filter the three personas"""
  def get(self):
    self.response.out.write(template.render('views/welcome.html', {}))

class DevHandler(webapp2.RequestHandler):
  """Handler for the Dev persona"""
  def get(self):
    #get page number
    p = self.request.get('p')
    p = int(p)
    persona = "devs"
    if p == 1:
      topic = "What is App Engine?"
      title = "Where do you want to deploy your app?"
      self.response.out.write(template.render('views/dev1.html', {'page' : p, 'persona' : persona,'title' : title, 'topic' : topic}))
    elif p == 2:
      topic = "Guestbook Application"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
      self.response.out.write(template.render('views/dev2.html', {'page' : p, 'persona' : persona,'title' : title, 'topic' : topic}))
    elif p == 3:
      topic = "Deploying an App"
      title = "Type the command \"ls\" into the terminal."
    elif p == 4:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
    elif p == 5:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."

class OpsHandler(webapp2.RequestHandler):
  """Handler for the Ops persona"""
  def get(self):
    #get page number
    p = self.request.get('p')
    p = int(p)
    persona = "ops"
    html_page = ''
    if p == 1:
      topic = "Deploy Your App"
      title = "Where do you want to deploy your app?"
      html_page = 'views/ops1.html'
    elif p == 2:
      topic = "Monitor Your App"
      title = ""
      html_page = 'views/ops2.html'
    elif p == 3:
      topic = "Managing Your App From the Command Line"
      title = "Type the command \"ls\" into the terminal."
      html_page = 'views/ops3.html'
    elif p == 4:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
      html_page = 'views/ops4.html'
    elif p == 5:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
      html_page = 'views/ops5.html'
    else:
      #return to main persona page
      self.redirect('/')
      return
    self.response.out.write(template.render(html_page, {'page' : p, 'persona' : persona,'title' : title, 'topic' : topic}))

class BusinessHandler(webapp2.RequestHandler):
  #get page number
  def get(self):
    p = self.request.get('p')
    p = int(p)
    persona = "bus"
    html_page = ""
    if p == 1:
      topic = "Flex Data"
      title = ""
      html_page = "views/bus1.html"
    elif p == 2:
      topic = "Flex Bill"
      title = "Budget flexibility blah blah with your AppScale deployment."
      html_page = "views/bus2.html"
    elif p == 3:
      topic = "Deploying an App"
      title = "Type the command \"appscale deploy \'path to your app\'\" into the terminal to deploy your app on AppScale."
    elif p == 4:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
    elif p == 5:
      topic = "Registering Appscale"
      title = "Type the \"some command\" command into the terminal to start register your appscale instance."
    self.response.out.write(template.render(html_page, {'page' : p, 'persona' : persona, 'title' : title, 'topic' : topic}))




app = webapp2.WSGIApplication([
                               ('/', WelcomeHandler),
                               ('/devs', DevHandler),
                               ('/ops', OpsHandler),
                               ('/bus', BusinessHandler)
                               ], debug=True)
