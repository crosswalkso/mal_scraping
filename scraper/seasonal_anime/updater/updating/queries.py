def create_score_hist_query(anime_ids, scores):
    queries = []
    for idx, score in enumerate(scores):
        if score == "NULL":
            query = f"""
            insert into anime_score_hist (d_date, anime_id, score)
            values (now()::date, {anime_ids[idx]}, NULL);
            """.strip()
        else:
            query = f"""
            insert into anime_score_hist (d_date, anime_id, score)
            values (now()::date, {anime_ids[idx]}, {score}::real);
            """.strip()
        queries.append(query)
    return queries


def create_member_hist_query(anime_ids, members):
    queries = []
    for idx, member in enumerate(members):
        query = f"""
        insert into anime_members_hist (d_date, anime_id, members)
        values (now()::date, {anime_ids[idx]}, {member}::int4);
        """.strip()
        queries.append(query)
    return queries
