lint:
	@echo "Checking flake8..."
	flake8 .

mypy:
	@echo "Checking mypy..."
	mypy .
