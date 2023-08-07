start:
	python 

build-docker:
	docker build -t sum-testing .  

run-docker:
	docker run --rm -it -p 6566:6566 -p 5000:5000 -v /Users/giuseppepitruzzella/PepperGateway/Gateway/:/app/ --name summarium sum-testing