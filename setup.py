import jinja2

def init():
    global env
    env = Environment(loader=FileSystemLoader("public/html"))
