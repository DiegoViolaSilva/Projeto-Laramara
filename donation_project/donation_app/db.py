
```python
# donation_app/db.py
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="donation_db",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    return conn
```
