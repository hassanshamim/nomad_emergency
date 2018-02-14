PROJECT_NAME = nomad_emergency


deploy:
	git push heroku master:master

test:
	py.test

run:
	heroku local web

remote-shell:
	heroku run bash
