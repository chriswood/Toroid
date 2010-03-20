import os
import ConfigParser
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from config import template_dir

class MainPage(webapp.RequestHandler):
    def get(self):
        greetings = 'hey man'
        template_values = {
            'greetings': greetings,
        }

        path = os.path.join(template_dir(), 'index.html')
        
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)
                                     
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
