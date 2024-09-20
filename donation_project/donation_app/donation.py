
```python
# donation_app/donation.py
from .db import get_db_connection

def save_donation(donor_id, donation_type, address, amount, payment_method):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO donations (donor_id, donation_type, address, amount, payment_method)
        VALUES (%s, %s, %s, %s, %s)
    ''', (donor_id, donation_type, address, amount, payment_method))
    conn.commit()
    cur.close()
    conn.close()

def get_donations():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM donations')
    donations = cur.fetchall()
    cur.close()
    conn.close()
    return donations
```
