.PHONY: help install lint test run

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

lint: ## Run the linter
	flake8 service --count --max-line-length=100 --statistics --exit-zero
	pylint service --max-line-length=100 --disable=R0903,W0707 --exit-zero

test: ## Run the unit tests
	nosetests

run: ## Run the service
	flask run --host=0.0.0.0 --port=8080 --reload
