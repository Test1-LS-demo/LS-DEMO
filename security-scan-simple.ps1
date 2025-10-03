# Security Scanning Script for ASPM Testing
Write-Host "Starting Security Scanning for ASPM Testing..." -ForegroundColor Green

# Function to run security scan on a repository
function Invoke-SecurityScan {
    param(
        [string]$RepoName,
        [string]$RepoPath
    )
    
    Write-Host "Scanning $RepoName..." -ForegroundColor Yellow
    
    # Create security scan directory
    $scanDir = "$RepoPath/security-scans"
    if (!(Test-Path $scanDir)) {
        New-Item -ItemType Directory -Path $scanDir -Force
    }
    
    # Generate timestamp
    $timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
    
    # Check for package files and run appropriate scans
    if (Test-Path "$RepoPath/package.json") {
        Write-Host "  Found Node.js project - running npm audit..." -ForegroundColor Cyan
        Set-Location $RepoPath
        npm audit --json > "$scanDir/npm-audit-$timestamp.json" 2>&1
    }
    
    if (Test-Path "$RepoPath/requirements.txt") {
        Write-Host "  Found Python project - running safety check..." -ForegroundColor Cyan
        Set-Location $RepoPath
        pip install safety
        safety check --json > "$scanDir/safety-check-$timestamp.json" 2>&1
    }
    
    Write-Host "  Security scan completed for $RepoName" -ForegroundColor Green
}

# Define repositories
$repositories = @(
    @{Name="LS-DEMO"; Path="LS-DEMO"},
    @{Name="WebGoat"; Path="WebGoat"},
    @{Name="juice-shop"; Path="juice-shop"},
    @{Name="mutillidae"; Path="mutillidae"},
    @{Name="NodeGoat"; Path="NodeGoat"}
)

# Run security scans on all repositories
foreach ($repo in $repositories) {
    if (Test-Path $repo.Path) {
        Invoke-SecurityScan -RepoName $repo.Name -RepoPath $repo.Path
    } else {
        Write-Host "Repository $($repo.Name) not found at $($repo.Path)" -ForegroundColor Red
    }
}

Write-Host "Security scanning completed! Check the 'security-scans' directories in each repository for results." -ForegroundColor Green
