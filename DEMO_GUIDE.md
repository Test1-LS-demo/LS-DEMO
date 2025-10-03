# 🎯 Legit Security ASPM Demo Guide
## 10-Minute Demo Script for Application Security Posture Management & Vulnerability Prioritization

---

## 📋 **PRE-DEMO SETUP** (Do this before your presentation)

### 1. **Import Your Repositories into Legit Security ASPM**
- Connect your GitHub organization `Test1-LS-demo`
- Import all 5 repositories:
  - `LS-DEMO` (your custom vulnerable app)
  - `juice-shop` (OWASP Juice Shop)
  - `NodeGoat` (OWASP NodeGoat)
  - `mutillidae` (OWASP Mutillidae)
  - `WebGoat` (OWASP WebGoat)

### 2. **Let the Initial Scan Complete**
- Wait for all repositories to be scanned
- This may take 5-10 minutes for the first scan

---

## 🎬 **DEMO SCRIPT: 10 Minutes Total**

---

## **PART 1: Application Security Posture Overview (4 minutes)**

### **Opening (30 seconds)**
> "Today I'll show you how Legit Security ASPM helps organizations manage application security across their entire portfolio and prioritize vulnerabilities based on business risk."

### **Step 1: Show Application Portfolio (1.5 minutes)**
**What to say:**
> "Let's start by looking at our application portfolio. I have 5 applications here - a mix of modern and legacy systems representing typical enterprise environments."

**What to do:**
1. **Click "Dashboard" in the sidebar** (pie chart icon)
2. **Show the repository overview** with all 5 repos
3. **Point out the different technologies:**
   - `LS-DEMO`: Python/Flask + Node.js
   - `juice-shop`: Modern Node.js/TypeScript
   - `NodeGoat`: Legacy Node.js
   - `mutillidae`: PHP
   - `WebGoat`: Java

**Key talking points:**
- "Notice the diversity of our application stack"
- "Each has different security profiles and risk levels"
- "This is typical of most organizations with mixed technology stacks"

### **Step 2: Demonstrate Vulnerability Discovery (1.5 minutes)**
**What to say:**
> "Let's see what security issues Legit has discovered across our applications."

**What to do:**
1. **Click "Issues" in the sidebar** (square with exclamation mark)
2. **Show the unified vulnerability dashboard**
3. **Point out the vulnerability distribution:**
   - Critical vulnerabilities (red)
   - High vulnerabilities (orange)
   - Medium/Low vulnerabilities (yellow/green)
4. **Show repository-specific filtering**

**Key talking points:**
- "We can see vulnerabilities across all our applications in one unified view"
- "The system automatically categorizes and prioritizes based on severity"
- "Notice how different applications have different risk profiles"

### **Step 3: Show Critical Vulnerability Details (1 minute)**
**What to say:**
> "Let's dive into some of the critical vulnerabilities to understand the business impact."

**What to do:**
1. **Filter to show only Critical/High vulnerabilities**
2. **Click on a high-priority vulnerability**
3. **Show the detailed analysis:**
   - Vulnerability description
   - Affected components
   - Exploitability information
   - Remediation guidance

**Key talking points:**
- "We can see specific vulnerable packages and their versions"
- "The system provides context about exploitability and impact"
- "This gives us actionable information for remediation"

---

## **PART 2: Risk-Based Vulnerability Prioritization (4 minutes)**

### **Step 4: Show Risk Scoring and Prioritization (1.5 minutes)**
**What to say:**
> "Legit doesn't just show you vulnerabilities - it prioritizes them based on actual business risk and exploitability."

