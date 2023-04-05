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


def get_title_ids():
    con = psycopg2.connect(
        user="crossp",
        host="127.0.0.1",
        port="5434",
        database="malinfo",
        options="-c search_path=mal",
    )
    cur = con.cursor()
    query = f"""
        select a.title, a.id
        from anime a
        join season s on a.season_id = s.id
        where season_id=2
        order by 2;
        """
    cur.execute(query)
    title_ids = cur.fetchall()
    cur.close()
    return dict(title_ids)
