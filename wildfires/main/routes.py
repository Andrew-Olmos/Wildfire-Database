from flask import render_template, request, Blueprint, redirect, url_for
from wildfires.main.forms import SearchForm
from flask_googlemaps import Map
from flask_cors import CORS, cross_origin
from wildfires.models import Fire, NWCGUnit
from sqlalchemy import text

main = Blueprint("main", __name__)


# @main.route('/login', methods=['GET', 'POST'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		username = request.form['username']
# 		password = request.form['password']
# 		# Check the username and password against the database here
# 		# If they match, redirect the user to the home page
# 		# If they don't match, set an error message
#         return redirect(url_for('home.html'))
# 		error = 'Invalid username or password'
# 	return render_template('login.html', error=error)

# @main.route("/", methods=["GET", "POST"])
# @main.route("/login", methods=["GET", "POST"])
# @cross_origin()
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']



# @main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@cross_origin()
def home():    
    form = SearchForm()
    if form.validate_on_submit():
        startYear = form.startYear.data
        endYear = form.endYear.data
        state = form.state.data
        rows = form.rows.data
        sort = form.sort.data
        order = form.order.data
        
        return redirect(url_for('main.searchHome', page=1, startYear=startYear, endYear=endYear, state=state, rows=rows, sort=sort, order=order))
    return render_template("home.html", form=form)



@main.route("/search/<sort>/<order>", methods=["GET", "POST"])
@cross_origin()
def searchHome(sort, order, state='', startYear=1992, endYear=1992, rows=1, page=1):    
    form = SearchForm()
    state = request.args.get('state', '', type=str)
    page = request.args.get('page', 1, type=int)
    rows = request.args.get('rows', 1, type=int)
    startYear = request.args.get('startYear', 1992, type=int)
    endYear = request.args.get('endYear', 1992, type=int)

    if(len(state) < 1):
        fires = Fire.query.filter((Fire.FIRE_YEAR >= startYear), (Fire.FIRE_YEAR <= endYear)).order_by(text(f'{sort} {order}')).paginate(page=page, per_page=rows)
    else:
        fires = Fire.query.filter((Fire.FIRE_YEAR >= startYear), (Fire.FIRE_YEAR <= endYear), (Fire.STATE == state)).order_by(text(f'{sort} {order}')).paginate(page=page, per_page=rows)
    markers = []
    for fire in fires.items:
        markers.append({
                            'icon': '/static/icons/fire_icon.png',
                            'lat':  fire.LATITUDE,
                            'lng':  fire.LONGITUDE,
                            'infobox': f"ID: {fire.FPA_ID} | Name: {fire.FIRE_NAME} | SIZE: {fire.FIRE_SIZE} | Cause: {fire.STAT_CAUSE_DESCR}"
                        })
    return render_template("search.html", form=form, fires=fires, markers=markers, startYear=startYear, endYear=endYear, rows=rows, state=state, sort=sort, order=order)


@main.route("/fire/<ID>", methods=["GET", "POST"])
@cross_origin()
def fire(ID):    
    fire = Fire.query.filter((Fire.FPA_ID == ID)).first()
    NWCG_Unit = NWCGUnit.query.filter((NWCGUnit.UnitId == fire.NWCG_REPORTING_UNIT_ID)).first()
    Lat = fire.LATITUDE
    Long = fire.LONGITUDE
    markers =   [{
                    'icon': '/static/icons/fire_icon.png',
                    'lat':  Lat,
                    'lng':  Long,
                    'infobox': f"ID: {fire.FPA_ID} | Name: {fire.FIRE_NAME} | SIZE: {fire.FIRE_SIZE} | Cause: {fire.STAT_CAUSE_DESCR}"
                }]
    return render_template("fire.html", fire=fire, markers=markers, NWCG_Unit=NWCG_Unit, Lat=Lat, Long=Long)



@main.route("/about")
def about():
    return render_template("about.html", title="About")
