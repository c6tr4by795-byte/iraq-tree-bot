import sqlite3


DB_NAME = "trees.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tree_requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        full_name TEXT,
        phone TEXT,
        province TEXT,
        district TEXT,
        area TEXT,
        count INTEGER,
        status TEXT,
        tree_code TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_request(
    telegram_id,
    full_name,
    phone,
    province,
    district,
    area,
    count
):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tree_requests
        (
            telegram_id,
            full_name,
            phone,
            province,
            district,
            area,
            count,
            status,
            tree_code
        )
        VALUES (?,?,?,?,?,?,?,?,?)
        """,
        (
            telegram_id,
            full_name,
            phone,
            province,
            district,
            area,
            count,
            "pending",
            ""
        )
    )

    request_id = cur.lastrowid

    conn.commit()
    conn.close()

    return request_id


def approve_request(request_id, tree_code):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tree_requests
        SET status=?, tree_code=?
        WHERE id=?
        """,
        (
            "approved",
            tree_code,
            request_id
        )
    )

    conn.commit()
    conn.close()


create_tables()
