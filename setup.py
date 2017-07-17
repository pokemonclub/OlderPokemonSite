import jinja2

def init():
    global env
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("public/html"))
