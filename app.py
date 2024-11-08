from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for events, a little update 2
events = []

# Endpoint to insert a new event
@app.route('/events', methods=['POST'])
def add_event():
    event = request.json
    events.append(event)
    return jsonify({"message": "Event added successfully!"}), 201

# Endpoint to list all events
@app.route('/events', methods=['GET'])
def list_events():
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(debug=True)
