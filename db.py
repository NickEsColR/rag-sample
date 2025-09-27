import sqlite3

# Connect to SQLite database
def connect_db(db_name="doc_sage.sqlite"):
    return sqlite3.connect(db_name)

# CRUD operations for chat table
def create_chat(title:str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat (title) VALUES (?)", (title,))
    chat_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return chat_id

def list_chats():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat ORDER BY created_at DESC")
    chats = cursor.fetchall()
    conn.close()
    return chats

def read_chat(chat_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat WHERE id = ?", (chat_id,))
    chat = cursor.fetchone()
    conn.close()
    return chat

def update_chat(chat_id:int, title:str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE chat SET title = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (title, chat_id))
    conn.commit()
    conn.close()

def delete_chat(chat_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat WHERE id = ?", (chat_id,))
    conn.commit()
    conn.close()

# CRUD operations for source table
def create_source(name:str, source_text:str, chat_id:int,type:str='document'):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sources (name, source_text, type, chat_id) VALUES (?, ?, ?, ?)", (name, source_text, type, chat_id))
    conn.commit()
    conn.close()
    
def read_source(source_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sources WHERE id = ?", (source_id,))
    source = cursor.fetchone()
    conn.close()
    return source

def update_source(source_id:int, name:str, source_text:str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE sources SET name = ?, source_text = ? WHERE id = ?", (name, source_text, source_id))
    conn.commit()
    conn.close()

def list_sources(chat_id:int, source_type:str | None=None):
    conn = connect_db()
    cursor = conn.cursor()
    if source_type:
        cursor.execute("SELECT * FROM sources WHERE chat_id = ? AND type = ?", (chat_id, source_type))
    else:
        cursor.execute("SELECT * FROM sources WHERE chat_id = ?", (chat_id,))
    sources = cursor.fetchall()
    conn.close()
    return sources

def delete_source(source_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sources WHERE id = ?", (source_id,))
    conn.commit()
    conn.close()

# CRUD operations for messages table
def create_message(chat_id:int, sender:str, content:str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (chat_id, sender, content) VALUES (?, ?, ?)", (chat_id, sender, content))
    conn.commit()
    conn.close()

def get_messages(chat_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT sender, content FROM messages WHERE chat_id = ? ORDER BY timestamp ASC", (chat_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

def delete_messages(chat_id:int):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()