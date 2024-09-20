```python
# donation_app/donor.py
from .db import get_db_connection

def save_donor(name, email, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO donors (name, email, password)
        VALUES (%s, %s, %s)
    ''', (name, email, password))
    conn.commit()
    cur.close()
    conn.close()
```