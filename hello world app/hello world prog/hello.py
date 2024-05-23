import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello")

app=webapp2.WSGIApplication([(r'/', MainPage)], debug=True)

#py google-cloud-sdk\bin\dev_appserver.py C:\Users\anann\Documents\vit\TY\sem6\CC\lab\lab 1\cloudcomputing
