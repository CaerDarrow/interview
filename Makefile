PORT=80

.PHONY: build
build:
	@echo "$@"
	@docker build -t backend .


.PHONY: run
run: build
	@echo "$@ on $(PORT)"
	@docker run -it -p 80:$(PORT) backend

.PHONY: stop
stop:
	@docker stop $(docker ps -q)