#!/usr/bin/env python3
"""
Simple SSRF validation test (no Flask required)
Run with: python test_ssrf_simple.py
"""

import ipaddress
import socket
from urllib.parse import urlparse

# Copy the SSRF mitigation functions (without Flask dependency)
ALLOWED_CALLBACK_HOSTS = {
    'example.com',
}

def is_private_ip(ip_str: str) -> bool:
    """Check if an IP address is private, loopback, or reserved."""
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast
    except ValueError:
        return True  # Block invalid IPs

def resolve_hostname(hostname: str) -> str:
    """Resolve hostname to IP address."""
    try:
        return socket.gethostbyname(hostname)
    except OSError:
        return ''

def is_url_allowed(raw_url: str) -> bool:
    """Comprehensive SSRF validation."""
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

def test_ssrf_mitigation():
    """Test cases for SSRF mitigation"""
    print("🔒 Testing SSRF Mitigation...")
    print("=" * 50)
    
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
    ]
    
    # Test cases that should be ALLOWED (return True)
    allowed_urls = [
        "https://example.com/webhook",          # Allowlisted host
        "http://example.com/callback",          # Allowlisted host
    ]
    
    print("\n🚫 Testing BLOCKED URLs (should return False):")
    blocked_count = 0
    for url in blocked_urls:
        result = is_url_allowed(url)
        status = "✓ BLOCKED" if not result else "✗ ALLOWED (UNEXPECTED)"
        if not result:
            blocked_count += 1
        print(f"  {url or 'None'}: {status}")
    
    print(f"\n✅ Successfully blocked {blocked_count}/{len(blocked_urls)} malicious URLs")
    
    print("\n✅ Testing ALLOWED URLs (should return True):")
    allowed_count = 0
    for url in allowed_urls:
        result = is_url_allowed(url)
        status = "✓ ALLOWED" if result else "✗ BLOCKED (UNEXPECTED)"
        if result:
            allowed_count += 1
        print(f"  {url}: {status}")
    
    print(f"\n✅ Successfully allowed {allowed_count}/{len(allowed_urls)} legitimate URLs")
    
    print("\n🎯 SSRF Mitigation Test Results:")
    print(f"   • Blocked malicious URLs: {blocked_count}/{len(blocked_urls)}")
    print(f"   • Allowed legitimate URLs: {allowed_count}/{len(allowed_urls)}")
    print(f"   • Total test coverage: {blocked_count + allowed_count}/{len(blocked_urls) + len(allowed_urls)}")
    
    if blocked_count == len(blocked_urls) and allowed_count == len(allowed_urls):
        print("\n🎉 ALL TESTS PASSED! SSRF mitigation is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Review the implementation.")

if __name__ == "__main__":
    test_ssrf_mitigation()
