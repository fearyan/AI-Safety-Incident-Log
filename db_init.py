from models import db, Incident
from app import create_app

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    # Sample incidents
    sample_incidents = [
        Incident(
            title="AI model generated biased output",
            description="The AI chatbot produced a response that was flagged as biased.",
            severity="Medium"
        ),
        Incident(
            title="Data privacy breach",
            description="Sensitive user data was exposed due to a model misconfiguration.",
            severity="High"
        ),
        Incident(
            title="False positive in content moderation",
            description="AI incorrectly flagged harmless content as inappropriate.",
            severity="Low"
        ),
    ]
    db.session.bulk_save_objects(sample_incidents)
    db.session.commit()
    print("Database initialized with sample data.")
