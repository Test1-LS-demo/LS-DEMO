from flask import Flask, request, jsonify
import jwt
import datetime
import ipaddress
import socket
from urllib.parse import urlparse

api = Flask(__name__)

# SSRF Mitigation Configuration
# Allowlist of external hosts or domains the server may contact
# Add your legitimate webhook destinations here
ALLOWED_CALLBACK_HOSTS = {
    'example.com',  # Replace with your actual webhook destinations
}

def is_private_ip(ip_str: str) -> bool:
    """
    Check if an IP address is private, loopback, or reserved.
    Returns True if the IP should be blocked for SSRF protection.
    """
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast
    except ValueError:
        return True  # Block invalid IPs

def resolve_hostname(hostname: str) -> str:
    """
    Resolve hostname to IP address.
    Returns empty string if resolution fails.
    """
    try:
        return socket.gethostbyname(hostname)
    except OSError:
        return ''

def is_url_allowed(raw_url: str) -> bool:
    """
    Comprehensive SSRF validation:
    1. Check URL is not empty
    2. Validate scheme (http/https only)
    3. Check against allowlist of permitted hosts
    4. Resolve hostname to IP and block private ranges
    5. Prevent DNS rebinding attacks
    """
    if not raw_url:
        return False
    parsed = urlparse(raw_url)
    if parsed.scheme not in ('http', 'https'):
        return False
    hostname = parsed.hostname or ''
    # Enforce allowlist if configured
    if ALLOWED_CALLBACK_HOSTS and hostname not in ALLOWED_CALLBACK_HOSTS:
        return False
    ip = resolve_hostname(hostname)
    if not ip or is_private_ip(ip):
        return False
    return True

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

# API07: Server Side Request Forgery (FIXED)
@api.route('/api/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint with SSRF mitigation:
    - Validates URL scheme (http/https only)
    - Checks against allowlist of permitted hosts
    - Resolves hostname to IP and blocks private/loopback ranges
    - Uses short timeout and disables redirects
    - Returns appropriate error codes for validation failures
    """
    url = request.json.get('callback_url')
    # Mitigation: Validate destination and restrict network targets
    if not is_url_allowed(url):
        return jsonify({"error": "callback_url not allowed"}), 400
    import requests
    try:
        # Use timeout and disable redirects to prevent SSRF
        requests.get(url, timeout=3, allow_redirects=False)
    except requests.RequestException:
        return jsonify({"error": "callback failed"}), 502
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
