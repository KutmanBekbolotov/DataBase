import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="111",
        host="localhost",
        port="4800"
    )
    cur = conn.cursor()

    conn.autocommit = False

    cur.execute("""
                CREATE TABLE IF NOT EXISTS
                users(
                id SERIAL PRIMARY KEY,
                username VARCHAR NOT NULL,
                email VARCHAR NOT NULL
                )
                """)

    cur.execute("""
                INSERT INTO users (username, email) VALUES (%s, %s)
                """, ('kutman', 'kutmanbekbolotv2003@gmail.com'))

    cur.execute("""
                SELECT * FROM users
                """)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()

except psycopg2.Error as e:
    conn.rollback()
    print("Error: ", e)

finally:
    cur.close()
    conn.close()
