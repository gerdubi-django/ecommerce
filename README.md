# Ecommerce

This project is a basic Django e-commerce application.

## Setup

1. Create and activate a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install the dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations.
   ```bash
   python manage.py migrate
   ```
4. Create an admin account.
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server.
   ```bash
   python manage.py runserver
   ```

## Tests

Execute the project test suite.
```bash
python manage.py test
```
