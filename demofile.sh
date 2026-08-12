
mkdir templates 
python3 scaffold.py user phone country_id:references password username email pic:file
python3 scaffold.py country name
python3 scaffold.py city country_id:references name
python3 scaffold.py off_the_beaten_track_photos city_id:references pic:file user_id:references description
python3 scaffold.py gem_place_photos city_id:references pic:file user_id:references description
python3 scaffold.py local_souvenir name  city_id:references pic:file user_id:references
