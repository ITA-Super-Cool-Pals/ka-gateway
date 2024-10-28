import csv, json
from io import StringIO
from flask import Response

def convert_json_to_csv(json_data, filename='data.csv'):
    # Create a string buffer to store CSV data
    csv_buffer = StringIO()

    # Check if json_data is non-empty and get the headers from first row
    if json_data:
        headers = json_data[0].keys()
    else:
        headers = []

    # Write CSV data to buffer
    writer = csv.DictWriter(csv_buffer, fieldnames=headers)
    writer.writeheader()
    writer.writerows(json_data)

    # Create a response with CSV MIME type
    csv_buffer.seek(0)
    response = Response(csv_buffer, mimetype="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response
