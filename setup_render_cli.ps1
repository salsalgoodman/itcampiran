# PowerShell script to install Render CLI
Write-Host "Installing Render CLI..." -ForegroundColor Green

# Check if chocolatey is installed
if (Get-Command choco -ErrorAction SilentlyContinue) {
    Write-Host "Using Chocolatey to install Render CLI..." -ForegroundColor Yellow
    choco install render-cli -y
} else {
    Write-Host "Chocolatey not found. Installing via npm..." -ForegroundColor Yellow
    
    # Check if npm is installed
    if (Get-Command npm -ErrorAction SilentlyContinue) {
        npm install -g @render/cli
    } else {
        Write-Host "npm not found. Please install Render CLI manually:" -ForegroundColor Red
        Write-Host "1. Install Node.js from https://nodejs.org" -ForegroundColor Yellow
        Write-Host "2. Run: npm install -g @render/cli" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Or install Chocolatey and run: choco install render-cli" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "Render CLI installed successfully!" -ForegroundColor Green
Write-Host "Run 'render --version' to verify" -ForegroundColor Cyan

