from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Rafael Marques',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Robert Hrosher',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'John Delare',
        'lang': 'python'
    },
    {
        'id': 4,
        'name': 'John Doe',
        'lang': 'node'
    }
]

@app.route('/devs', methods =['GET'])
def home():
    return jsonify(devs)

@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang)

@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev)

    return jsonify({'error': 'not found'})



if __name__ == '__main__':
    app.run(debug=True)


