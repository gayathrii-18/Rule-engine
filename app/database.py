import sqlite3
from .models import Node, NodeType
import json

def get_db_connection():
    conn = sqlite3.connect('rule_engine.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS rules
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     ast TEXT NOT NULL)''')
    conn.close()

def save_rule(name, ast):
    conn = get_db_connection()
    conn.execute('INSERT INTO rules (name, ast) VALUES (?, ?)',
                 (name, json.dumps(ast.to_dict())))
    conn.commit()
    conn.close()

def get_rule(name):
    conn = get_db_connection()
    rule = conn.execute('SELECT * FROM rules WHERE name = ?', (name,)).fetchone()
    conn.close()
    if rule:
        return Node.from_dict(json.loads(rule['ast']))
    return None
