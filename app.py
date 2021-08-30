from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/vizapp_db_conf', methods=['GET', 'POST'])
def add_message(vizapp_db_conf):
    content = request.json
    print content['name']

    return jsonify({"vizapp_db_conf":vizapp_db_conf})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)