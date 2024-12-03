from flask import Flask, request, jsonify, make_response, render_template_string

app = Flask(__name__)

# In-memory storage for events
events = []

# HTML template for displaying events
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendar Events</title>
</head>
<body>
    <h1>Calendar Events</h1>
    <ul>
    {% for event in events %}
        <li>{{ event }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

# Endpoint to insert a new event
@app.route('/events', methods=['POST'])
def add_event():
    event = request.json
    events.append(event)
    return jsonify({"message": "Event added successfully!"}), 201

# Endpoint to list all events
@app.route('/events', methods=['GET'])
def list_events():
    return render_template_string(html_template, events=events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
