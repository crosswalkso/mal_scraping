def create_score_hist_query(scores):
    queries = []
    for idx, score in enumerate(scores):
        if score == "NULL":
            query = f"""
            insert into anime_score_hist (d_date, anime_id, score)
            values (now()::date, {idx+1}, NULL);
            """.strip()
        else:
            query = f"""
            insert into anime_score_hist (d_date, anime_id, score)
            values (now()::date, {idx+1}, {score}::real);
            """.strip()
        queries.append(query)
    return queries


def create_member_hist_query(members):
    queries = []
    for idx, member in enumerate(members):
        query = f"""
        insert into anime_members_hist (d_date, anime_id, members)
        values (now()::date, {idx+1}, {member}::int4);
        """.strip()
        queries.append(query)
    return queries
