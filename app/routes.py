from flask import Blueprint, jsonify, request
from app import db
from .models import Instrument, Project, ProjectInstrumentation

api_bp = Blueprint('api', __name__)

@api_bp.route("/instruments", methods=["GET"])
def get_instruments():
    instruments = Instrument.query.all()
    return jsonify([
        {"id": inst.id, "name": inst.name, "abbreviation": inst.abbreviation}
        for inst in instruments
    ])


@api_bp.route("/instruments", methods=["POST"])
def add_instrument():
    data = request.get_json()

    if not data or 'name' not in data or 'abbreviation' not in data:
        return jsonify({'error': 'Missing name or abbreviation'}), 400

    new_instr = Instrument(name=data['name'], abbreviation=data['abbreviation'])
    db.session.add(new_instr)
    db.session.commit()

    return jsonify({
        'id': new_instr.id,
        'name': new_instr.name,
        'abbreviation': new_instr.abbreviation
    }), 201


@api_bp.route("/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([
        {"id": p.id, "title": p.title}
        for p in projects
    ])

@api_bp.route("/projects", methods=["POST"])
def add_project():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400

    new_proj = Project(title=data['title'])
    db.session.add(new_proj)
    db.session.commit()

    return jsonify({
        'id': new_proj.id,
        'title': new_proj.title
    }), 201

# === GET all project-instrumentation relationships ===
@api_bp.route("/project-instrumentation", methods=["GET"])
def get_project_instrumentations():
    instrumentations = ProjectInstrumentation.query.all()
    return jsonify([
        {
            "id": pi.id,
            "project": pi.project.title,
            "instrument": pi.instrument.name,
            "count": pi.count
        }
        for pi in instrumentations
    ])

# === POST: assign instrument to project ===
@api_bp.route("/project-instrumentation", methods=["POST"])
def add_project_instrumentation():
    data = request.get_json()
    if not data or "project_id" not in data or "instrument_id" not in data or "count" not in data:
        return jsonify({"error": "Missing project_id, instrument_id or count"}), 400

    # Optional: validate existence
    project = Project.query.get(data["project_id"])
    instrument = Instrument.query.get(data["instrument_id"])
    if not project or not instrument:
        return jsonify({"error": "Invalid project_id or instrument_id"}), 404

    new_entry = ProjectInstrumentation(
        project_id=data["project_id"],
        instrument_id=data["instrument_id"],
        count=data["count"]
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({
        "id": new_entry.id,
        "project": project.title,
        "instrument": instrument.name,
        "count": new_entry.count
    }), 201