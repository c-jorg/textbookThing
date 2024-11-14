#from classes import db.session, Date, Diagram, Feature, Image, init_db
from classes import *

with app.app_context():
    db.create_all()
    #init_db()

    byteArray = bytearray([0] * 100)
    date = Date("2021-11-7", 2024)
    feature = Feature(3, None, None, None, 15)
    image = Image("test", 20.2, 100, 100, "testBook", "1-1-1-1", "test ref", "testSubject", "bar", False)

    jsonDate = {"date":"2022-01-01","year":2022}
    jsonFeature = {"number_Bars":5,"numberPoints":12}
    jsonImage = {"imageName":"testing","bookTitle":"testing"}

    dateSchema = DateSchema(session=db.session)
    featureSchema = FeatureSchema(session=db.session)
    imageSchema = ImageSchema(session=db.session)

    date2 = DateSchema().load(jsonDate)
    feature2 = FeatureSchema().load(jsonFeature)
    image2 = ImageSchema().load(jsonImage)

    db.session.add(date2)
    db.session.add(feature2)
    db.session.add(image2)
    db.session.commit()

    diagram2 = (date2.imageID, feature2.featureID, image2.imageID)
    db.session.add(diagram2)
    db.session.commit()

    # db.session.add(date)
    # db.session.add(feature)
    # db.session.add(image)
    # db.session.commit()

    # diagram = Diagram(image.imageID, feature.featureID, date.dateID, byteArray, byteArray)
    # db.session.add(diagram)
    # db.session.commit()

    # db.session.query(Diagram).all()
    # db.session.query(Feature).all()
    # db.session.query(Image).all()
    # db.session.query(Date).all()


    results = db.session.query(Diagram).filter(Diagram.imageID == 1).all()
    diagramSchema = DiagramSchema(session=db.session)
    #print(results)
    for result in results:
        print(result)
        print(diagramSchema.dump(result))
    #print(results[0].image)