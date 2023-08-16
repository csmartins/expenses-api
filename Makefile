setup:
	pipenv shell

start:
	uvicorn api.main:app --reload --host 0.0.0.0