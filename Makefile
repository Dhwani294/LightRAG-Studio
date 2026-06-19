run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy .

docker:
	docker compose up --build