from classes import session, Date, Diagram, Feature, Image, init_db

init_db()

# byteArray = bytearray([0] * 100)
# date = Date("2021-11-7", 2024)
# feature = Feature(3, None, None, None, 15)
# image = Image("test", 20.2, 100, 100, "testBook", "1-1-1-1", "test ref", "testSubject", "bar", False)

# session.add(date)
# session.add(feature)
# session.add(image)
# session.commit()

# diagram = Diagram(image.imageID, feature.featureID, date.dateID, byteArray, byteArray)
# session.add(diagram)
# session.commit()

# session.query(Diagram).all()
# session.query(Feature).all()
# session.query(Image).all()
# session.query(Date).all()


results = session.query(Diagram).filter(Diagram.imageID == 1).all()

print(results)
print(results[0].image)