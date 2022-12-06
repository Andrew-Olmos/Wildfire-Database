from wildfires import db


class County(db.Model):
    __tablename__ = 'Counties'

    COUNTY_ID = db.Column(db.Text(255), primary_key=True)
    COUNTY_NAME = db.Column(db.Text(255))
    STATE_ID = db.Column(db.Text(255))



class Country(db.Model):
    __tablename__ = 'Countries'

    COUNTRY_ID = db.Column(db.Text(255), primary_key=True)
    COUNTRY_NAME = db.Column(db.Text(255))
    LAT = db.Column(db.Numeric(255))
    LONG = db.Column(db.Numeric(255))



class Fire(db.Model):
    __tablename__ = 'Fires'
    __table_args__ = (
        db.CheckConstraint("(typeof(FPA_ID) = 'text' or typeof(FPA_ID) = 'null') and not length(FPA_ID) > 100) PRIMARY KEY, NWCG_REPORTING_UNIT_ID text (255) CHECK ((typeof(NWCG_REPORTING_UNIT_ID) = 'text' or typeof(NWCG_REPORTING_UNIT_ID) = 'null') and not length(NWCG_REPORTING_UNIT_ID) > 255), SOURCE_REPORTING_UNIT text (30) CHECK ((typeof(SOURCE_REPORTING_UNIT) = 'text' or typeof(SOURCE_REPORTING_UNIT) = 'null') and not length(SOURCE_REPORTING_UNIT) > 30), SOURCE_REPORTING_UNIT_NAME text (255) CHECK ((typeof(SOURCE_REPORTING_UNIT_NAME) = 'text' or typeof(SOURCE_REPORTING_UNIT_NAME) = 'null') and not length(SOURCE_REPORTING_UNIT_NAME) > 255), LOCAL_FIRE_REPORT_ID text (255) CHECK ((typeof(LOCAL_FIRE_REPORT_ID) = 'text' or typeof(LOCAL_FIRE_REPORT_ID) = 'null') and not length(LOCAL_FIRE_REPORT_ID) > 255), LOCAL_INCIDENT_ID text (255) CHECK ((typeof(LOCAL_INCIDENT_ID) = 'text' or typeof(LOCAL_INCIDENT_ID) = 'null') and not length(LOCAL_INCIDENT_ID) > 255), FIRE_CODE text (10) CHECK ((typeof(FIRE_CODE) = 'text' or typeof(FIRE_CODE) = 'null') and not length(FIRE_CODE) > 10), FIRE_NAME text (255) CHECK ((typeof(FIRE_NAME) = 'text' or typeof(FIRE_NAME) = 'null') and not length(FIRE_NAME) > 255), FIRE_YEAR int16 CHECK ((typeof(FIRE_YEAR) = 'integer' or typeof(FIRE_YEAR) = 'null') and FIRE_YEAR >= - 32768 and FIRE_YEAR <= 32767), DISCOVERY_DATE realdate CHECK ((typeof(DISCOVERY_DATE) = 'real' or typeof(DISCOVERY_DATE) = 'null') and DISCOVERY_DATE >= 0.0), DISCOVERY_TIME text (4) CHECK ((typeof(DISCOVERY_TIME) = 'text' or typeof(DISCOVERY_TIME) = 'null') and not length(DISCOVERY_TIME) > 4), STAT_CAUSE_CODE float64 CHECK (typeof(STAT_CAUSE_CODE) = 'real' or typeof(STAT_CAUSE_CODE) = 'null'), STAT_CAUSE_DESCR text (100) CHECK ((typeof(STAT_CAUSE_DESCR) = 'text' or typeof(STAT_CAUSE_DESCR) = 'null') and not length(STAT_CAUSE_DESCR) > 100), CONT_DATE realdate CHECK ((typeof(CONT_DATE) = 'real' or typeof(CONT_DATE) = 'null') and CONT_DATE >= 0.0), CONT_TIME text (4) CHECK ((typeof(CONT_TIME) = 'text' or typeof(CONT_TIME) = 'null') and not length(CONT_TIME) > 4), FIRE_SIZE float64 CHECK (typeof(FIRE_SIZE) = 'real' or typeof(FIRE_SIZE) = 'null'), FIRE_SIZE_CLASS text (1) CHECK ((typeof(FIRE_SIZE_CLASS) = 'text' or typeof(FIRE_SIZE_CLASS) = 'null') and not length(FIRE_SIZE_CLASS) > 1), LATITUDE float64 CHECK (typeof(LATITUDE) = 'real' or typeof(LATITUDE) = 'null'), LONGITUDE float64 CHECK (typeof(LONGITUDE) = 'real' or typeof(LONGITUDE) = 'null'), STATE text (255) CHECK ((typeof(STATE) = 'text' or typeof(STATE) = 'null') and not length(STATE) > 255), FIPS_CODE text (255) CHECK ((typeof(FIPS_CODE) = 'text' or typeof(FIPS_CODE) = 'null') and not length(FIPS_CODE) > 255)"),
    )

    FPA_ID = db.Column(db.Text(100), primary_key=True)
    NWCG_REPORTING_UNIT_ID = db.Column(db.Text(255))
    SOURCE_REPORTING_UNIT = db.Column(db.Text(30))
    SOURCE_REPORTING_UNIT_NAME = db.Column(db.Text(255))
    LOCAL_FIRE_REPORT_ID = db.Column(db.Text(255))
    LOCAL_INCIDENT_ID = db.Column(db.Text(255))
    FIRE_CODE = db.Column(db.Text(10))
    FIRE_NAME = db.Column(db.Text(255))
    FIRE_YEAR = db.Column(db.Integer)
    DISCOVERY_DATE = db.Column(db.Float)
    DISCOVERY_TIME = db.Column(db.Text(4))
    STAT_CAUSE_CODE = db.Column(db.Float)
    STAT_CAUSE_DESCR = db.Column(db.Text(100))
    CONT_DATE = db.Column(db.Float)
    CONT_TIME = db.Column(db.Text(4))
    FIRE_SIZE = db.Column(db.Float)
    FIRE_SIZE_CLASS = db.Column(db.Text(1))
    LATITUDE = db.Column(db.Float)
    LONGITUDE = db.Column(db.Float)
    STATE = db.Column(db.Text(255))
    FIPS_CODE = db.Column(db.Text(255))

    NWCG_Units = db.relationship('NWCGUnit', secondary='NWCG_Sources', backref='fires')
    Reporters = db.relationship('Reporter', secondary='Reporting_Sources', backref='fires')
    Systems = db.relationship('System', secondary='System_Sources', backref='fires')




