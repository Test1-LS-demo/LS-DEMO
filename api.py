from flask import Flask, request, jsonify
import jwt
import datetime

api = Flask(__name__)

# API01: Broken Object Level Authorization
@api.route('/api/users/<user_id>/profile')
def get_user_profile(user_id):
    # Vulnerability: No authorization check
    return jsonify({"user_id": user_id, "email": "user@example.com"})

# API02: Broken Authentication
@api.route('/api/login', methods=['POST'])
def api_login():
    # Vulnerability: Weak authentication
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:  # Any username/password works
        token = jwt.encode({'user': username}, 'secret', algorithm='HS256')
        return jsonify({'token': token})

# API03: Broken Object Property Level Authorization
@api.route('/api/users/<user_id>')
def get_user_details(user_id):
    # Vulnerability: Exposing sensitive data
    return jsonify({
        "user_id": user_id,
        "email": "user@example.com",
        "ssn": "123-45-6789",  # Sensitive data exposed
        "api_key": "secret_key_123"
    })

# API04: Unrestricted Resource Consumption
@api.route('/api/search')
def search():
    query = request.args.get('query')
    # Vulnerability: No rate limiting or resource constraints
    results = []
    for i in range(10000):  # Expensive operation
        results.append(f"Result {i} for {query}")
    return jsonify(results)

# API05: Broken Function Level Authorization
@api.route('/api/admin/delete-user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Vulnerability: No admin authorization check
    return jsonify({"message": f"User {user_id} deleted"})

# API06: Unrestricted Access to Sensitive Business Flows
@api.route('/api/purchase', methods=['POST'])
def purchase():
    # Vulnerability: No business logic validation
    quantity = request.json.get('quantity', 1)
    return jsonify({"message": f"Purchased {quantity} items"})

# API07: Server Side Request Forgery
@api.route('/api/webhook', methods=['POST'])
def webhook():
    url = request.json.get('callback_url')
    # Vulnerability: SSRF via webhook
    import requests
    response = requests.get(url)
    return jsonify({"status": "webhook_sent"})

# API08: Security Misconfiguration
@api.route('/api/config')
def get_config():
    # Vulnerability: Exposing configuration
    return jsonify({
        "database_url": "mongodb://admin:password@localhost:27017",
        "api_keys": ["key1", "key2", "key3"],
        "debug": True
    })

# API09: Improper Inventory Management
@api.route('/api/v1/old-endpoint')
def old_endpoint():
    # Vulnerability: Deprecated endpoint still active
    return jsonify({"message": "This is a deprecated endpoint"})

# API10: Unsafe Consumption of APIs
@api.route('/api/integrate', methods=['POST'])
def integrate_external_api():
    external_api_url = request.json.get('api_url')
    # Vulnerability: Unsafe consumption of external API
    import requests
    response = requests.get(external_api_url, verify=False)  # SSL verification disabled
    return jsonify(response.json())

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5001)
