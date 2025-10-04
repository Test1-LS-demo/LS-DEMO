from flask import Flask, request, render_template_string, redirect
import sqlite3
import subprocess
import pickle
import base64

app = Flask(__name__)

# A01: Broken Access Control
@app.route('/admin/<user_id>')
def admin_panel(user_id):
    # Vulnerability: No authentication check
    return f"Admin panel for user {user_id}"

# A02: Cryptographic Failures
@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    # Vulnerability: Storing passwords in plain text
    if password == "admin123":
        return "Login successful"

# A03: Injection (SQL Injection)
@app.route('/user/<username>')
def get_user(username):
    conn = sqlite3.connect('users.db')
    # Vulnerability: SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = conn.execute(query).fetchone()
    return str(result)

# A04: Insecure Design
@app.route('/reset-password')
def reset_password():
    # Vulnerability: Password reset without proper verification
    return "Password reset link sent (no verification required)"

# A05: Security Misconfiguration
app.config['DEBUG'] = True  # Vulnerability: Debug mode in production

# A06: Vulnerable and Outdated Components
# Using outdated Flask version (specify in requirements.txt)

# A07: Identification and Authentication Failures
@app.route('/session')
def session_management():
    # Vulnerability: Weak session management
    session_id = "123456"  # Static session ID
    return f"Session: {session_id}"

# A08: Software and Data Integrity Failures
@app.route('/deserialize')
def deserialize_data():
    data = request.args.get('data')
    # Vulnerability: Unsafe deserialization
    obj = pickle.loads(base64.b64decode(data))
    return str(obj)

# A09: Security Logging and Monitoring Failures
@app.route('/transfer', methods=['POST'])
def money_transfer():
    amount = request.form['amount']
    # Vulnerability: No logging of sensitive operations
    return f"Transferred ${amount}"

# A10: Server-Side Request Forgery (SSRF)
@app.route('/fetch-url')
def fetch_url():
    url = request.args.get('url')
    # Vulnerability: SSRF - fetching user-provided URL
    result = subprocess.run(['curl', url], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
