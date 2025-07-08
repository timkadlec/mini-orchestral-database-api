from . import db

class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    abbreviation = db.Column(db.String(20), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

class ProjectInstrumentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey("instrument.id"), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    project = db.relationship("Project", backref="instrumentations")
    instrument = db.relationship("Instrument")
