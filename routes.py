from flask import url_for, render_template, redirect

from app import app
from forms import MainForm
import persist


@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
    form = MainForm()
    if form.validate_on_submit():
        x = persist.add(form.recording_url)
        return redirect(f"/thankyou/{x}")
    return render_template("index.html", form=form)


@app.route("/thankyou/<friendly>", methods=['GET'])
def thanks(friendly):
    return render_template("thankyou.html", context={'friendly': friendly})