t_NWCG_Sources = db.Table(
    'NWCG_Sources',
    db.Column('FPA_ID', db.ForeignKey('Fires.FPA_ID')),
    db.Column('NWCG_UNIT_ID', db.ForeignKey('NWCG_Units.UnitId'))
)



class NWCGUnit(db.Model):
    __tablename__ = 'NWCG_Units'
    __table_args__ = (
        db.CheckConstraint("(typeof(UnitId) = 'text' or typeof(UnitId) = 'null') and not length(UnitId) > 255) PRIMARY KEY, GeographicArea text (255) CHECK ((typeof(GeographicArea) = 'text' or typeof(GeographicArea) = 'null') and not length(GeographicArea) > 255), Gacc text (255) CHECK ((typeof(Gacc) = 'text' or typeof(Gacc) = 'null') and not length(Gacc) > 255), WildlandRole text (255) CHECK ((typeof(WildlandRole) = 'text' or typeof(WildlandRole) = 'null') and not length(WildlandRole) > 255), UnitType text (255) CHECK ((typeof(UnitType) = 'text' or typeof(UnitType) = 'null') and not length(UnitType) > 255), Department text (255) CHECK ((typeof(Department) = 'text' or typeof(Department) = 'null') and not length(Department) > 255), Agency text (255) CHECK ((typeof(Agency) = 'text' or typeof(Agency) = 'null') and not length(Agency) > 255), Country text (255) CHECK ((typeof(Country) = 'text' or typeof(Country) = 'null') and not length(Country) > 255), State text (255) CHECK ((typeof(State) = 'text' or typeof(State) = 'null') and not length(State) > 255), Code text (255) CHECK ((typeof(Code) = 'text' or typeof(Code) = 'null') and not length(Code) > 255), Name text (255) CHECK ((typeof(Name) = 'text' or typeof(Name) = 'null') and not length(Name) > 255)"),
    )

    UnitId = db.Column(db.Text(255), primary_key=True)
    GeographicArea = db.Column(db.Text(255))
    Gacc = db.Column(db.Text(255))
    WildlandRole = db.Column(db.Text(255))
    UnitType = db.Column(db.Text(255))
    Department = db.Column(db.Text(255))
    Agency = db.Column(db.Text(255))
    Country = db.Column(db.Text(255))
    State = db.Column(db.Text(255))
    Code = db.Column(db.Text(255))
    Name = db.Column(db.Text(255))



class Reporter(db.Model):
    __tablename__ = 'Reporters'

    REPORTING_UNIT_ID = db.Column(db.Text(255), primary_key=True)
    REPORTING_UNIT_NAME = db.Column(db.Text(255))



t_Reporting_Sources = db.Table(
    'Reporting_Sources',
    db.Column('FPA_ID', db.ForeignKey('Fires.FPA_ID')),
    db.Column('REPORTING_UNIT_ID', db.ForeignKey('Reporters.REPORTING_UNIT_ID'))
)



class State(db.Model):
    __tablename__ = 'States'

    STATE_ID = db.Column(db.Text(255), primary_key=True)
    STATE_NAME = db.Column(db.Text(255))
    COUNTRY_ID = db.Column(db.Text(255))
    LAT = db.Column(db.Numeric(255))
    LONG = db.Column(db.Numeric(255))



t_System_Sources = db.Table(
    'System_Sources',
    db.Column('FPA_ID', db.ForeignKey('Fires.FPA_ID')),
    db.Column('SYSTEM_ID', db.ForeignKey('Systems.SYSTEM_ID'))
)



class System(db.Model):
    __tablename__ = 'Systems'

    SYSTEM_ID = db.Column(db.Text(255), primary_key=True)
    SYSTEM_TYPE = db.Column(db.Text(255))
