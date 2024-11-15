from classes import *
import base64
from datetime import datetime

with app.app_context():
    db.create_all()

    everythingSchema = EverythingSchema(session=db.session)
    imageSchema = ImageSchema(session=db.session)
    featureSchema = FeatureSchema(session=db.session)
    dateSchema = DateSchema(session=db.session)
    factSchema = DiagramSchema(session=db.session)

    date = datetime.today().strftime('%Y-%m-%d')
    results = db.session.query(Date).filter(Date.date == date).all()
    if len(results) > 0:
        date = results[0]
    else:
        date = Date(date, datetime.today().strftime('%Y'))
        #print(date)
        db.session.add(date)
        db.session.commit()
        results = db.session.query(Date).filter(Date.date == datetime.today().strftime('%Y-%m-%d')).all()
        date = results[0]
        #print(date)

    results = db.session.query(Everything).all()
    for everything in results:
        image = everything.makeImage()
        feature = everything.makeFeature()
        print(image)
        print(feature)