**What to do:**
1. **Stay in "Issues" section** (you're already there)
2. **Show the risk scoring methodology**
3. **Point out how vulnerabilities are ranked:**
   - Business impact assessment
   - Exploitability scoring
   - Remediation effort estimation
4. **Show the difference between CVSS scores and Legit's risk scores**

**Key talking points:**
- "This isn't just a list of CVEs - it's business-focused risk assessment"
- "The system understands which vulnerabilities matter most to your organization"
- "We can see the full context of each vulnerability"

### **Step 5: Demonstrate Cross-Application Impact (1.5 minutes)**
**What to say:**
> "Let's see how vulnerabilities span across our application portfolio and understand the full scope of risk."

**What to do:**
1. **Show a vulnerability that affects multiple applications**
2. **Demonstrate the cross-application view**
3. **Show how fixing it in one place affects the overall risk**
4. **Point out shared dependencies and their risks**

**Key talking points:**
- "The same vulnerability might exist in multiple applications"
- "We can see the full scope of impact across our portfolio"
- "This helps prioritize remediation efforts based on maximum impact"

### **Step 6: Show Remediation Guidance (1 minute)**
**What to say:**
> "For each vulnerability, Legit provides specific, actionable remediation guidance."

**What to do:**
1. **Click on a high-priority vulnerability**
2. **Show the remediation section:**
   - Specific version updates needed
   - Code changes required
   - Testing recommendations
3. **Show the automated fix suggestions**

**Key talking points:**
- "The system provides specific remediation guidance"
- "We can see exactly what needs to be changed"
- "This reduces the time from discovery to fix"

---

## **PART 3: Live Critical Vulnerability Fix (2 minutes)**

### **Step 7: Fix Critical Flask Vulnerability in LS-DEMO (2 minutes)**
**What to say:**
> "Let's fix a critical vulnerability in real-time. I'll show you how to remediate a high-risk Flask vulnerability in our LS-DEMO application."

**What to do:**
1. **Navigate to LS-DEMO repository** in Legit
2. **Find the Flask vulnerability** (likely Flask 1.0.2 or similar)
3. **Show the vulnerability details:**
   - Click on the Flask vulnerability
   - Show the risk score and impact
   - Show the suggested fix (upgrade to Flask 2.0+)
4. **Apply the fix:**
   - Open the requirements.txt file
   - Update Flask version: `Flask>=2.0.0`
   - Commit the change
   - Show the verification in Legit

**Key talking points:**
- "This is a critical authentication vulnerability in Flask"
- "The fix is simple - just update the version number"
- "We can see the risk reduction immediately after the fix"
- "This demonstrates the complete vulnerability lifecycle"

### **Alternative Fix Options (if Flask fix isn't available):**
- **NodeGoat**: Update express-jwt from 0.1.3 to 9.0+
- **juice-shop**: Update jsonwebtoken from 0.4.0 to 9.0+
- **mutillidae**: Update PHP dependencies
- **WebGoat**: Update Java dependencies

---

## **CLOSING (30 seconds)**

### **Summary**
> "In just 10 minutes, we've seen how Legit Security ASPM provides:
> - Unified vulnerability management across all applications
> - Risk-based prioritization that focuses on business impact
> - Cross-application visibility and impact analysis
> - Actionable remediation guidance and verification
> 
> This gives security teams the tools they need to secure their entire application portfolio efficiently and focus on what matters most."

---

## 🎯 **KEY DEMO TIPS**

### **Before the Demo:**
1. **Practice the navigation** - know where each section is
2. **Identify 2-3 specific vulnerabilities** to focus on
3. **Prepare the Flask fix** in advance (update requirements.txt)
4. **Test your internet connection** and Legit Security access

### **During the Demo:**
1. **Keep moving** - don't get stuck on one vulnerability
2. **Use the "wow" moments** - show risk reduction after fixes
3. **Tell a story** - connect the technical details to business value
4. **Be prepared to skip** sections if you're running short on time

### **If Something Goes Wrong:**
1. **Have screenshots** ready as backup
2. **Know your key talking points** even without the UI
3. **Focus on the business value** rather than technical details
4. **Be honest** - "Let me show you this feature" if something doesn't work

---

## 📊 **DEMO METRICS TO HIGHLIGHT**

- **5 different application types** (Python, Node.js, PHP, Java)
- **Unified vulnerability dashboard** across all applications
- **Risk-based prioritization** vs. traditional CVSS scoring
- **Cross-application impact** analysis
- **Live remediation** demonstration
- **Business-focused** security management

---

## 🚀 **SUCCESS METRICS**

Your demo is successful if the audience understands:
1. **Unified visibility** - one platform for all applications
2. **Smart prioritization** - business-focused risk assessment
3. **Actionable remediation** - clear next steps for fixes
4. **Complete lifecycle** - from discovery to verification

**Good luck with your demo!** 🎯
