### `admin.py` - Funcionalidades Administrativas

```python
# donation_app/admin.py
from .donation import get_donations

def view_money_donations():
    donations = get_donations()
    money_donations = [d for d in donations if d[2] == 'money']
    return money_donations

def view_item_donations():
    donations = get_donations()
    item_donations = [d for d in donations if d[2] in ['food', 'clothes']]
    return item_donations
```
