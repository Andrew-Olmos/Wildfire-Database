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
    if form.validate_on_submit():
        state = form.state.data
        year = form.year.data

        fires = Fire.query.filter((Fire.FIRE_YEAR == year), (Fire.STATE == state)).paginate(page=1, per_page=ROWS_PER_PAGE)
        markers = []
        for fire in fires.items:
            markers.append({
                        'icon': '/static/icons/fire_icon.png',
                        'lat':  fire.LATITUDE,
                        'lng':  fire.LONGITUDE,
                        'infobox': "Put Fire Info Here"
                    })
        return redirect(url_for('main.searchHome', page=1, year=year, state=state))
    return render_template("home.html", form=form)



@main.route("/search/<year>/<state>", methods=["GET", "POST"])
@cross_origin()
def searchHome(year, state, page=1):    
    form = SearchForm()
    page = request.args.get('page', 1, type=int)


    fires = Fire.query.filter((Fire.FIRE_YEAR == year), (Fire.STATE == state)).paginate(page=page, per_page=ROWS_PER_PAGE)
    markers = []
    for fire in fires.items:
        markers.append({
                            'icon': '/static/icons/fire_icon.png',
                            'lat':  fire.LATITUDE,
                            'lng':  fire.LONGITUDE,
                            'infobox': "Put Fire Info Here"
                        })
    return render_template("search.html", form=form, fires=fires, markers=markers)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
