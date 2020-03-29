from app import app

@app.route('/')
@app.route('/index')
def index():
    return "You must have Clothes."
