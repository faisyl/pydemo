import cherrypy
import time

SVCNAME=''

class RootServer:
    @cherrypy.expose
    def index(self, **keywords):
    	global SVCNAME
        return "{}It works! Access /sleep/<sleep-in-secs> to sleep that many seconds".format(SVCNAME)

    @cherrypy.expose
    def sleep(self, seconds=0):
    	global SVCNAME
        cherrypy.response.headers['Content-Type'] = 'text/html'
        def content(i):
            if not i: i=600
            yield("<html><body>")
            for x in range(i):
                time.sleep(1)
    		yield('<p>{}{}: {}</p>'.format(SVCNAME,time.ctime(time.time()), i-x))            
            yield("</body></html>")
        return content(int(seconds))
    sleep._cp_config = {'response.stream': True}

if __name__ == '__main__':
    import os
    CPATH = os.getenv('CERTPATH', '/run/secrets')
    ccert = os.path.join(CPATH, 'server.crt')
    ckey = os.path.join(CPATH, 'server.key')
    SVCNAME = os.getenv('SVCNAME', '')
    if SVCNAME:
        SVCNAME = "[{}]".format(SVCNAME)
    if os.path.exists(ccert):
        server_config={
            'server.socket_host': '0.0.0.0',
            'server.socket_port':443,
    
            'server.ssl_module':'pyopenssl',
            'server.ssl_certificate': ccert,
            'server.ssl_private_key': ckey,
        }
        print "Serving TLS on port 443"
    else:
        server_config={
            'server.socket_host': '0.0.0.0',
            'server.socket_port':80,
        }
        print "Serving non-TLS on port 80" 

    cherrypy.config.update(server_config)
    cherrypy.quickstart(RootServer())
