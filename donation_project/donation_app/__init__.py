```python
# donation_app/__init__.py

# Importar módulos do pacote
from .db import get_db_connection
from .models import create_tables
from .donor import save_donor
from .donation import save_donation, get_donations
from .community import save_community, get_communities
from .admin import view_money_donations, view_item_donations
```

