# 🔍 ASPM Filtering Troubleshooting Guide
## How to Successfully Identify Cross-Application Vulnerabilities

### Current Filter Analysis
Your current filter:
- **Dependencies**: Name contains "express"
- **Linked Repositories**: Name is one of 5 repositories
- **Associated Issues**: Status is "Open" AND CVE ID is "CVE-2022-24999"

### Potential Issues & Solutions

#### **Issue 1: Filter Too Specific**
**Problem**: Looking for exact CVE-2022-24999 might miss other Express vulnerabilities
**Solution**: Try these alternative filters:

**Option A: Remove CVE specificity**
```
Dependencies: Name contains "express"
Linked Repositories: [All repositories]
Associated Issues: Status is "Open" AND Severity is "Critical" OR "High"
```

**Option B: Broaden CVE search**
```
Dependencies: Name contains "express"
Linked Repositories: [All repositories]
Associated Issues: Status is "Open" AND CVE ID contains "CVE-2022"
```

#### **Issue 2: Repository Limitation**
**Problem**: "5 repositories" might not show which specific ones are affected
**Solution**: Try these approaches:

**Option A: Show all repositories**
```
Dependencies: Name contains "express"
Linked Repositories: [Remove repository filter]
Associated Issues: Status is "Open" AND Severity is "Critical" OR "High"
```

**Option B: Group by repository**
```
Dependencies: Name contains "express"
Linked Repositories: [All repositories]
Associated Issues: Status is "Open" AND Severity is "Critical" OR "High"
Group By: Repository Name
```

#### **Issue 3: Status Filter Too Restrictive**
**Problem**: "Open" status might exclude other relevant vulnerabilities
**Solution**: Try these alternatives:

**Option A: Remove status filter**
```
Dependencies: Name contains "express"
Linked Repositories: [All repositories]
Associated Issues: Severity is "Critical" OR "High"
```

**Option B: Include multiple statuses**
```
Dependencies: Name contains "express"
Linked Repositories: [All repositories]
Associated Issues: Status is "Open" OR "New" OR "Reopened" AND Severity is "Critical" OR "High"
```

### Alternative Filtering Strategies

#### **Strategy 1: Vulnerability-First Approach**
```
Issues: Severity is "Critical" OR "High"
Linked Repositories: [Show all repositories]
Dependencies: [Show all affected dependencies]
Group By: CVE ID
```

#### **Strategy 2: Package-First Approach**
```
Dependencies: Name contains "express" OR "axios" OR "flask"
Linked Repositories: [All repositories]
Associated Issues: Severity is "Critical" OR "High"
Group By: Package Name
```

#### **Strategy 3: OWASP Category Approach**
```
Issues: OWASP Category is "A06: Vulnerable Components" AND Severity is "Critical" OR "High"
Linked Repositories: [All repositories]
Dependencies: [Show all affected dependencies]
Group By: OWASP Category
```

#### **Strategy 4: Cross-Application Impact Approach**
```
Issues: Severity is "Critical" OR "High"
Linked Repositories: [All repositories]
Dependencies: [Show all affected dependencies]
Show: Only vulnerabilities affecting 2+ repositories
```

### Step-by-Step Testing Process

#### **Step 1: Test Basic Package Filter**
1. Remove all filters except:
   - Dependencies: Name contains "express"
   - Associated Issues: Severity is "Critical" OR "High"
2. Check if you see any results
3. If yes, note which repositories are affected

#### **Step 2: Test CVE Filter**
1. Keep the basic filter from Step 1
2. Add: CVE ID contains "CVE-2022"
3. Check if you see cross-application results
4. If yes, note the specific CVEs and affected repositories

#### **Step 3: Test Repository Grouping**
1. Use the filter from Step 2
2. Add: Group By Repository Name
3. Check if you can see which repositories are affected by each vulnerability

#### **Step 4: Test Cross-Application Filter**
1. Use: Issues affecting 2+ repositories
2. Filter by: Severity is "Critical" OR "High"
3. Check if you see vulnerabilities spanning multiple applications

### Expected Results for Cross-Application Vulnerabilities

#### **Express.js Vulnerabilities**
- **CVE-2022-24999**: Should appear in juice-shop, NodeGoat, LS-DEMO
- **CVE-2022-24998**: Should appear in juice-shop, NodeGoat, LS-DEMO
- **Other Express CVEs**: Should show cross-application impact

#### **Axios Vulnerabilities**
- **CVE-2021-3749**: Should appear in juice-shop, NodeGoat, LS-DEMO
- **CVE-2021-3748**: Should appear in juice-shop, NodeGoat, LS-DEMO

#### **Flask Vulnerabilities**
- **CVE-2018-1000656**: Should appear in LS-DEMO
- **CVE-2020-26160**: Should appear in LS-DEMO

### Troubleshooting Common Issues

#### **Issue: No Results Found**
**Possible Causes:**
1. Filter too restrictive
2. Data not properly ingested
3. Repository connections not established

**Solutions:**
1. Broaden the filter criteria
2. Check if repositories are properly connected
3. Verify vulnerability data is ingested

#### **Issue: Results Show Single Repository Only**
**Possible Causes:**
1. Filter not showing cross-application view
2. Grouping not enabled
3. Repository correlation not working

**Solutions:**
1. Enable repository grouping
2. Use "affecting multiple repositories" filter
3. Check cross-repository correlation settings

#### **Issue: Too Many Results**
**Possible Causes:**
1. Filter too broad
2. Not focused on critical/high severity
3. Including too many vulnerability types

**Solutions:**
1. Add severity filters
2. Focus on specific packages
3. Use cross-application impact filters

### Verification Checklist

#### **✅ Cross-Application Vulnerability Indicators**
- [ ] Same CVE appears in multiple repositories
- [ ] Same package version appears in multiple repositories
- [ ] Vulnerability severity is Critical or High
- [ ] Repository grouping shows multiple affected applications
- [ ] Risk assessment considers cross-application impact

#### **✅ Expected Cross-Application Vulnerabilities**
- [ ] Express.js vulnerabilities in Node.js applications
- [ ] Axios vulnerabilities in HTTP client usage
- [ ] Flask vulnerabilities in Python applications
- [ ] OWASP Top 10 issues spanning multiple technology stacks

### Next Steps if Still Not Working

#### **Option 1: Contact ASPM Support**
- Provide your current filter configuration
- Ask about cross-application vulnerability correlation
- Request guidance on repository grouping

#### **Option 2: Manual Verification**
- Check each repository individually for Express vulnerabilities
- Compare CVE IDs across repositories
- Look for shared package versions

#### **Option 3: Alternative Approach**
- Use dependency analysis tools
- Generate SBOM reports
- Cross-reference vulnerability databases

### Success Criteria

You'll know the filtering is working when you see:
1. **Same CVE in multiple repositories**
2. **Same package version in multiple repositories**
3. **Cross-application risk assessment**
4. **Repository grouping showing affected applications**
5. **Unified vulnerability management across applications**

This indicates that your ASPM tool is properly correlating vulnerabilities across your application portfolio.
