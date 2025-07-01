import sqlite3
from typing import List, Tuple, Optional, Dict, Any

class WholesaleBase:
    """Класс для работы с базой данных оптовой базы."""
    
    def __init__(self, db_name: str = 'wholesale_base.db'):
        """Инициализация соединения с базой данных."""
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
    def __enter__(self):
        """Контекстный менеджер для соединения с БД."""
        self.connect()
        return self