#!/usr/bin/env python3
"""
Simple validation test for SSRF fix in api.py
Run with: python test_ssrf_fix.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api import is_url_allowed

def test_ssrf_mitigation():
    """Test cases for SSRF mitigation"""
    print("Testing SSRF mitigation...")
    
    # Test cases that should be BLOCKED (return False)
    blocked_urls = [
        "http://127.0.0.1:8080/admin",           # Localhost
        "http://localhost:3000/secret",          # Localhost
        "http://169.254.169.254/latest/meta-data/",  # AWS metadata
        "http://10.0.0.1:8080/internal",        # Private IP
        "http://192.168.1.1/admin",             # Private IP
        "http://[::1]:8080/",                   # IPv6 localhost
        "ftp://example.com",                    # Wrong scheme
        "javascript:alert(1)",                  # XSS attempt
        "",                                     # Empty URL
        None,                                   # None URL
    ]
    
    # Test cases that should be ALLOWED (return True)
    # Note: These will only work if 'example.com' is in ALLOWED_CALLBACK_HOSTS
    allowed_urls = [
        "https://example.com/webhook",          # Allowlisted host
        "http://example.com/callback",          # Allowlisted host
    ]
    
    print("\nTesting BLOCKED URLs (should return False):")
    for url in blocked_urls:
        result = is_url_allowed(url)
        status = "✓ BLOCKED" if not result else "✗ ALLOWED (UNEXPECTED)"
        print(f"  {url or 'None'}: {status}")
    
    print("\nTesting ALLOWED URLs (should return True):")
    for url in allowed_urls:
        result = is_url_allowed(url)
        status = "✓ ALLOWED" if result else "✗ BLOCKED (UNEXPECTED)"
        print(f"  {url}: {status}")
    
    print("\nSSRF mitigation test completed!")

if __name__ == "__main__":
    test_ssrf_mitigation()
