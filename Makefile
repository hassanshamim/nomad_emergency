PROJECT_NAME = nomad_emergency


deploy:
	git push heroku master:master
	heroku run python emergency/manage.py migrate
	heroku run python emergency/manage.py populate_languages --clear

test:
	py.test

run:
	heroku local web
