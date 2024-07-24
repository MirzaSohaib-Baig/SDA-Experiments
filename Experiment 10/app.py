from flask import Flask, jsonify, request, json

app = Flask( __name__ )
data = json.load(open("data.json", encoding="utf-8"))

@app.route('/')
def hello():
    return 'Welcome back, Hacker'

@app.route('/showdata')
def showall():
    return jsonify(data)

@app.route('/show', methods=['GET', 'POST', 'PUT', 'DELETE'])
def showid():
    if request.method == 'POST':
        id = int(request.args['id'])
        name = request.args['name']
        coursecredit = int(request.args['coursecredit'])
        semester = int(request.args['semester'])
        dic = {'id': id, 'name': name, 'coursecredit': coursecredit, 'semester': semester}
        data.append(dic)
        return(dic)

    elif request.method == 'GET':
        d = []
        id = int(request.args['id'])
        for i in data:
            if i['id'] == id:
                d.append(i)
                break
        return jsonify(d)

    elif request.method == 'PUT':
        id = int(request.args['id'])
        name = request.args['name']
        coursecredit = int(request.args['coursecredit'])
        semester = int(request.args['semester'])
        for i in data:
            if i['id'] == id:
                i['name'] = name
                i['coursecredit'] = coursecredit
                i['semester'] = semester
                break
        return jsonify(data)

    elif request.method == 'DELETE':
        id = int(request.args['id'])
        for i in data:
            if i['id'] == id:
                data.remove(i)
        return jsonify(data)