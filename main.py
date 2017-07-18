import cherrypy
import setup, os, sys, view

if "__main__" == __name__:
    setup.init()
    conf = {
        '/':{
            'tools.sessions.on':True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir': './public'
        }
    }

    cherrypy.tree.mount(view.home(), "/", conf)
    #cherrypy.tree.mount(view.dex(), "/dex", conf)
    #cherrypy.tree.mount(view.calc(), "/calc", conf)
    #cherrypy.tree.mount(view.gym_leaders(), "/gyms", conf)

    cherrypy.config.update({
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
            })

    cherrypy.engine.start()
    cherrypy.engine.block()
