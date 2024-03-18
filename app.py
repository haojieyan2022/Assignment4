from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    grades = StringField('Grades')
    satisfaction = SelectField('Academic Experience Satisfaction', choices=[
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very-dissatisfied', 'Very Dissatisfied')
    ])
    improvements = TextAreaField('Recommendations for Improvement')
    submit = SubmitField('Submit')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = MyForm()
    success = False  # Set success to False by default
    if form.validate_on_submit():
        with open('data.txt', 'a') as f:
            f.write('Name: {}\n'.format(form.name.data))
            f.write('Student Number: {}\n'.format(form.student_number.data))
            f.write('Email: {}\n'.format(form.email.data))
            f.write('Grades: {}\n'.format(form.grades.data))
            f.write('Satisfaction: {}\n'.format(form.satisfaction.data))
            f.write('Improvements: {}\n'.format(form.improvements.data))
            f.write('\n')
        success = True  # Set success to True after successful form submission
    return render_template('data_collection.html', form=form, success=success)

if __name__ == '__main__':
    app.run(debug=True)