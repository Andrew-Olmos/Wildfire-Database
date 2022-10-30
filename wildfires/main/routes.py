from flask import render_template, request, Blueprint, redirect, url_for
from wildfires.main.forms import SearchForm
from flask_googlemaps import Map
from flask_cors import CORS, cross_origin

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@cross_origin()
def home():    
    form = SearchForm()
    query = ""
    if form.validate_on_submit():
        query = form.search.data
        #return redirect(url_for("main.search", query=query, page=1))
    return render_template("home.html", form=form, query=query)


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
