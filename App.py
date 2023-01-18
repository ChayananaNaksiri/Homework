from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello Chayanana!'

@app.route('/Id')
def Id():
    return '654272105'

@app.route('/name')
def name():
    return 'Chayanana Naksiri'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if _name_ == '_main_':
    app.run(debug=True)