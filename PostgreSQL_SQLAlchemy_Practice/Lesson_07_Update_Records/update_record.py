from database import SessionLocal
from models import Contact

# Create Session
session = SessionLocal()

# Find Contact
contact = session.query(Contact).filter_by(id=1).first()

# Update Record
if contact:
    contact.name = "Rameez Raja"
    contact.phone = "03112223344"

    session.commit()

    print("Record updated successfully!")
else:
    print("Record not found!")

# Close Session
session.close()