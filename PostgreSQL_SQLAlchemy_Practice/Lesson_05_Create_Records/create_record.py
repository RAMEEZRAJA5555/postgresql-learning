from database import SessionLocal
from models import Contact

# Create Session
session = SessionLocal()

# Create Contact Object
new_contact = Contact(
    name="Rameez Raja",
    phone="03001234567",
    email="rameez@example.com"
)

# Add Record
session.add(new_contact)

# Save Changes
session.commit()

# Close Session
session.close()

print("Record inserted successfully!")