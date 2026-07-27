from database import SessionLocal
from models import Contact

# Create Session
session = SessionLocal()

# Read All Records
contacts = session.query(Contact).all()

# Display Records
for contact in contacts:
    print(
        contact.id,
        contact.name,
        contact.phone,
        contact.email
    )

# Close Session
session.close()