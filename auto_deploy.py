# -*- coding: utf-8 -*-
"""
Automated deployment script
Helps push to GitHub and deploy to Render
"""

import os
import subprocess
import sys

def run_command(cmd, check=True, show_output=True):
    """Run a shell command"""
    if show_output:
        print(f"\n🔧 {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=check
        )
        if show_output and result.stdout:
            print(result.stdout)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        if show_output:
            print(f"❌ Error: {e}")
            if e.stderr:
                print(f"Error: {e.stderr}")
        return False, "", str(e)

def check_git_status():
    """Check git status"""
    print("🔍 Checking Git status...")
    success, stdout, _ = run_command("git status --short", check=False)
    if stdout.strip():
        print("📝 Uncommitted changes found:")
        print(stdout)
        return False
    print("✅ All changes committed")
    return True

def push_to_github():
    """Push code to GitHub"""
    print("\n📤 Pushing to GitHub...")
    
    # Check if remote exists
    success, stdout, _ = run_command("git remote -v", check=False, show_output=False)
    if not success or not stdout.strip():
        print("❌ No GitHub remote configured!")
        print("\n📋 Please run these commands:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git")
        print("   git branch -M main")
        return False
    
    # Push
    success, _, _ = run_command("git push -u origin main", check=False)
    if success:
        print("✅ Code pushed to GitHub successfully!")
        return True
    else:
        print("⚠️  Push failed. You may need to:")
        print("   1. Create repository on GitHub first")
        print("   2. Authenticate with GitHub")
        print("   3. Try again")
        return False

def deploy_to_render():
    """Deploy to Render using CLI"""
    print("\n🚀 Deploying to Render...")
    
    # Check if Render CLI is installed
    success, _, _ = run_command("render --version", check=False, show_output=False)
    if not success:
        print("❌ Render CLI not installed!")
        print("\n📥 Install Render CLI:")
        print("   npm install -g @render/cli")
        print("   Or run: setup_render_cli.ps1")
        return False
    
    # Check if logged in
    success, _, _ = run_command("render whoami", check=False, show_output=False)
    if not success:
        print("⚠️  Not logged in to Render")
        print("   Run: render login")
        return False
    
    # Deploy
    print("📤 Deploying...")
    success, stdout, stderr = run_command("render deploy", check=False)
    if success:
        print("✅ Deployment successful!")
        return True
    else:
        print("⚠️  Deployment may need manual configuration")
        print("   Check Render dashboard: https://dashboard.render.com")
        return False

def main():
    print("=" * 70)
    print("🤖 Automated Deployment Script")
    print("=" * 70)
    
    # Step 1: Check git status
    if not check_git_status():
        print("\n⚠️  You have uncommitted changes")
        response = input("   Commit them now? (y/n): ")
        if response.lower() == 'y':
            message = input("   Commit message (or press Enter for default): ")
            if not message:
                message = "Update bot code"
            run_command(f'git commit -am "{message}"')
        else:
            print("   Please commit changes first")
            sys.exit(1)
    
    # Step 2: Push to GitHub
    print("\n" + "=" * 70)
    print("📤 Step 1: Push to GitHub")
    print("=" * 70)
    
    github_ok = push_to_github()
    if not github_ok:
        print("\n⚠️  GitHub push failed. Please:")
        print("   1. Create repository on GitHub")
        print("   2. Add remote: git remote add origin https://github.com/USER/REPO.git")
        print("   3. Run this script again")
        sys.exit(1)
    
    # Step 3: Deploy to Render
    print("\n" + "=" * 70)
    print("🚀 Step 2: Deploy to Render")
    print("=" * 70)
    
    render_ok = deploy_to_render()
    if not render_ok:
        print("\n💡 Alternative: Use Render Dashboard")
        print("   1. Go to https://dashboard.render.com")
        print("   2. New + → Background Worker")
        print("   3. Connect your GitHub repository")
        print("   4. Configure and deploy")
    
    print("\n" + "=" * 70)
    print("✅ Process complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()

