from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
       <label>
        Rotate By:
        <input type="text" id="rot" name="rot" value="0"/>
       </label>
       <textarea rows="4" cols="50" name="text">{0}</textarea>
       <input type="submit" value="Submit"/>
     </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rotation= request.form['rot']
    final= rotate_string(str(text),int(rotation))
    return  '<h1>' + form.format(final) + '</h1>'

app.run()