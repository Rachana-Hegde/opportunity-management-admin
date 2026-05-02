from flask import request, jsonify
from app import app
from models import db, Admin, Opportunity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import secrets, datetime


# ========================= SIGNUP =========================
@app.route('/signup', methods=['POST'])
def signup():
    data = request.form if request.form else request.get_json()

    full_name = data.get('full_name') or data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password') or data.get('confirmPassword')

    if not all([full_name, email, password, confirm_password]):
        return jsonify({"error": "All fields required"}), 400

    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    if Admin.query.filter_by(email=email).first():
        return jsonify({"error": "Account already exists"}), 400

    hashed_pw = generate_password_hash(password)

    new_user = Admin(full_name=full_name, email=email, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Signup successful"}), 201


# ========================= LOGIN =========================
@app.route('/login', methods=['POST'])
def login():
    data = request.form if request.form else request.get_json()

    email = data.get('email')
    password = data.get('password')
    remember = data.get('remember', False)

    user = Admin.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    login_user(user, remember=True)

    return jsonify({"message": "Login successful"}), 200


# ========================= LOGOUT =========================
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})


# ========================= FORGOT PASSWORD =========================
@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.form if request.form else request.get_json()

    email = data.get('email')
    user = Admin.query.filter_by(email=email).first()

    if user:
        token = secrets.token_urlsafe(16)
        expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        print(f"\nRESET LINK: http://127.0.0.1:5000/reset/{token}")
        print(f"EXPIRES AT: {expiry}\n")
    return jsonify({"message": "Reset link sent to your email!"}), 200


# ========================= GET ALL OPPORTUNITIES =========================
@app.route('/opportunities', methods=['GET'])
@login_required
def get_opportunities():
    ops = Opportunity.query.filter_by(admin_id=current_user.id).all()

    result = []
    for op in ops:
        return jsonify([
    {
        "id": op.id,
        "title": op.title,
        "description": op.description,
        "duration": op.duration,
        "start_date": op.start_date,
        "skills": op.skills,  
        "max_applicants": op.max_applicants,
        "future_opportunities": op.future_opportunities
    }
    for op in ops
])

    return jsonify(result), 200


# ========================= ADD OPPORTUNITY =========================
@app.route('/opportunities', methods=['POST'])
@login_required
def add_opportunity():
    data = request.form if request.form else request.get_json()

    required = ['title', 'duration', 'start_date', 'description',
                'skills', 'category', 'future_opportunities']

    if not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    new_op = Opportunity(
        title=data['title'],
        duration=data['duration'],
        start_date=data['start_date'],
        description=data['description'],
        skills=data['skills'],
        category=data['category'],
        future_opportunities=data['future_opportunities'],
        max_applicants=data.get('max_applicants'),
        admin_id=current_user.id
    )

    db.session.add(new_op)
    db.session.commit()

    return jsonify({"message": "Opportunity created"}), 201


# ========================= UPDATE =========================
@app.route('/opportunities/<int:id>', methods=['PUT'])
@login_required
def update_opportunity(id):
    op = Opportunity.query.get_or_404(id)

    if op.admin_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json

    op.title = data.get('title')
    op.duration = data.get('duration')
    op.start_date = data.get('start_date')
    op.description = data.get('description')
    op.skills = data.get('skills')
    op.category = data.get('category')
    op.future_opportunities = data.get('future_opportunities')
    op.max_applicants = data.get('max_applicants')

    db.session.commit()

    return jsonify({"message": "Updated"})


# ========================= DELETE =========================
@app.route('/opportunities/<int:id>', methods=['DELETE'])
@login_required
def delete_opportunity(id):
    op = Opportunity.query.get_or_404(id)

    # 🔥 SECURITY (very important)
    if op.admin_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(op)
    db.session.commit()

    return jsonify({"message": "Deleted"})

@app.route('/check-session')
def check_session():
    from flask_login import current_user
    if current_user.is_authenticated:
        return jsonify({
            "logged_in": True,
            "email": current_user.email
        })
    return jsonify({"logged_in": False})