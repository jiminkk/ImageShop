import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import render_template


UPLOAD_FOLDER = '/Users/Calvin_Yin/Desktop'
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = "I've done all the things, and here is a new photo" 
            return render_template('test.html', data = data) 
            #return redirect(url_for('uploaded_file',
             #             	filename=filename))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)