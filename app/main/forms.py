from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[Required()])


    submit = SubmitField('submit')

class CommentForm(FlaskForm):

    name= StringField('Enter your comment here' ,validators = [Required()])

    submit = SubmitField('create')
