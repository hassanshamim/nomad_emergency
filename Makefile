PROJECT_NAME = nomad_emergency


deploy:
	git push heroku heroku-prep:master

test:
	py.test

run:
	heroku local web
