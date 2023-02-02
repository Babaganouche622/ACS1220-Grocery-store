from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, InputRequired

from grocery_app.models import GroceryStore, ItemCategory

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
