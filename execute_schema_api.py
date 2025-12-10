# -*- coding: utf-8 -*-
"""
Execute schema using Supabase REST API
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def get_project_info():
    """Get project info from CLI"""
    import subprocess
    import json
    
    try:
        result = subprocess.run(
            "npx --yes supabase status --output json",
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except:
        pass
    return None

def execute_sql_via_api(sql_content, project_url, api_key):
    """Execute SQL via Supabase Management API"""
    # Note: Direct SQL execution via REST API requires service role key
    # For now, we'll use the SQL Editor approach or create a migration
    
    print("⚠️  Direct SQL execution via REST API requires service role key")
    print("   Using migration approach instead...")
    return False

def main():
    print("="*70)
    print("Executing Schema via Migration")
    print("="*70)
    
    # Check if migration file exists
    migration_file = "supabase/migrations/20251130212146_initial_schema.sql"
    
    if not os.path.exists(migration_file):
        print(f"❌ Migration file not found: {migration_file}")
        return
    
    print(f"✅ Migration file found: {migration_file}")
    
    # Try db push
    import subprocess
    print("\n🚀 Pushing migration to database...")
    
    result = subprocess.run(
        "npx --yes supabase db push",
        shell=True,
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✅ Schema executed successfully!")
        print(result.stdout)
        
        # Get project info
        project_info = get_project_info()
        if project_info:
            project_ref = project_info.get('project_ref', 'npzffoovhbmikjwrzdhw')
            project_url = f"https://{project_ref}.supabase.co"
            print(f"\n📋 Project URL: {project_url}")
            print("\nNext steps:")
            print("1. Get API key from: https://app.supabase.com → Settings → API")
            print("2. Update .env with:")
            print(f"   SUPABASE_URL={project_url}")
            print("   SUPABASE_KEY=your_anon_key_here")
            print("3. Create storage bucket 'receipts' in Supabase Dashboard")
    else:
        print("❌ Migration failed:")
        print(result.stderr)
        print("\n💡 Alternative: Execute SQL manually in SQL Editor")
        print("   Go to: https://app.supabase.com → SQL Editor")

if __name__ == '__main__':
    main()

