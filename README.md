# Seller Metrics Dashboard

An individual Django research-milestone project. It is a seller-facing analytics dashboard, not a storefront. A seller can add products and record sales; the dashboard calculates units sold, revenue, profit, inventory, and low-stock status.

## Technology choices

| Technology | Why it fits | Tradeoff |
| --- | --- | --- |
| Django | Batteries-included Python web framework: ORM, forms, templates, admin, migrations, and security features. | More structure than a minimal Flask app. |
| SQLite | Included with Python; no server setup for this prototype. | Use PostgreSQL for a deployed multi-user application. |
| `uv` | Fast Python package/project manager; makes the dependency environment reproducible. | Team members need to install one additional tool. |
| HTML/CSS | Server-rendered interface with no front-end build system. | Less dynamic than a React-style client UI. |

## Run locally

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

## Useful commands

```bash
uv add PACKAGE_NAME       # add a dependency and update uv.lock
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py test
```

## Future production direction

For deployment, change `DATABASES` to PostgreSQL, set environment-based secrets and allowed hosts, collect static files, and deploy with a production WSGI/ASGI server. A managed platform such as Render or Railway would reduce operational setup for a student project.
