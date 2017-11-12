from flask import Flask, render_template
# from wtforms import Form, TextField, validators

#from flask.ext.navigation import Navigation

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/howitworks')
def how():
    return render_template('howitworks.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')
 
# class ReusableForm(Form):
#     recipient = TextField('Recipient:', validators=[validators.required()])
#     sender = TextField('@wellesley.edu email:', validators=[validators.required()])
#     message = TextField('Message:', validators=[validators.required()])
#   
@app.route('/submission')
def submission():
    # form = ReusableForm(request.form)
    # 
    # if request.method == 'POST':
    #     recipient=request.form['inputRecipient']
    #     email=request.form['inputEmail']
    #     message=request.form['inputMessage']
    #     print name, " ", email, " ", password
    #     
    #     if form.validate():
    #         flash('Thanks for registration')
    #     else:
    #         flash('Error with message')
        
    return render_template('submission.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8910)