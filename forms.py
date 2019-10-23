from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateAccount(FlaskForm):
    s_username = StringField("Your Name", validators=[DataRequired, Length(min=2, max=20)])
    r_username = StringField("Name of other person")
    submit = SubmitField("Create Link")
