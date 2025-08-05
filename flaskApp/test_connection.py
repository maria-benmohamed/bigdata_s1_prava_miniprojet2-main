import psycopg2
from psycopg2.extras import RealDictCursor

def test_db_connection():
    try:
        conn = psycopg2.connect(
            host='aws-0-eu-north-1.pooler.supabase.com',
            port=5432,
            database='postgres',
            user='postgres.wtfcaacrrcjzhhtnphlf',
            password='mimi2004.'
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("SELECT * FROM resultats LIMIT 5;")
        rows = cursor.fetchall()
        print("✔ Connected and retrieved rows:")
        for row in rows:
            print(row)

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_db_connection()
