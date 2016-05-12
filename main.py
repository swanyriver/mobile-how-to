#!/usr/bin/env python

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)



class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    Hotestlisting = getListing() or errorListing()

    listingQuery = Listing.query(ancestor=ndb.Key('Listing',LISTINGS_KEY)).order(-Listing.timeAdded)
    listings = listingQuery.fetch()

    templateVars = {
      'Hotestlisting':Hotestlisting,
      'listings':listings
    }

    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(templateVars))

    


app = webapp2.WSGIApplication([
    webapp2.Route('/*', MainPage),
], debug=True)

