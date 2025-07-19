run-docker:
	docker compose -f docker-compose.yaml up -d --build

down-docker:
	docker compose -f docker-compose.yaml down

pre-commit-setup:
	uv run pre-commit install

pre-commit-run:
	uv run pre-commit run --all-files --verbose --show-diff-on-failure
