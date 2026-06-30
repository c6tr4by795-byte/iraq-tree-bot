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
        tree_code TEXT UNIQUE,
        qr_code TEXT,
        latitude REAL,
        longitude REAL,
        image_id TEXT,
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
            qr_code,
            latitude,
            longitude,
            image_id
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
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
            None,
            None,
            "",
        ),
    )

    request_id = cur.lastrowid

    conn.commit()
    conn.close()

    return request_id


def get_request(request_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM requests WHERE id=?",
        (request_id,),
    )

    row = cur.fetchone()

    conn.close()

    return row


def get_tree(tree_code):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM requests WHERE tree_code=?",
        (tree_code,),
    )

    row = cur.fetchone()

    conn.close()

    return row


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


def reject_request(request_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE requests
        SET status=?
        WHERE id=?
        """,
        (
            "rejected",
            request_id,
        ),
    )

    conn.commit()
    conn.close()


create_tables()
