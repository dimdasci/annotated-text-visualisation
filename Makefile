install: dirs requirements 

dirs:
	mkdir -p data src/pages src/utils

requirements:
	pip install -U pip setuptools wheel
	pip install -r requirements.txt

## Format using Black
format: 
	black src

## Lint using flake8
lint:
	flake8 src

## Docker
build: 
	docker build -t dimdasci/annotated-text-visualisation:0.2.0 .

push:
	docker push dimdasci/annotated-text-visualisation:0.2.0
	