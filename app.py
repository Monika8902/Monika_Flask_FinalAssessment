from flask import Flask, jsonify
from data_loader import load_data, get_distinct_queries
from urllib.parse import unquote_plus

app = Flask(__name__)

load_data()


@app.route('/1/queries/count/<date_prefix>')
def count_distinct_queries(date_prefix):
    decoded_date_prefix = unquote_plus(date_prefix)
    distinct_queries = get_distinct_queries(decoded_date_prefix)
    count = len(distinct_queries)
    return jsonify({"count": count})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)