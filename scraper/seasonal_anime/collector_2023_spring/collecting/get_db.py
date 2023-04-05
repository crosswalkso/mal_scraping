import psycopg2
from psycopg2 import Error


class GetDB:
    def connection(self):
        try:
            con = psycopg2.connect(
                user="crossp",
                host="127.0.0.1",
                port="5434",
                database="malinfo",
                options="-c search_path=mal",
            )
            return con
        except Error:
            print(Error)

    def read_detail_data(self, con, detail):
        cur = con.cursor()
        cur.execute(f"select {detail}_name, id from {detail};")
        raw_detail = cur.fetchall()
        cur.close()
        return raw_detail

    def read_anime_table(self, con):
        cur = con.cursor()
        query = f"""
        select main_img, id
        from anime;
        """
        cur.execute(query)
        anime_main_img_id = cur.fetchall()
        cur.close()
        return anime_main_img_id
