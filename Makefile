check:
	pre-commit run --show-diff-on-failure --color=always --all-files

test:
	docker exec -i web pytest -v tests/

up:
	docker-compose up -d --build

reload:
	docker-compose down && docker-compose up -d --build

logs:
	docker logs web --follow

exec:
	docker exec -it web bash
