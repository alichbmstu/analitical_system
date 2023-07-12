import json

from flask import Flask, jsonify, request

with open('output.json', 'r') as fp:
    data = json.load(fp)
    print(data)

app = Flask('Freelys')

def check_log(username, password):
    flag = False
    for key1, value1 in data.items():
        for key2, value2 in data.items():
            if username == value1 and password == value2:
                flag = True
    return flag

@app.get('/login')
def loginPage():
    return """
    <html>
        <head>
            <title>Freelys Login page</title>
        </head>
        <body>
            <form action="/login" method="POST">
                <input name="username" />
                <input name="password" />
                <button action="submit">Login</button>
            </form>
        </body>
    </html>
    """


@app.post('/login')
def loginHandler():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    if check_log(username, password):
        return jsonify({"result": "OK"}), 200
    else:
        return jsonify({"result": "ERROR", "msg": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)

