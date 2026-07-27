from database import SessionLocal
from models import Contact

# Create Session
session = SessionLocal()

# Find Contact
contact = session.query(Contact).filter_by(id=1).first()

# Delete Record
if contact:
    session.delete(contact)
    session.commit()
    print("Record deleted successfully!")
else:
    print("Record not found!")

# Close Session
session.close()