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
        <form method = 'POST'>
            <label> Enter number to rotate by:
                <input  type="text" name ="rot" value="0" />
            </label>
            <br><br>
            <textarea  name = "text">{0}</textarea>
            <br><br>
            <input type="submit" value = "Click to Encode" />

        </form>

    </body>
</html>

"""
@app.route("/")
def index():
    return form.format('')


@app.route("/", methods=['POST'])
def encrypt():
    rot_num = int(request.form['rot'])
    wording = request.form['text']
    encrypted_words = rotate_string(wording, rot_num)

    return form.format(encrypted_words)


app.run()