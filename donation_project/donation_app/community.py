```python
# donation_app/community.py
from .db import get_db_connection

def save_community(name, address, contact):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO communities (name, address, contact)
        VALUES (%s, %s, %s)
    ''', (name, address, contact))
    conn.commit()
    cur.close()
    conn.close()

def get_communities():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM communities')
    communities = cur.fetchall()
    cur.close()
    conn.close()
    return communities
```

