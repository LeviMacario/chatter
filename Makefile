# TODO: Instalar deps do SO, ex: deps para PIL
clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

run:
	@flask run
	
help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
