#from classes import db.session, Date, Diagram, Feature, Image, init_db
from classes import *
import base64
from datetime import datetime
#from cached_properties import cached_property


with app.app_context():
    db.drop_all()
    db.create_all()
    #init_db()

    everythingSchema = EverythingSchema(session=db.session)
    imageSchema = ImageSchema(session=db.session)
    featureSchema = FeatureSchema(session=db.session)
    dateSchema = DateSchema(session=db.session)
    factSchema = DiagramSchema(session=db.session)

    byteArray = bytearray([0] * 100)
    #base64.b64encode(byteArray).decode('utf-8')
    #date = Date(datetime.today().strftime('%Y-%m-%d'), 2024)
    date = datetime.today().strftime('%Y-%m-%d')
    results = db.session.query(Date).filter(Date.date == date).all()
    if len(results) > 0:
        date = results[0]
    else:
        date = Date(date, datetime.today().strftime('%Y'))
        print(date)
        db.session.add(date)
        db.session.commit()
        results = db.session.query(Date).filter(Date.date == datetime.today().strftime('%Y-%m-%d')).all()
        date = results[0]
        print(date)

    jsonEverything = {"Image_name":"test",
        "Resolution":"100x100",
        "Extracted_image":base64.b64encode(byteArray).decode('utf-8'),
        "Full_page_image":base64.b64encode(byteArray).decode('utf-8'),
        "GraphType":"bar",
        "NumBars":"5",
        "NumPoints":"No Data",
        "NumSlices":None
    }
    print(jsonEverything)
    jsonEverything = Everything.replaceNoData(jsonEverything)

    db.session.add(everythingSchema.load(jsonEverything, partial=True))
    db.session.commit()

    results = db.session.query(Everything).all()
    print(results)
    for result in results:
        print(result)
        print(result.Extracted_image)
        #print(everythingSchema.dump(result))
        #everything = everythingSchema.load(result)
        image = result.makeImage()
        feature = result.makeFeature()

        db.session.add(image)
        db.session.add(feature)
        db.session.add(date)
        db.session.commit()

        fact = Diagram(image.imageID, feature.featureID, date.dateID, result.Extracted_image, result.Full_page_image)
        db.session.add(fact)
        db.session.commit()

    print('Facts')
    results = db.session.query(Diagram).all()
    for result in results:
        #print(factSchema.load(results))
        print(result)

    print('Features')
    results = db.session.query(Feature).all()
    for result in results:
        print(result)

    print('Images')
    results = db.session.query(Image).all()
    for result in results:
        print(result)

    print('Dates')
    #print(datetime.today().strftime('%Y-%m-%d'))
    today =datetime.today().strftime('%Y-%m-%d')
    results = db.session.query(Date).filter(Date.date == today).all()
    print(results)

    # everything = everythingSchema.load(jsonEverything, partial=True)
    # image = everything.makeImage()
    # feature = everything.makeFeature()

    # db.session.add(date)
    # db.session.add(image)
    # db.session.add(feature)
    # db.session.commit()

    # fact = Diagram(image.imageID, feature.featureID, date.dateID, everything.Extracted_image, everything.Full_page_image)
    # db.session.add(fact)
    # db.session.commit()

    # results = db.session.query(Diagram).all()
    # print(results)
    # for result in  results:
    #     print(factSchema.dump(result))
    # results = db.session.query(Image).all()
    # print(results)
    # for result in  results:
    #     print(imageSchema.dump(results))
    # results = db.session.query(Feature).all()
    # print(results)
    # for result in  results:
    #     print(featureSchema.dump(results))

    # everything2 = Everything("testing", "10x10", "12", True, byteArray, byteArray, "testing", "bar", "5", None, None, None, None, "5", "5", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    # image2 = everything2.makeImage()
    # feature2 = everything2.makeFeature()

    # db.session.add(everything2)
    # db.session.add(image2)
    # db.session.add(feature2)
    # db.session.commit()

    # fact2 = Diagram(image2.imageID, feature2.featureID, date.dateID, everything2.Extracted_image, everything2.Full_page_image)
    # db.session.add(fact2)
    # db.session.commit()

    # results = db.session.query(Diagram).all()
    # print(results)
    # for result in  results:
    #     print(factSchema.dump(result))
    # results = db.session.query(Image).all()
    # print(results)
    # for result in  results:
    #     print(imageSchema.dump(results))
    # results = db.session.query(Feature).all()
    # print(results)
    # for result in  results:
    #     print(featureSchema.dump(results))

    # feature = Feature(3, None, None, None, 15)
    # image = Image("test", 20.2, 100, 100, "testBook", "1-1-1-1", "test ref", "testSubject", "bar", False)

    # jsonDate = {"date":"2022-01-01","year":2022}
    # jsonFeature = {"number_Bars":5,"numberPoints":12}
    # jsonImage = {"imageName":"testing","bookTitle":"testing"}

    # dateSchema = DateSchema(session=db.session)
    # featureSchema = FeatureSchema(session=db.session)
    # imageSchema = ImageSchema(session=db.session)

    # date2 = DateSchema().load(jsonDate)
    # feature2 = FeatureSchema().load(jsonFeature)
    # image2 = ImageSchema().load(jsonImage)

    # db.session.add(date2)
    # db.session.add(feature2)
    # db.session.add(image2)
    # db.session.commit()

    # diagram2 = (date2.imageID, feature2.featureID, image2.imageID)
    # db.session.add(diagram2)
    # db.session.commit()

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


    # results = db.session.query(Diagram).filter(Diagram.imageID == 1).all()
    # diagramSchema = DiagramSchema(session=db.session)
    #print(results)
    # for result in results:
    #     print(result)
    #     print(diagramSchema.dump(result))
    #print(results[0].image)