from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def manage_contacts():
    if request.method == 'POST':
        new_contact = request.json
        contacts.append(new_contact)
        return jsonify(new_contact), 201
    return jsonify(contacts)

@app.route('/contacts/<int:index>', methods=['PUT', 'DELETE'])
def update_contact(index):
    if request.method == 'PUT':
        updated_contact = request.json
        contacts[index] = updated_contact
        return jsonify(updated_contact)
    elif request.method == 'DELETE':
        deleted_contact = contacts.pop(index)
        return jsonify(deleted_contact)

if __name__ == '__main__':
    app.run(debug=True)
