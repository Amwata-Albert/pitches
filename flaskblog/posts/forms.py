from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    category = SelectField('Category', choices=[('Product Pitch', 'Product Pitch'), ('Interview Pitch', 'Interview Pitch'), ('Pick Up Lines', 'Pick Up Lines'), ('Promotion Pitch', 'Promotion Pitch')], validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')