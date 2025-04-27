from flask import Flask, request, jsonify
from models import db, Incident
from datetime import datetime
import os

ALLOWED_SEVERITIES = {"Low", "Medium", "High"}

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///incidents.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/incidents', methods=['GET'])
    def get_incidents():
        incidents = Incident.query.all()
        return jsonify([
            {
                "id": i.id,
                "title": i.title,
                "description": i.description,
                "severity": i.severity,
                "reported_at": i.reported_at.isoformat()
            } for i in incidents
        ]), 200

    @app.route('/incidents', methods=['POST'])
    def create_incident():
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400
        title = data.get('title')
        description = data.get('description')
        severity = data.get('severity')
        if not title or not description or not severity:
            return jsonify({"error": "Missing required fields"}), 400
        if severity not in ALLOWED_SEVERITIES:
            return jsonify({"error": "Invalid severity"}), 400
        incident = Incident(title=title, description=description, severity=severity)
        db.session.add(incident)
        db.session.commit()
        return jsonify({
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "reported_at": incident.reported_at.isoformat()
        }), 201

    @app.route('/incidents/<int:incident_id>', methods=['GET'])
    def get_incident(incident_id):
        incident = Incident.query.get(incident_id)
        if not incident:
            return jsonify({"error": "Incident not found"}), 404
        return jsonify({
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "reported_at": incident.reported_at.isoformat()
        }), 200

    @app.route('/incidents/<int:incident_id>', methods=['DELETE'])
    def delete_incident(incident_id):
        incident = Incident.query.get(incident_id)
        if not incident:
            return jsonify({"error": "Incident not found"}), 404
        db.session.delete(incident)
        db.session.commit()
        return '', 204

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
