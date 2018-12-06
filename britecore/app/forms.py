from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import (
    TextField,
    SubmitField,
    StringField,
    SelectField,
    SubmitField,
    IntegerField,
    TextAreaField,
    DateField,
    SubmitField,
)


class FeatureRequestForm(FlaskForm):
    title = TextField(u"title", validators=[DataRequired()])
    description = TextAreaField(u"description", validators=[DataRequired()])
    client = SelectField(
        u"client",
        validators=[DataRequired()],
        choices=[
            ("Client A", "Client A"),
            ("Client B", "Client B"),
            ("Client C", "Client C"),
            ("Client D", "Client D"),
            ("Client E", "Client E"),
            ("Client F", "Client F"),
            ("Client G", "Client G"),
            ("Client H", "Client H"),
            ("Client I", "Client I"),
            ("Client J", "Client J"),
            ("Client K", "Client K"),
            ("Client L", "Client L"),
            ("Client M", "Client M"),
            ("Client N", "Client N"),
            ("Client O", "Client O"),
            ("Client P", "Client P"),
            ("Client Q", "Client Q"),
            ("Client R", "Client R"),
            ("Client S", "Client S"),
            ("Client T", "Client T"),
            ("Client U", "Client U"),
            ("Client V", "Client V"),
            ("Client W", "Client W"),
            ("Client X", "Client X"),
            ("Client Y", "Client Y"),
            ("Client Z", "Client Z"),
        ],
    )
    client_priority = IntegerField(
        u"client_priority", validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    target_date = DateField(u"target_date", validators=[DataRequired()])
    product_area = SelectField(
        u"product_area",
        validators=[DataRequired()],
        choices=[
            ("Policies", "Policies"),
            ("Billing", "Billing"),
            ("Claims", "Claims"),
            ("Reports", "Reports"),
        ],
    )
    submit = SubmitField(u"submit")
