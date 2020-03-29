from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sshh'
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

import routes

if __name__ == "main":
    app.run(debug=True)
