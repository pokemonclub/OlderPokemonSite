import jinja2

def init():
    global env
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["../public/html", "../public/css"]))
    global footer
    footer = env.get_template("footer.html")
    global head
    head = env.get_template("head.html")
    global home
    home = env.get_template("home.html")
    global pkmnpage
    pkmnpage = env.get_template("pokemon.html")
    global navbar
    navbar = env.get_template("navbar.html")
