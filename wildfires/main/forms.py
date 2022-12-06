from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    # search = StringField("Search for an Item", validators=[DataRequired()])
    stateChoices = [('', ''), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'),('CA', 'California'), ('CO', 'Colorado'),
    ('DC', 'Washington DC') , ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('CT', 'Connecticut'), 
    ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'),('LA', 'Louisiana'),('MA', 'Massachusetts'),
    ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'),('MO', 'Missouri'),('MS', 'Mississippi'), ('MT', 'Montana'), 
    ('NC', 'North Carolina'), ('NE', 'Nebraska'),('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),('NV', 'Nevada'), ('NY', 'New York'), 
    ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'),('SC', 'South Carolina'), 
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'),('VT', 'Vermont'), 
    ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming'),('AB', 'Alberta'), ('BC', 'British Colombia'), ('MB', 'Manitoba'), 
    ('NB', 'New Brunswick'),('NL', 'Newfoundland and Labrador') , ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories') , 
    ('ON', 'Ontario') , ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YK', 'Yukon'), ('76', 'Navassa Island'), ('GU', 'Guam'), ('AS', 'American Samoa')]
    
    # 1992 - 2015
    yearChoices = [('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'),
    ('2000', '2000'),('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), 
    ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015')]
    
    rowChoices = [('10', '10'), ('20', '20'), ('50', '50'), ('100', '100')]

    sortChoices = [('FIRE_NAME', 'Name'), ('FPA_ID', 'ID'), ('FIRE_SIZE', 'Size'), ('FIRE_YEAR', 'Year'), ('STATE', 'State'), ('DISCOVERY_DATE', 'Discovery Date'), ('STAT_CAUSE_DESCR', 'Cause')]

    orderChoices = [('DESC', 'Descending'), ('ASC', 'Ascending')]

    startYear = SelectField(u"Start Year", choices = yearChoices, validators=[DataRequired()])
    endYear = SelectField(u"Start Year", choices = yearChoices, validators=[DataRequired()])
    state = SelectField(u"State", choices = stateChoices)
    rows = SelectField(u"Rows per Page", choices = rowChoices, coerce=int, validators = [DataRequired()])
    sort = SelectField(u"Sort Results By", choices = sortChoices, validators = [DataRequired()])
    order = SelectField(u"Order Results By", choices = orderChoices, validators = [DataRequired()])

    submit = SubmitField("Search")
