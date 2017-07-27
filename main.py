import os, sys, cherrypy, jinja2, datetime

if __name__ == "__main__":
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("public/html"))



    #Helper Classes
    class tournament():
        def __init__(self, name, date, first, second, third, prize="", challonge=""):
            self.name = name
            self.date_obj = date
            self.date = date.strftime("%d %B %Y")
            self.first = first
            self.second = second
            self.third = third
            self.prize = prize
            self.challonge = challonge

    class regulation():
        def __init__(self, title, link, active):
            self.title = title
            self.link = link
            self.active = active

    class officer():
        def __init__(self, name, position):
            self.name = name
            self.position = position



    #Home Page
    class home():
        tourneys = [
        tournament("Monotype", datetime(2015,11,20,0,0), "Nick Boyd", "Rianna \"the Bops\" Nandan", "Ty Garcia", challonge="http://challonge.com/sjsumonotypefall2015"),
        tournament("Cute", datetime(2016, 3, 18,0,0), "Shayda Sophia", "Javier Ayala", "Brenna Botzheim"),
        tournament("NU", datetime(2016, 3, 4,0,0), "Javier Ayala", "Claude Michel", "Will Giallo", challonge="http://challonge.com/sjsunuspring2016"),
        tournament("Gen 1", datetime(2016, 2, 26,0,0), "Manuel Saucedo", "Javier Ayala", "Will Giallo"),
        tournament("Team Battle", datetime(2016, 2, 19,0,0), "Shayda Sophia and Alex Vargas", "Tad Mikasa and Rianna \"the Bops\" Nandan", "Will Giallo and Joe Giallo"),
        tournament("OU", datetime(2016, 2, 5,0,0), "Javier Ayala", "Tad Mikasa", "Ty Garcia"),
        tournament("Halloween", datetime(2015, 10, 30,0,0), "Javier Ayala", "Tad Mikasa", "Chris Ngai"),
        tournament("Little Cup", datetime(2015, 10, 16,0,0), "Nick Boyd", "Shayda Sophia", "Will Giallo and Alex Vargas - tied"),
        tournament("Draft", datetime(2015, 10, 2,0,0), "Yair", "Tad Mikasa", "Chris Ngai"),
        tournament("Monochrome", datetime(2015, 9, 18,0,0), "Eduardo", "Javier Ayala", "Alex Nguyen"),
        tournament("OU", datetime(2015, 9, 4,0,0), "Javier Ayala", "Chris Ngai", "Shayda Sophia"),
        tournament("OU", datetime(2015, 4, 24,0,0), "Jason Yan", "Khalia Flores", "NA"),
        tournament("VGC", datetime(2015, 4, 8,0,0), "Sergio Camacho", "Javier Ayala", "Jason Yan"),
        tournament("Little Cup", datetime(2015, 3, 13,0,0), "Shayda Sophia", "Tad Mikasa", "Jose Madrid"),
        tournament("Never Used", datetime(2015, 2, 25,0,0), "Jose Madrid", "Jason Yan", "James Escoto"),
        tournament("OU Draft", datetime(2016, 4, 22,0,0), "Chris Ngai", "Tad Mikasa", "Ty Garcia", challonge="http://challonge.com/2016SpringDraftTournament"),
        tournament("Monotype", datetime(2016, 5, 6,0,0), "Rianna \"the Bops\" Nandan", "Shayda Sophia", "Alex Vargas", challonge="http://challonge.com/2016springmonotypetourney"),
        tournament("OU", datetime(2016, 6, 9,0,0), "Tad Mikasa", "Raymond", "Joe Giallo", challonge="http://challonge.com/SJSUOUTOURNEY2016FALL"),
        tournament("Teambuilder", datetime(2016, 6, 23,0,0), "Shashwath", "Jordan", "Javier Ayala", challonge="http://challonge.com/TBTSJSUF2016"),
        tournament("Draft", datetime(2016, 10, 14,0,0), "Will Giallo", "Chris Ngai", "Nick Boyd", challonge="http://challonge.com/DraftTourneyF2016"),
        tournament("Halloween", datetime(2016, 10, 28,0,0), "Raymond", "Tad Mikasa", "Rianna \"the Bops\" Nandan", challonge="http://challonge.com/HALLOWTOURNEYF2016"),
        tournament("Find a Friend", datetime(2016, 11, 4,0,0), "Will and Shayda", "Tad and Mitchell", "Sean and Claude", challonge="http://challonge.com/TT2016F"),
        tournament("Monotype", datetime(2016, 12, 2,0,0), "Rianna \"the Bops\" Nandan", "Nick Boyd", "Yair Aragundi", challonge="http://challonge.com/MonotypeFall16"),
        tournament("Team Rocket", datetime(2017, 2, 3,0,0), "Nick Boyd", "Will Giallo", "Ed Martinez", challonge="http://challonge.com/SJSUTR2017")
        ]

        regulations = [
        regulation("Club Tournament Regulations","https://docs.google.com/document/d/1d5JiFS_6BsYqIfMRnN7J20UPxzovNyXQ179j2T9YVAo/edit", False),
        regulation("Contest Tournament","https://docs.google.com/document/d/1q15GqdMIj3aiA3s64VkQRVKDJdbry0dsh2YZKelb9-w/edit", False),
        regulation("Favorite Pokemon","https://docs.google.com/document/d/1Oi0WhzGesphmcFN4FWQk3DlJ_i-x3mFZZkVdVatRvUY/edit", False),
        regulation("Generation 1 Tournament","https://docs.google.com/document/d/1asPIVJJLAUJJiKZlfovNGp2ehuDs6oCmmeJPLhWHY4s/edit", False),
        regulation("Gym Regulations","https://docs.google.com/document/d/1Je7YDFOZtfAMwj9iELk-ZcIArCQJhAHKByBCUE3LpP8/edit", False),
        regulation("Halloween","https://docs.google.com/document/d/1kdOmbO2ed2YTkEWv-oe2aD2rwAo8_nDSpQfgplIk11Q/edit", False),
        regulation("Little Cup","https://docs.google.com/document/d/1sNPHsBBkmCBHNQLbrE-WLu5uuDwA5Oyhmx1jOtJuBbA/edit", True),
        regulation("Monochrome","https://docs.google.com/document/d/1MnnYwcmwCZFYDc8qf3UPaj0jVnhD3KL0PWoVMHKAZMA/edit", False),
        regulation("Monotype","https://docs.google.com/document/d/1ulhvToTeYAy1GK7jaNPlTNUXa0mrdtygj-FVAzwTWbc/edit", True),
        regulation("Never Used","https://docs.google.com/document/d/1t2TIuIz8kkz1UFA50STbpuc72n7OTxB5QyCEgK0dJI8/edit", False),
        regulation("Not Fully Evolved (NFE)","https://docs.google.com/document/d/16WUmQfOOjksfjkBVevBS6zxz-WQMPxaMDuFM2I60yBE/edit", False),
        regulation("Over Used","https://docs.google.com/document/d/1mxHoxztFC5nWjzU5sLomVmFZQwlAuMvnmReiOkP_9UM/edit", False),
        regulation("OU Draft","https://docs.google.com/document/d/1T3W_VsrZBEPngOdFnJU531By72sBjATPef9AJI8EqXs/edit", False),
        regulation("Point Buy","https://docs.google.com/document/d/1lA4bK2z5ehU4_DO4AIOXAg_KCDmZQhADB3qD9CIvUnA/edit", True),
        regulation("Saint Patrick's Day","https://docs.google.com/document/d/1_rzUVCSVMF6zN453l3auAjTzqyM1_xTijDxDn_bYFpA/edit", True),
        regulation("Steal Yo Pokes","https://docs.google.com/document/d/1ZG0CCfdZwnkK6p_ZYIM5b1Xj0k8-9G2vjd0VgxspGjo/edit", False),
        regulation("Team Battle","https://docs.google.com/document/d/108gnHE_Gacj8aEkdSt4mY-PZ8TWHTXd3OgxQKuD2hJY/edit", False),
        regulation("Team Builder","https://docs.google.com/document/d/13gWOnTRv6mcjoqAslxa7VeBM2vB-F7GO71SIeMkHTwQ/edit", False),
        regulation("Team Rocket","https://docs.google.com/document/d/1ZG0CCfdZwnkK6p_ZYIM5b1Xj0k8-9G2vjd0VgxspGjo/edit", True),
        regulation("Tier Rotation","https://docs.google.com/document/d/1VDKwWH9FjWv3UZbCMwIKAl7WNDnhSH1r0g5KxEymAxY/edit", False),
        regulation("Ubers","https://docs.google.com/document/d/1o7C7RdxOGGt6tnWpyowq78-1ILPYIHmScMluaPHizxo/edit", False),
        regulation("VGC","https://docs.google.com/document/d/1czvrFG9eMvloleFIT8Pn0X_mPWgTRZi4SRsPfecjjeY/edit", True)
        ]
        for reg in regulations:
            if not reg.active:
                regulations.remove(reg)
        for reg in regulations:
            if not reg.active:
                regulations.remove(reg)
        for reg in regulations:
            if not reg.active:
                regulations.remove(reg)

        officers = [
        ["Spring 2017: Another New Game", officer("Khaila Zherine Flores", "President"), officer("William Giallo", "Vice President"), officer("Jason Yan", "Treasurer"), officer("Kevin Nguyen", "Secretary"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Social Media Manager"),officer("Patrick Rettinhouse", "Intern")],
        ["Fall 2016: Steeling the Sun", officer("Khaila Zherine Flores", "President"),officer("William Giallo", "Vice President"),officer("Jason Yan", "Treasurer"),officer("Shayda Sophia", "Secretary"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Rianna Nandan", "Historian"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Media Manager")],
        ["Spring 2016: Dawn of the Pokemon League", officer("Khaila Zherine Flores", "President"),officer("William Giallo", "Vice President"),officer("Jose Madrid", "Treasurer"),officer("Shayda Sophia", "Secretary"),officer("Alex Nguyen", "Publicist"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Javier Ayala-Mora", "Historian"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Media Manager")],
        ["Fall 2015: The Great Expansion", officer("Khaila Zherine Flores", "President"), officer("James Escoto", "President"), officer("Jose Madrid", "Treasurer"), officer("Shayda Sophia", "Secretary"),officer("Alex Nguyen", "Publicist"), officer("Nick Boyd", "Web Master"), officer("Jason Yan", "Jr. Web Master"), officer("Javier Ayala-Mora", "Historian"), officer("Tad Mikasa", "Event Coordinator")],
        ["Spring 2015: New Game", officer("Khaila Zherine Flores", "President"), officer("James Escoto", "President"), officer("Jose Madrid", "Treasurer"), officer("Nick Boyd", "Secretary"), officer("Alex Nguyen", "Publicist")]
        ]

        @cherrypy.expose
        def index(self):
            challonge_link = ""
            for x in sorted(self.tourneys, key=lambda date: date.date_obj, reverse=True):
                if x.challonge != "":
                    challonge_link = x.challonge
                    break
            return env.get_template("home.html").render(tournaments=sorted(self.tourneys, key=lambda date: date.date_obj, reverse=True), regulations=sorted(self.regulations), officers=self.officers, c_link=challonge_link)

    conf = {
        '/':{
            'tools.sessions.on':True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
        '/static':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir': 'public'
            }
    }

    cherrypy.tree.mount(home(), "/", conf)
    #cherrypy.tree.mount(view.dex(), "/dex", conf)
    #cherrypy.tree.mount(view.calc(), "/calc", conf)
    #cherrypy.tree.mount(view.gym_leaders(), "/gyms", conf)

    cherrypy.config.update({
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 80,
            })

    cherrypy.engine.start()
    cherrypy.engine.block()
