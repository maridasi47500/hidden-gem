from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (phone,country_id,password,username,email,pic) values (:phone,:country_id,:password,:username,:email,:pic)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['phone','country_id','password','username','email','pic']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['phone','country_id','password','username','email','pic']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['phone','country_id','password','username','email','pic']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (country_id,name) values (:country_id,:name)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_off_the_beaten_track_photos", methods=["GET","POST"])
def add_one_off_the_beaten_track_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into off_the_beaten_track_photos (city_id,pic,user_id,description) values (:city_id,:pic,:user_id,:description)",hey)
        user = query_db('select * from off_the_beaten_track_photos')

        return render_template("off_the_beaten_track_photosform.html", off_the_beaten_track_photoss=user, one_user=one_user, the_title="add new off_the_beaten_track_photos", touslescity=touslescity, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    user = query_db('select * from off_the_beaten_track_photos')
    one_user = query_db("select * from off_the_beaten_track_photos limit 1", one=True)
    return render_template("off_the_beaten_track_photosform.html", off_the_beaten_track_photoss=user, one_user=one_user, the_title="add new off_the_beaten_track_photos", touslescity=touslescity, touslesuser=touslesuser)

@app.route("/add_one_gem_place_photos", methods=["GET","POST"])
def add_one_gem_place_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into gem_place_photos (city_id,pic,user_id,description) values (:city_id,:pic,:user_id,:description)",hey)
        user = query_db('select * from gem_place_photos')

        return render_template("gem_place_photosform.html", gem_place_photoss=user, one_user=one_user, the_title="add new gem_place_photos", touslescity=touslescity, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    user = query_db('select * from gem_place_photos')
    one_user = query_db("select * from gem_place_photos limit 1", one=True)
    return render_template("gem_place_photosform.html", gem_place_photoss=user, one_user=one_user, the_title="add new gem_place_photos", touslescity=touslescity, touslesuser=touslesuser)

@app.route("/add_one_local_souvenir", methods=["GET","POST"])
def add_one_local_souvenir():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into local_souvenir (name,city_id,pic,user_id) values (:name,:city_id,:pic,:user_id)",hey)
        user = query_db('select * from local_souvenir')

        return render_template("local_souvenirform.html", local_souvenirs=user, one_user=one_user, the_title="add new local_souvenir", touslescity=touslescity, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    user = query_db('select * from local_souvenir')
    one_user = query_db("select * from local_souvenir limit 1", one=True)
    return render_template("local_souvenirform.html", local_souvenirs=user, one_user=one_user, the_title="add new local_souvenir", touslescity=touslescity, touslesuser=touslesuser)

