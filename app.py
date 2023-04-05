from flask import Flask, render_template, request, redirect, url_for
import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), r"C:\learning-platform\upload documents")
app.config['SECRET_KEY'] = 'your_secret_key'

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[FileRequired(), FileAllowed(['pdf', 'doc', 'docx', 'txt'], 'Only PDF, DOC, DOCX, and TXT files allowed!')])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', form=form, files=files)

if __name__ == '__main__':
    app.run(debug=True)
