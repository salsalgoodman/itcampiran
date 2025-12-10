# -*- coding: utf-8 -*-
"""
Deploy bot to Render using Render CLI
This script automates the deployment process
"""

import os
import subprocess
import json
import sys

def run_command(cmd, check=True):
    """Run a shell command"""
    print(f"🔧 Running: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=check
        )
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False, "", str(e)

def check_render_cli():
    """Check if Render CLI is installed"""
    print("🔍 Checking Render CLI installation...")
    success, stdout, stderr = run_command("render --version", check=False)
    if success:
        print(f"✅ Render CLI found: {stdout.strip()}")
        return True
    else:
        print("❌ Render CLI not found!")
        print("\n📥 Please install Render CLI:")
        print("   Option 1: npm install -g @render/cli")
        print("   Option 2: choco install render-cli (if you have Chocolatey)")
        print("   Option 3: Run setup_render_cli.ps1")
        return False

def check_git_repo():
    """Check if git repo is initialized and has remote"""
    print("\n🔍 Checking Git repository...")
    
    # Check if git is initialized
    success, _, _ = run_command("git rev-parse --git-dir", check=False)
    if not success:
        print("❌ Git repository not initialized!")
        print("   Run: git init")
        return False
    
    # Check if remote exists
    success, stdout, _ = run_command("git remote -v", check=False)
    if not success or not stdout.strip():
        print("⚠️  No remote repository configured")
        print("   You need to add GitHub remote first:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git")
        return False
    
    print("✅ Git repository configured")
    return True

def create_render_yaml():
    """Create render.yaml configuration file"""
    print("\n📝 Creating render.yaml configuration...")
    
    render_config = """services:
  - type: worker
    name: workshop-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python workshop_signup_bot.py
    envVars:
      - key: BOT_TOKEN
        sync: false
      - key: SUPABASE_URL
        sync: false
      - key: SUPABASE_KEY
        sync: false
      - key: ADMIN_IDS
        sync: false
      - key: ZARINPAL_URL
        sync: false
      - key: ZARINPAL_URL_ECONOMY
        sync: false
      - key: ZARINPAL_URL_STANDARD
        sync: false
      - key: ZARINPAL_URL_PROFESSIONAL
        sync: false
      - key: BANK_NAME
        sync: false
      - key: BANK_ACCOUNT
        sync: false
      - key: ACCOUNT_HOLDER
        sync: false
"""
    
    with open("render.yaml", "w", encoding="utf-8") as f:
        f.write(render_config)
    
    print("✅ render.yaml created")
    return True

def main():
    print("=" * 70)
    print("🚀 Render CLI Deployment Script")
    print("=" * 70)
    print()
    
    # Step 1: Check Render CLI
    if not check_render_cli():
        print("\n❌ Please install Render CLI first and run this script again")
        sys.exit(1)
    
    # Step 2: Check Git
    git_ok = check_git_repo()
    if not git_ok:
        print("\n⚠️  Git repository not fully configured")
        print("   Please configure GitHub remote and run again")
        sys.exit(1)
    
    # Step 3: Create render.yaml
    if not os.path.exists("render.yaml"):
        create_render_yaml()
    else:
        print("\n✅ render.yaml already exists")
    
    # Step 4: Login to Render
    print("\n🔐 Step 1: Login to Render")
    print("   Run: render login")
    print("   This will open a browser for authentication")
    input("\n   Press Enter after you've logged in...")
    
    # Step 5: Deploy
    print("\n🚀 Step 2: Deploying to Render...")
    print("   This will create a new service on Render")
    
    # Check if service already exists
    success, stdout, _ = run_command("render services list", check=False)
    if success and "workshop-bot" in stdout:
        print("⚠️  Service 'workshop-bot' already exists")
        response = input("   Do you want to update it? (y/n): ")
        if response.lower() == 'y':
            print("\n📤 Updating service...")
            run_command("render deploy")
        else:
            print("   Skipping deployment")
    else:
        print("\n📤 Creating new service...")
        print("   Run: render deploy")
        print("   Or use: render services:create")
    
    print("\n" + "=" * 70)
    print("✅ Setup complete!")
    print("=" * 70)
    print("\n📋 Next steps:")
    print("1. Make sure you're logged in: render login")
    print("2. Set environment variables in Render dashboard")
    print("3. Deploy: render deploy")
    print("\n💡 Tip: You can also use Render dashboard for easier setup")

if __name__ == "__main__":
    main()

