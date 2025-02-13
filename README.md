# Flask Broilerplate: Environment Setup

Customizable broiler-plate and project template for scaling python web projects. 

Key Principles:
- Modularity
- DRY - 'Don't Repeat Yourself'
- Separation of Concerns
- Configuration Management
- Testing


## Getting Started

1. Create and activate python virtual environment:
```
python -m venv venv
```

```
venv\Scripts\activate
```

> **Note:** [This Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) manages virtual environments automatically.

2. Create `.env` file for project variables

3. Create entry point: New file `app.py`

4. Include project packages: 
```
py -m pip install -r requirements.txt
```
AND
```
pip freeze > requirements.txt
```

5. Layer application using a **modular file structure**:

```
project/
│
├── app/
│   ├── __init__.py          # App factory, configuration, and initialization
│   ├── config.py            # Configuration settings (dev, prod, testing)
│   ├── extensions.py        # Initialize extensions (e.g., SQLAlchemy, Flask-Migrate)
│   │
│   ├── models/              # Database models (SQLAlchemy)
│   │   ├── __init__.py
│   │   └── user_repository.py
│   │
│   ├── repositories/        # Data access layer (e.g., SQLAlchemy queries)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── post.py
│   │
│   ├── services/            # Business logic (e.g., user registration, post creation)
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── post_service.py
│   │
│   ├── api/                 # REST API (Blueprint)
│   │   ├── __init__.py
│   │   ├── v1/              # Versioned API
│   │   │   ├── routes.py
│   │   │   └── schemas.py   # Request/response validation (e.g., Marshmallow)
│   │   └── v2/              # Future API versions
│   │       ├── routes.py
│   │       └── schemas.py
│   │
│   ├── web/                 # Web routes (Blueprint for HTML templates)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py         # WTForms for form validation
│   │
│   ├── templates/           # HTML templates (Jinja2)
│   │   ├── base.html
│   │   ├── web/
│   │   │   ├── index.html
│   │   │   └── profile.html
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   │
│   ├── static/              # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── scripts/
│   │   └── images/
│   │
│   └── utils/               # Shared utilities (e.g., helpers, custom decorators)
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                   # Unit and integration tests
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_api.py
│
├── requirements.txt         # Dependencies
├── .env                     # Environment variables (not committed)
├── run.py                   # Entry point to run the app
└── README.md                # Important App information
```


## DRY Principles

Reuses service and repository logic, avoiding duplication.

