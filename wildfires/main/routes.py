from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
from wildfires.main.forms import SearchForm, LoginForm, RegisterForm
from flask_googlemaps import Map
from flask_cors import CORS, cross_origin
from wildfires.models import Fire, NWCGUnit, Users
from sqlalchemy import text
from wildfires import login_manager, db
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
#


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@main.route("/", methods=["GET", "POST"])
@main.route("/login", methods=["GET", "POST"])
# @cross_origin()
def login():
    form = LoginForm()
    csrf_token = form.csrf_token
    if form.validate_on_submit():
        print("Post Method")
        # data = request.get_json()
        # print("request")
        user = Users.query.filter_by(username=form.username.data).first()
        print("User: ", user)
        print(form.password.data)
        check = check_password_hash(user.password, form.password.data)
        print(check)
        if user is None or not check:
            flash('Invalid username or password', 'error')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.home', form=form, csrf_token=csrf_token))
    else:
        return render_template('login.html', form=form)

# @main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@cross_origin()
@login_required
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
    return render_template("home.html", user = current_user.name, form=form)



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


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, 10)
        new_user = Users(username=form.username.data, name=form.name.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)
