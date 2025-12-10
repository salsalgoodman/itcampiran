# -*- coding: utf-8 -*-
"""
Step-by-step Supabase setup using CLI
"""

import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def run_cmd(cmd, description):
    """Run a command and show output"""
    print(f"\n{'='*70}")
    print(f"Step: {description}")
    print(f"{'='*70}")
    print(f"Command: {cmd}")
    print("\n⏳ Running... (This may open a browser for authentication)")
    
    try:
        # Use Popen to allow interaction
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Wait a bit and check if it's still running
        import time
        time.sleep(2)
        
        if process.poll() is None:
            print("✅ Command is running (may require browser authentication)")
            print("   Please complete authentication in your browser")
            print("   Waiting for completion...")
            stdout, stderr = process.communicate()
        else:
            stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            print("✅ Success!")
            if stdout:
                print(stdout)
            return True
        else:
            print(f"⚠️  Exit code: {process.returncode}")
            if stderr:
                print(f"Errors: {stderr}")
            if stdout:
                print(f"Output: {stdout}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("="*70)
    print("Supabase CLI Setup - Step by Step")
    print("="*70)
    
    # Step 1: Login
    print("\n📋 Step 1: Login to Supabase")
    print("   This will open your browser for authentication")
    input("   Press Enter to continue...")
    
    login_success = run_cmd(
        "npx --yes supabase login",
        "Login to Supabase"
    )
    
    if not login_success:
        print("\n⚠️  Login may have failed or requires manual completion")
        print("   You can try running manually: npx --yes supabase login")
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Step 2: Get project info
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    
    if supabase_url and 'supabase.co' in supabase_url:
        try:
            # Extract project ref: https://xxxxx.supabase.co -> xxxxx
            project_ref = supabase_url.split('//')[1].split('.')[0]
            print(f"\n📎 Detected project reference: {project_ref}")
            
            # Step 3: Link project
            print("\n📋 Step 2: Link to your Supabase project")
            input("   Press Enter to continue...")
            
            link_success = run_cmd(
                f"npx --yes supabase link --project-ref {project_ref}",
                f"Link project {project_ref}"
            )
            
            if not link_success:
                print("\n⚠️  Project linking may require manual setup")
                print(f"   Try: npx --yes supabase link --project-ref {project_ref}")
        except:
            print("\n⚠️  Could not extract project reference from SUPABASE_URL")
            print("   Please link manually:")
            print("   npx --yes supabase link --project-ref YOUR_PROJECT_REF")
    
    # Step 4: Execute schema
    print("\n📋 Step 3: Execute database schema")
    print("   This will create the users and receipts tables")
    input("   Press Enter to continue...")
    
    if os.path.exists("supabase_setup.sql"):
        # Try db execute first
        execute_success = run_cmd(
            "npx --yes supabase db execute -f supabase_setup.sql",
            "Execute SQL schema"
        )
        
        if not execute_success:
            # Try db push as alternative
            print("\n💡 Trying alternative method: db push")
            execute_success = run_cmd(
                "npx --yes supabase db push",
                "Push database changes"
            )
        
        if execute_success:
            print("\n" + "="*70)
            print("✅ Schema Setup Complete!")
            print("="*70)
            print("\nNext steps:")
            print("1. Create storage bucket 'receipts' in Supabase Dashboard")
            print("   → Go to Storage → New bucket → Name: receipts → Public")
            print("2. Verify tables were created:")
            print("   → Go to Table Editor in Supabase Dashboard")
            print("3. Configure .env with all your credentials")
            print("4. Run: python workshop_signup_bot.py")
        else:
            print("\n⚠️  Schema execution may need to be done manually")
            print("   Go to: https://app.supabase.com → SQL Editor")
            print("   Copy/paste contents of supabase_setup.sql")
    else:
        print("❌ supabase_setup.sql not found!")

if __name__ == '__main__':
    main()

