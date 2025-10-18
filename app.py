import os
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, request, jsonify
import jwt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
JWT_SECRET = os.getenv("JWT_SECRET", "fallback-secret")
PORT = int(os.getenv("PORT", 3000))

# User demo (in-memory)
users = {
    "user1@example.com": {
        "email": "user1@example.com",
        "password": "pass123",
        "name": "User Satu"
    }
}

# Daftar item marketplace
items = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse Wireless", "price": 150000}
]

# === JWT Functions ===
def create_token(email):
    payload = {
        "sub": email,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.InvalidTokenError:
        return "invalid"

# === Decorator JWT ===
def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        token = auth.split(" ")[1]
        result = verify_token(token)
        if result == "expired":
            return jsonify({"error": "Token expired"}), 401
        elif result == "invalid":
            return jsonify({"error": "Invalid token"}), 401
        request.current_user = result
        return f(*args, **kwargs)
    return decorated

# === ENDPOINTS ===

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Invalid credentials"}), 401
    user = users.get(data["email"])
    if not user or user["password"] != data["password"]:
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_token(data["email"])
    print(f"[LOG] Login sukses: {data['email']}")
    return jsonify({"access_token": token}), 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items}), 200

@app.route("/profile", methods=["PUT"])
@jwt_required
def update_profile():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body harus JSON"}), 400
    if "name" not in data and "email" not in data:
        return jsonify({"error": "Minimal berikan 'name' atau 'email'"}), 400

    current_email = request.current_user["email"]
    user = users.get(current_email)
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404

    new_email = data.get("email", current_email)
    new_name = data.get("name", user["name"])

    if new_email != current_email:
        if new_email in users:
            return jsonify({"error": "Email sudah digunakan"}), 400
        del users[current_email]

    users[new_email] = {**user, "email": new_email, "name": new_name}
    print(f"[LOG] Profile diperbarui: {new_email}")
    return jsonify({
        "message": "Profile updated",
        "profile": {"name": new_name, "email": new_email}
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint tidak ditemukan"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Metode tidak diizinkan"}), 405

if __name__ == "__main__":
    print(f"🚀 Server berjalan di http://localhost:{PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=True)