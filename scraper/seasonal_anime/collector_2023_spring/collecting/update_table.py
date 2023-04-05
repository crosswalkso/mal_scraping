from .get_db import GetDB
from .execute_queries import insert_queries


class UpdateTables(GetDB):
    def __init__(self):
        con = self.connection()
        self.detail_table_dicts = []
        self.detail_table_dicts.append(dict(self.read_detail_data(con, "genre")))
        self.detail_table_dicts.append(dict(self.read_detail_data(con, "studio")))
        self.detail_table_dicts.append(dict(self.read_detail_data(con, "theme")))
        self.detail_table_dicts.append(dict(self.read_detail_data(con, "source")))
        self.detail_table_dicts.append(dict(self.read_detail_data(con, "demo")))

        con.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return "exit!"

    def get_anime_table(self, con):
        return dict(self.read_anime_table(con))

    def get_new_detail(self, old_detail_dict, collected_detail_set):
        index = len(old_detail_dict)
        new_detail_dict = {}
        for s in collected_detail_set:
            if s not in old_detail_dict:
                index = index + 1
                new_detail_dict[s] = index
        old_detail_dict.update(new_detail_dict)  # updated_detail_dict
        return new_detail_dict, old_detail_dict

    def insert_detail_table(self, detail_name, new_details_info):
        queries = []
        for new_detail_info in new_details_info:
            query = f"""
            insert into {detail_name}({detail_name}_name)
            values ('{new_detail_info}');
            """
            queries.append(query)
        insert_queries(queries)

    def connect_anime_and_detail_id(
        self, detail_dicts, updated_detail_table_info_dicts
    ):
        con = self.connection()
        anime_img_id = self.get_anime_table(con)
        con.close()
        queries = []
        table_names = [
            "anime_genres",
            "anime_studios",
            "theme_list",
            "source_list",
            "demo_list",
        ]
        column_names = [
            "genre_id",
            "studio_id",
            "theme_id",
            "source_id",
            "demo_id",
        ]
        for idx, detail_dict in enumerate(detail_dicts):
            for main_img in detail_dicts[detail_dict]:
                anime_id = anime_img_id[main_img]
                detail_names = detail_dicts[detail_dict][main_img]
                for detail_name in detail_names:
                    detail_id = updated_detail_table_info_dicts[idx][detail_name]
                    query = f"""insert into {table_names[idx]}(anime_id,{column_names[idx]}) values ({anime_id}, {detail_id});""".strip()
                    queries.append(query)
        insert_queries(queries)
