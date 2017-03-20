import cherrypy

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def index(self):
       data = cherrypy.request.json
       print ("QUERY: " + "\"" + data['result']['resolvedQuery'] + "\"")
       print ("ACTION: " + data['result']['action'])
       print ("INTENT: " + data['result']['metadata']['intentName'])
       print ("CONTEXTS: " + data['result']['contexts'][0]['name'])


if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')
