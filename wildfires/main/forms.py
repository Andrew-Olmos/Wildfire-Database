from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField("Search for an Item", validators=[DataRequired()])
    stateChoices = [('AK', 'Alaska'), ('AL', 'Alabama'), ('AB', 'Alberta'), ('BC', 'British Colombia'), ('MB', 'Manitoba'), 
    ('NB', 'New Brunswick'),('NL', 'Newfoundland and Labrador') , ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories') , 
    ('ON', 'Ontario') , ('PE', 'Prince Edward Island'),('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YK', 'Yukon'), ('76', 'Navassa Island'), 
    ('AR', 'Arkansas'), ('AS', 'American Samoa'), ('AZ', 'Arizona'),('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), 
    ('DC', 'Washington DC') , ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'),
    ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'),('LA', 'Louisiana'),('MA', 'Massachusetts'),
    ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MIN', 'Minnesota'),('MO', 'Missouri'),('MS', 'Mississippi'), ('MT', 'Montana'), 
    ('NC', 'North Carolina'), ('NE', 'Nebraska'),('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),('NV', 'Nevada'), ('NY', 'New York'), 
    ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'),('SC', 'South Carolina'), 
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'),('VT', 'Vermont'), 
    ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')]
    state = SelectField(u"State", choices = stateChoices, validators = [DataRequired()])
    submit = SubmitField("Search")
