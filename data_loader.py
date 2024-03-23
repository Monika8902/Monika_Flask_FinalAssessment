from datetime import datetime

queries_data = {}


def load_data():
    global queries_data
    with open('hn_logs.tsv', 'r') as file:
        queries_data = {}
        for line in file:
            timestamp, query = line.strip().split('\t')
            queries_data.setdefault(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'), []).append(query)


def get_distinct_queries(date_prefix):
    distinct_queries = set()
    for timestamp, queries in queries_data.items():
        if str(timestamp).startswith(date_prefix):
            distinct_queries.update(queries)
    return list(distinct_queries)