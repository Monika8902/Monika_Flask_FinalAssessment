# Monika_Flask_FinalAssessment
Code Explanation:

1.Overview:
   - This code consists of two main files: `data_loader.py` and `app.py`.
   - The purpose of the code is to create a Flask API that counts the distinct queries for a given date prefix from a dataset stored in a TSV file.

2.data_loader.py:
   - This module is responsible for loading data from the TSV file and providing a function to retrieve distinct queries based on a date prefix.
   - It utilizes the `datetime` module to handle timestamps.
   - The `load_data()` function loads data from the TSV file located at the specified path ('hn_logs.tsv').
   - For each line in the file, it splits the line into timestamp and query components, converts the timestamp to a `datetime` object, and stores the data in a dictionary (`queries_data`), where timestamps are keys and queries are values.
   - The `get_distinct_queries()` function retrieves distinct queries associated with a given date prefix from the `queries_data` dictionary.
   - It iterates through the timestamps in `queries_data`, checks if the string representation of each timestamp starts with the provided date prefix, and collects the associated queries into a set to remove duplicates.
   - Finally, it returns the distinct queries as a list.

3. app.py :
   - This module sets up a Flask web application to expose an API endpoint for counting distinct queries based on a date prefix.
   - It imports the necessary modules (`Flask`, `jsonify`, `data_loader`, and `unquote_plus` from `urllib.parse`).
   - The `load_data()` function from `data_loader` is called to load the dataset when the application starts.
   - The `/1/queries/count/<date_prefix>` route is defined to handle GET requests with a date prefix parameter.
   - The `count_distinct_queries()` function is executed when a request is made to the defined route.
   - It decodes the URL-encoded date prefix using `unquote_plus()` to handle special characters.
   - Then, it calls the `get_distinct_queries()` function from `data_loader` to retrieve distinct queries for the given date prefix.
   - The count of distinct queries is calculated, and the result is returned as a JSON response.

4. Execution:
   - To run the Flask application, you can execute `app.py`.
   - The application listens for incoming requests on the specified host (`0.0.0.0`) and port (`8000`) and runs in debug mode (`debug=True`).
   - Once the application is running, it exposes the `/1/queries/count/<date_prefix>` endpoint, allowing users to query for distinct counts of queries based on date prefixes.

