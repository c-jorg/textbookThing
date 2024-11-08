from classes import  Date, Diagram, Feature, Image, db, app


#init_db()

with app.app_context():
    byteArray = bytearray([0] * 100)
    date = Date("2021-11-7", 2024)
    feature = Feature(3, None, None, None, 15)
    image = Image("test", 20.2, 100, 100, "testBook", "1-1-1-1", "test ref", "testSubject", "bar", False)

    db.session.add(date)
    db.session.add(feature)
    db.session.add(image)
    db.session.commit()

    diagram = Diagram(image.imageID, feature.featureID, date.dateID, byteArray, byteArray)
    db.session.add(diagram)
    db.session.commit()

    db.session.query(Diagram).all()
    db.session.query(Feature).all()
    db.session.query(Image).all()
    db.session.query(Date).all()



    results = db.session.query(Diagram).filter(Diagram.imageID == 1).all()

    print(results)
    print(results[0].image)