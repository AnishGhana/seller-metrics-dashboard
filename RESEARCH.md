# Research notes: seller metrics dashboard

## Problem and prototype scope

Our eventual team product will let sellers see metrics for products they sell. This prototype deliberately is **not** a storefront: it tracks a catalog, sales records, revenue, estimated profit, and inventory alerts.

## Framework options considered

| Option | Strengths | Limitations for this project | Decision |
| --- | --- | --- | --- |
| Django | Built-in ORM, migrations, forms, templates, admin, security defaults, and authentication. Fast to build a data-focused web app. | More conventions and files to learn. | Chosen. |
| Flask | Very small and flexible; good for a simple API or learning HTTP basics. | Requires selecting/connecting extra libraries for database models, forms, migrations, and auth. | Not chosen for this prototype. |
| FastAPI | Excellent API development, automatic documentation, and type-oriented validation. | A separate front end would be needed for a polished dashboard. | Consider later if a mobile/client API is needed. |

## Supporting technology choices

| Need | Choice | Reason |
| --- | --- | --- |
| Language | Python 3.12 | Django's primary ecosystem; readable and familiar to the team. |
| Package manager | `uv` | Creates an isolated environment, resolves dependencies, and records exact versions in `uv.lock`. |
| Development database | SQLite | Built into Python with no database server required; suitable for one-person prototype data. |
| Production database | PostgreSQL | Better concurrency, backups, and managed-host support for a deployed team app. |
| UI | Django templates plus HTML/CSS | Lets us build a functional dashboard without a separate Node/React build pipeline. |
| Testing | Django `TestCase` | Tests business rules: metric calculations and preventing overselling inventory. |

## What I learned by building the sample

- A Django project holds the configuration and top-level routes; a Django app is a focused feature module. Here, `config` is the project and `metrics` is the app.
- Models define database tables. `makemigrations` creates a versioned schema change; `migrate` applies it to the database.
- Django forms validate submitted data on the server. The sale form prevents a user from recording more units than are in inventory.
- A view receives a request, queries/models data, and renders a template. URLs map browser paths to views.
- `uv sync` creates the virtual environment and installs exactly the project dependencies. `uv add` changes the dependency list and lock file.

## Deployment considerations

For a real deployment, do not use the development secret key or `DEBUG=True`. Use environment variables, PostgreSQL, a production app server, static-file handling, HTTPS, and a platform such as Render, Railway, or a cloud provider. Add user authentication and associate products with sellers so each seller can see only their own analytics.
