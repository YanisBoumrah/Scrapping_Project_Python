import json

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String(1000), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'company': self.company, 'location': self.location, 'salary': self.salary, 'summary': self.summary}

    @staticmethod
    def add_job(_title, _company, _location, _salary, _summary):
        """function to add a job to database using _title, _company, _location, _salary and summary
        as parameters"""
        new_job = Job(title=_title, company=_company, location= _location, salary=_salary, summary=_summary)
        db.session.add(new_job)
        db.session.commit()

    @staticmethod
    def get_all_jobs():
        """function to get all jobs in our database"""
        return [Job.json(job) for job in Job.query.all()]

    @staticmethod
    def get_job(_id):
        """function to get job using the id of the job as parameter"""
        return [Job.json(Job.query.filter_by(id=_id).first())]

    @staticmethod
    def update_job(_id, _title, _company, _location, _salary, _summary):
        """function to update the details of a job using the id, title,
        company ,location ,salary and genre as parameters"""
        job_to_update = Job.query.filter_by(id=_id).first()
        job_to_update.title = _title
        job_to_update.company = _company
        job_to_update.location = _location
        job_to_update.salary = _salary
        job_to_update.summary = _summary
        db.session.commit()

    @staticmethod
    def delete_job(_id):
        """function to delete a movie from our database using
        the id of the movie as a parameter"""
        Job.query.filter_by(id=_id).delete()
        db.session.commit()