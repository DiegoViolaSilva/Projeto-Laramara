```python
# donation_app/models.py
from .db import get_db_connection

def create_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            id SERIAL PRIMARY KEY,
            donor_id INTEGER REFERENCES donors(id),
            donation_type VARCHAR(10),
            address TEXT,
            amount DECIMAL(10, 2),
            payment_method VARCHAR(50),
            status BOOLEAN DEFAULT FALSE
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS communities (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            address TEXT,
            contact VARCHAR(100)
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
```
