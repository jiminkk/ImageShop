

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import render_template
from PIL import Image


UPLOAD_FOLDER = os.getcwd()+"/input/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           

@app.route('/')
def home(): 
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            try:
                os.stat(UPLOAD_FOLDER)
            except:
                os.mkdir(UPLOAD_FOLDER)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "User_image." + file.filename.rsplit('.',1)[1]))
            data = "/static/input/User_image."+file.filename.rsplit('.',1)[1]
            #im = Image.open(os.getcwd()+"/input/User_image."+file.filename.rsplit('.',1)[1]
            #data = im
            return render_template('test.html', data = data) 
            #return redirect(url_for('uploaded_file',
             #             	filename=filename))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)