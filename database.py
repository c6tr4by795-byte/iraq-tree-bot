import sqlite3

DB_NAME = "trees.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        full_name TEXT,
        phone TEXT,
        province TEXT,
        district TEXT,
        area TEXT,
        trees_count INTEGER,
        status TEXT,
        tree_code TEXT,
        qr_code TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    trees_count,
):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO requests(
            telegram_id,
            full_name,
            phone,
            province,
            district,
            area,
            trees_count,
            status,
            tree_code,
            qr_code
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            telegram_id,
            full_name,
            phone,
            province,
            district,
            area,
            trees_count,
            "pending",
            "",
            "",
        ),
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
        UPDATE requests
        SET
            status=?,
            tree_code=?,
            qr_code=?
        WHERE id=?
        """,
        (
            "approved",
            tree_code,
            tree_code,
            request_id,
        ),
    )

    conn.commit()
    conn.close()


create_tables()
