from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, DecimalField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, InputRequired, ValidationError

from grocery_app.models import GroceryStore, ItemCategory, User
from grocery_app.extensions import app, db, bcrypt


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField 
    title = StringField("Title of store", [InputRequired(message="Must have a title")])
    # - address - StringField
    address = StringField("Location address", [InputRequired(message="Must have an address")])
    # - submit button
    submit = SubmitField("Create New Store")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    name = StringField("Name of item", [InputRequired(message="Needs a name")])
    # - price - FloatField
    price = DecimalField("Price")
    # - category - SelectField (specify the 'choices' param)
    category = SelectField("Category", choices=ItemCategory.choices())
    # - photo_url - StringField
    photo_url = StringField("Image url", [URL()])
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField("Store", query_factory=lambda: GroceryStore.query, allow_blank=False)
    # - submit button
    submit = SubmitField("Create New Item")

# Authentication

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
