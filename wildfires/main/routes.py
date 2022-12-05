from flask import render_template, request, Blueprint, redirect, url_for
from wildfires.main.forms import SearchForm
from flask_googlemaps import Map
from flask_cors import CORS, cross_origin
from wildfires.models import Fire

main = Blueprint("main", __name__)

ROWS_PER_PAGE = 10
@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@cross_origin()
def home():    
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    fires = Fire.query.filter_by(FIRE_YEAR='2011').paginate(page=page, per_page=ROWS_PER_PAGE)
    if form.validate_on_submit():
        state = form.state.data
        fires = Fire.query.filter((Fire.FIRE_YEAR == '2011'), (Fire.STATE == state)).paginate(page=page, per_page=ROWS_PER_PAGE)
        return render_template("home.html", form=form, fires=fires)
    return render_template("home.html", form=form, fires=fires)


@main.route("/search/", methods=["GET", "POST"])
def searchHome():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data
        return redirect(url_for("main.search", query=query, page=1))
    return render_template(
        "search.html",
        form=form,
    )


@main.route("/about")
def about():
    return render_template("about.html", title="About")
