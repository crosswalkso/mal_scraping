import psycopg2


# anime, genre
def insert_queries(queries):
    con = psycopg2.connect(
        user="crossp",
        host="127.0.0.1",
        port="5434",
        database="malinfo",
        options="-c search_path=mal",
    )

    cur = con.cursor()
    for query in queries:
        cur.execute(query)
    con.commit()
    cur.close()
    con.close()
