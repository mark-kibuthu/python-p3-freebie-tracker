#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample data
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="DevSoft", founding_year=2010)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Add them to the session
session.add_all([company1, company2, dev1, dev2])
session.commit()

# Now create some freebies
freebie1 = Freebie(item_name="T-shirt", value=10, dev_id=dev1.id, company_id=company1.id)
freebie2 = Freebie(item_name="Sticker", value=1, dev_id=dev2.id, company_id=company2.id)

session.add_all([freebie1, freebie2])
session.commit()

print("Seed data added successfully!")
