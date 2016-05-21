#!/usr/bin/env python

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

PAGES = [
  ("", "/"),
  ("Primitive Data", "simple.html"),
  ("Passing Objects", "objects.html"),
  ("Use Global Reference", "global.html"),
  ("Avoid Using Activities", "avoid.html")
]


class MainPage(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    template = self.request.path[1:]
    if not template:
      template = "index.html"
      var = {"pages": PAGES, "pageIndex":0}
    else:
      var = {"pages": PAGES, "pageIndex": [x[1] for x in PAGES].index(template)}

    self.response.headers['Content-Type'] = 'text/html'
    jTemplate = JINJA_ENVIRONMENT.get_template(template)
    self.response.write(jTemplate.render(var))


app = webapp2.WSGIApplication([
    webapp2.Route(r'/<:.*>', handler=MainPage),
], debug=True)

