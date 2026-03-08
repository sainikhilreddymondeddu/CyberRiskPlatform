import sqlite3
import json
from datetime import datetime

DB_NAME = "scan_history.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        risk_score INTEGER,
        threat_level TEXT,
        open_ports INTEGER,
        breach TEXT,
        phishing TEXT,
        result_json TEXT,
        scan_time TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_scan(result):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO scans(
        target,
        risk_score,
        threat_level,
        open_ports,
        breach,
        phishing,
        result_json,
        scan_time
    )

    VALUES(?,?,?,?,?,?,?,?)
    """, (

        result["target"],
        result["score"],
        result["threat_level"],
        result["port_count"],
        "Yes" if result["breach"]["breached"] else "No",
        result["phishing"],
        json.dumps(result),
        current_time

    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        target,
        risk_score,
        threat_level,
        open_ports,
        breach,
        phishing,
        scan_time
    FROM scans
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def get_report(scan_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT result_json
    FROM scans
    WHERE id=?
    """, (scan_id,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return json.loads(row[0])
    else:
        return None