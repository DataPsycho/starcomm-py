.PHONY: post serve buildd served killd

app_name = starcomm-py:latest

post:
	curl -X POST -H "Content-Type: application/json" -d '{"from": "Saru", "message": "Saru to Discovery. Over!"}' http://0.0.0.0:8080/discovery

serve:
	clear
	bash ./gunicorn_starter.sh

buildd:
	docker build -t $(app_name) .

served:
	sudo docker run --detach -p 8080:8080 $(app_name)


killd:
	@echo 'Killing container...'
	docker ps | grep $(app_name) | awk '{print $$1}' | xargs -r docker stop


removed:
	docker ps -a | grep $(app_name) | awk '{print $$1}' | xargs docker rm