import _sqlite3

connection = _sqlite3.connect('doc_sage.sqlite')
cursor = connection.cursor()

# chat table: store chat names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Sources table: store sources loaded into the vector store
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source_text TEXT,
        type TEXT DEFAULT 'document',
        chat_id INTEGER,
        FOREIGN KEY (chat_id) REFERENCES chat (id)
    )
''')

# Messages table: store messages in a chat
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (chat_id) REFERENCES chat (id)
    )
''')

connection.commit()
connection.close()

print("Database and tables created successfully.")