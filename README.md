## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`poetry`](https://github.com/python-poetry/poetry) (**required**)
- [`pre-commit`](https://pre-commit.com/) (**required**)
- `pycharm 2017+` or `vscode`

## Development in a Docker container

- Create `.env` file. (use [`.env.template`](https://gitlab.proninteam.ru/fastapi/fastapi-application/-/blob/development/environment/.env.template) as example)
- Run `docker-compose up -d --build`
