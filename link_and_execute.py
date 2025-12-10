# -*- coding: utf-8 -*-
"""
Link to Supabase project and execute schema
"""

import subprocess
import sys

def run_cmd(cmd, description):
    """Run a command"""
    print(f"\n{'='*70}")
    print(f"{description}")
    print(f"{'='*70}")
    print(f"Command: {cmd}\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            print("✅ Success!")
            if result.stdout:
                print(result.stdout)
            return True, result.stdout
        else:
            print("❌ Failed")
            if result.stderr:
                print(f"Error: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            return False, result.stderr
    except subprocess.TimeoutExpired:
        print("⏱️  Command timed out")
        return False, "Timeout"
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, str(e)

def main():
    print("="*70)
    print("Link Project and Execute Schema")
    print("="*70)
    
    # Get project ref from user or use first available
    print("\n📋 Available projects:")
    print("1. supabase-lime-village (zwwoyzfxcyjvnmokrzew)")
    print("2. supabase-webdevai-school (sackrqpqkzpofkhjiawi)")
    print("3. supabase-green-mountain (nmvymyymtssygorxtips)")
    print("4. supabase-purple-chair (eoltdxziroohwevxwuwj)")
    print("5. ahlmedia (rhvrbvndpcdqsuzjzwxt)")
    print("6. HOOSHMAN-MANAGEMENT (sgdtcddrxostkepeujet)")
    print("7. supabase-yellow-window (ptpytuhffbsjnxxljztx)")
    print("8. supabase-amber-book (tnpivqszqcarprfsoswt)")
    print("9. supabase-lime-elephant (jneejjvqvddyrkutrwgw)")
    print("10. supabase-hooshman (nfggrireetqvdhidfjjb)")
    
    # Try to get from .env or use a default
    from dotenv import load_dotenv
    import os
    load_dotenv()
    
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    
    if supabase_url and 'supabase.co' in supabase_url and 'your_' not in supabase_url.lower():
        try:
            project_ref = supabase_url.split('//')[1].split('.')[0]
            print(f"\n✅ Using project from .env: {project_ref}")
        except:
            project_ref = None
    else:
        # Use the most recent project (last in list)
        project_ref = "nfggrireetqvdhidfjjb"  # supabase-hooshman
        print(f"\n💡 Using most recent project: {project_ref} (supabase-hooshman)")
        print("   (You can change this by setting SUPABASE_URL in .env)")
    
    if not project_ref:
        print("\n❌ Could not determine project reference")
        print("   Please set SUPABASE_URL in .env or specify project ref")
        return
    
    # Step 1: Link project
    success, output = run_cmd(
        f"npx --yes supabase link --project-ref {project_ref}",
        f"Linking to project: {project_ref}"
    )
    
    if not success:
        print("\n⚠️  Project linking failed. Trying to continue anyway...")
        # Check if already linked
        check_result = subprocess.run(
            "npx --yes supabase status",
            shell=True,
            capture_output=True,
            text=True
        )
        if check_result.returncode == 0:
            print("✅ Project appears to be linked already")
        else:
            print("❌ Cannot proceed without linking")
            return
    
    # Step 2: Execute schema
    print("\n" + "="*70)
    print("Executing Database Schema")
    print("="*70)
    
    if not os.path.exists("supabase_setup.sql"):
        print("❌ supabase_setup.sql not found!")
        return
    
    success, output = run_cmd(
        "npx --yes supabase db execute -f supabase_setup.sql",
        "Executing SQL schema"
    )
    
    if success:
        print("\n" + "="*70)
        print("✅ Schema Execution Complete!")
        print("="*70)
        print("\nNext steps:")
        print("1. Create storage bucket 'receipts' in Supabase Dashboard")
        print("   → Go to Storage → New bucket → Name: receipts → Public")
        print("2. Update .env with your SUPABASE_URL:")
        print(f"   SUPABASE_URL=https://{project_ref}.supabase.co")
        print("3. Run: python setup_check.py to verify")
        print("4. Run: python workshop_signup_bot.py to start bot")
    else:
        # Try alternative method
        print("\n💡 Trying alternative: db push")
        success2, output2 = run_cmd(
            "npx --yes supabase db push",
            "Pushing database changes"
        )
        
        if not success2:
            print("\n⚠️  Both methods failed. Please execute SQL manually:")
            print("   Go to: https://app.supabase.com → SQL Editor")
            print("   Copy contents of supabase_setup.sql and run it")

if __name__ == '__main__':
    main()

