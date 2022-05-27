from  flask import Flask, render_template 
from flask_wtf import FlaskForm 
from wtforms  import FileField
from flask_uploads import configure_uploads,AUDIO, IMAGES,UploadSet


app = Flask(__name__)

app.config['SECRET_KEY'] = 'sUPERSECRETKEY'
app.config['UPLOADED_AUDIO_DEST'] = 'uploads/audio'
   

audio = UploadSet('audio', AUDIO)
configure_uploads(app, audio)

class myForm(FlaskForm): 
    image = FileField('image')
    
    
@app.route('/' , METHODS=['GET', 'POST'])  
def index(): 
    form = Myform()
    
    if form.validate_on_submit(): 
       
        filename = audio.save(form.audio.data())
        return f'Filename: {filename}'
    
    return render_template('ind.html', form=form)