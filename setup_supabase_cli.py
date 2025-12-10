# -*- coding: utf-8 -*-
"""
Setup Supabase CLI and execute schema
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(cmd, check=True):
    """Run a shell command"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=check
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

def install_supabase_cli():
    """Try to install Supabase CLI"""
    print("=" * 70)
    print("Installing Supabase CLI")
    print("=" * 70)
    
    # Try npx approach (works without global install)
    print("\n📦 Using npx to run Supabase CLI (no installation needed)...")
    
    # Test if npx works
    success, stdout, stderr = run_command("npx --version", check=False)
    if success:
        print("✅ npx is available")
        return "npx"
    
    print("❌ npx not available")
    return None

def login_to_supabase(use_npx=False):
    """Login to Supabase"""
    print("\n" + "=" * 70)
    print("Supabase Login")
    print("=" * 70)
    
    if use_npx:
        cmd = "npx --yes supabase login"
    else:
        cmd = "supabase login"
    
    print(f"\n🔐 Running: {cmd}")
    print("   This will open a browser for authentication...")
    
    success, stdout, stderr = run_command(cmd, check=False)
    
    if success:
        print("✅ Login successful!")
        return True
    else:
        print(f"⚠️  Login command output: {stdout}")
        print(f"   Errors: {stderr}")
        return False

def link_project(use_npx=False):
    """Link to Supabase project"""
    print("\n" + "=" * 70)
    print("Link Supabase Project")
    print("=" * 70)
    
    # Get project ref from .env if available
    from dotenv import load_dotenv
    load_dotenv()
    
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    
    if supabase_url and 'supabase.co' in supabase_url:
        # Extract project ref from URL
        # URL format: https://xxxxx.supabase.co
        try:
            project_ref = supabase_url.split('//')[1].split('.')[0]
            print(f"\n📎 Detected project ref: {project_ref}")
            
            if use_npx:
                cmd = f"npx --yes supabase link --project-ref {project_ref}"
            else:
                cmd = f"supabase link --project-ref {project_ref}"
            
            print(f"🔗 Running: {cmd}")
            success, stdout, stderr = run_command(cmd, check=False)
            
            if success:
                print("✅ Project linked!")
                return True
            else:
                print(f"⚠️  Link output: {stdout}")
                print(f"   Errors: {stderr}")
                print("\n   You may need to link manually:")
                print(f"   {cmd}")
                return False
        except:
            print("⚠️  Could not extract project ref from URL")
            print("   Please link manually:")
            if use_npx:
                print("   npx --yes supabase link --project-ref YOUR_PROJECT_REF")
            else:
                print("   supabase link --project-ref YOUR_PROJECT_REF")
            return False
    else:
        print("⚠️  SUPABASE_URL not found in .env")
        print("   Please link manually:")
        if use_npx:
            print("   npx --yes supabase link --project-ref YOUR_PROJECT_REF")
        else:
            print("   supabase link --project-ref YOUR_PROJECT_REF")
        return False

def execute_schema(use_npx=False):
    """Execute SQL schema"""
    print("\n" + "=" * 70)
    print("Executing Schema")
    print("=" * 70)
    
    sql_file = "supabase_setup.sql"
    
    if not os.path.exists(sql_file):
        print(f"❌ {sql_file} not found!")
        return False
    
    if use_npx:
        cmd = f'npx --yes supabase db execute -f {sql_file}'
    else:
        cmd = f'supabase db execute -f {sql_file}'
    
    print(f"\n🚀 Running: {cmd}")
    success, stdout, stderr = run_command(cmd, check=False)
    
    if success:
        print("✅ Schema executed successfully!")
        print(stdout)
        return True
    else:
        print(f"⚠️  Execution output: {stdout}")
        print(f"   Errors: {stderr}")
        
        # Alternative: use db push if execute doesn't work
        print("\n💡 Trying alternative method: db push...")
        if use_npx:
            cmd2 = "npx --yes supabase db push"
        else:
            cmd2 = "supabase db push"
        
        success2, stdout2, stderr2 = run_command(cmd2, check=False)
        if success2:
            print("✅ Schema pushed successfully!")
            return True
        else:
            print("❌ Both methods failed")
            print("\n   Please execute SQL manually in Supabase SQL Editor:")
            print("   https://app.supabase.com → SQL Editor")
            return False

def main():
    print("=" * 70)
    print("Supabase CLI Setup and Schema Execution")
    print("=" * 70)
    
    # Try to use npx
    cli_method = install_supabase_cli()
    
    if not cli_method:
        print("\n❌ Could not set up Supabase CLI")
        print("\n   Please install manually:")
        print("   1. Install Scoop: https://scoop.sh")
        print("   2. Run: scoop install supabase")
        print("   OR")
        print("   Use npx: npx --yes supabase <command>")
        return
    
    use_npx = (cli_method == "npx")
    
    # Login
    if not login_to_supabase(use_npx):
        print("\n⚠️  Login may require manual interaction")
        print("   Please run login command manually if needed")
    
    # Link project
    if not link_project(use_npx):
        print("\n⚠️  Project linking may require manual setup")
    
    # Execute schema
    if execute_schema(use_npx):
        print("\n" + "=" * 70)
        print("✅ Schema Setup Complete!")
        print("=" * 70)
        print("\nNext steps:")
        print("1. Create storage bucket 'receipts' in Supabase Dashboard")
        print("2. Make it public")
        print("3. Configure .env with your credentials")
        print("4. Run: python workshop_signup_bot.py")
    else:
        print("\n" + "=" * 70)
        print("⚠️  Schema execution needs manual steps")
        print("=" * 70)
        print("\nPlease run SQL manually:")
        print("1. Go to: https://app.supabase.com → SQL Editor")
        print("2. Copy contents of supabase_setup.sql")
        print("3. Paste and click 'Run'")

if __name__ == '__main__':
    main()

