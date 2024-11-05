#You must restart the kernal before running this file 

#have to import every data type you want to use
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import os


#deletes the db file every time I run this so I dont have to do it manually
try:
    os.remove("mydb.db")
except:
    print("no mydb.db file")
#this is the base class for database objects
Base = declarative_base()


#A person a row in the table. Must extend the Base class
class Person(Base): 
    __tablename__ = "people"
    
    #these are all of the columns in the people table
    #pythonVar for column = Column("columnname", DataType, Optional things(PK, unique not null etc))
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    
    
    #constructor for a person object/row
    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        
    
    #representation function. Its the thing that gets printed when this object is queried
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}),{self.age})"
    

#extending the Base class
class Item(Base):
    __tablename__ = "items"
    
    #primary_key=True makes it auto increment without any extra steps
    item = Column("item", Integer, primary_key=True)
    description = Column("desctription", String)
    owner = Column(Integer, ForeignKey("people.ssn"))
    
    #constructor for a item object/row
    def __init__(self, item, description, owner):
        self.item = item
        self.description = description
        self.owner = owner
        
    
    #representation function
    def __repr__(self):
        return f"({self.item}) {self.description} owned by {self.owner}"
    
    

#this makes a databse file call mydb.db
engine = create_engine("postgresql+psycopg2://postgres:letmein@localhost:3333/ormTest", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#creating a person and adding them to the database
person = Person(12312, "Mike", "Smith", "m", 35)
session.add(person)
#have to commit before changes are made
session.commit()

p1 = Person(31234, "Anna", "Blue", "f", 40)
p2 = Person(32423, "Bob", "Blue", "m", 35)
p3 = Person(45654, "Angela", "Cold", "f", 22)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

#basically a select * FROM peopl query for all Person objects, which would be a row in the db
results = session.query(Person).all()
print(results)

#equivalent to a SELECT * FROM people WHERE lastname == "Blue"
results = session.query(Person).filter(Person.lastname == "Blue")
#for some reason you have to iterate over it to print, not sure why. But you dont have to if the query is for all
for r in results:
    print(r)
    
    
#greater than query
results = session.query(Person).filter(Person.age > 25)
for r in results:
    print(r)
    
#string like query
results = session.query(Person).filter(Person.firstname.like("%An%"))
for r in results:
    print(r)
    
#column in a list of values query
results = session.query(Person).filter(Person.firstname.in_(["Anna","Mike"]))
for r in results:
    print(r)
    
#making items and assigning them Person owners as the foreign key constraint
i1 = Item(1, "Car", p1.ssn)
i2 = Item(2, "Laptop", p1.ssn)
i3 = Item(3, "PS5", p2.ssn)
i4 = Item(4, "Tool", p3.ssn)
i5 = Item(5, "Book", p3.ssn)
session.add(i1)
session.add(i2)
session.add(i3)
session.add(i4)
session.add(i5)
session.commit()

#SELECT * FROM items
results = session.query(Item).all()
print(results)

#SELECT * FROM items WHERE Item.owner = Person.ssn AND person.firstname = "Anna"
#adding the .all() at the end of the query lets you print it without iterating over it all
results = session.query(Item, Person).filter(Item.owner == Person.ssn).filter(Person.firstname == "Anna").all()
print(results)
#for r in results:
#    print(r)
    
