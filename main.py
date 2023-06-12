from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/shablon.html')
def shablon():
    return render_template('shablon.html')


if __name__ == '__main__':
    print('PyCharm')
    # app.run(port=8080, host='0.0.0.0')
    app.run(debug=True, port=8080, host='127.0.0.1')

