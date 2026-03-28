# how to create django project structure
To create a Django project structure, you can use the following command in your terminal:
`django-admin startproject project_name`
This will create a new directory called `project_name` with the following structure:

```project_name/
    manage.py
    project_name/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
- `project_name/`: The inner directory that contains the actual project code.
- `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `settings.py`: Contains all the settings and configuration for your Django project.
- `urls.py`: Contains the URL declarations for this Django project; a "table of contents" of your Django-powered site.
- `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.
- `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project (if you are using Django 3.0 or later).
- `wsigi.py` and `asgi.py` are used for deploying your project to a web server.

## Django App Structure
In addition to the project structure, you can also create apps within your Django project. An app is a web application that does something, e.g., a blog system, a database of public records, or a simple poll app. To create an app, you can use the following command:`python manage.py startapp app_name`
This will create a new directory called `app_name` with the following structure:

```app_name/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    migrations/
        __init__.py
```
- `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `admin.py`: Contains the configuration for the Django admin interface for this app.
- `apps.py`: Contains the configuration for this app.
- `models.py`: Contains the data models for this app.
- `tests.py`: Contains the tests for this app.
- `views.py`: Contains the views for this app.
- `migrations/`: Contains the migration files for this app.
- `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
