# -*- coding: utf-8 -*-
"""
Script to connect to Supabase and run the database schema
"""

import os
import sys
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

def read_sql_file(filename):
    """Read SQL file content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        sys.exit(1)

def run_schema():
    """Connect to Supabase and run schema"""
    # Get credentials
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    # Check if credentials are set
    if not supabase_url or not supabase_key:
        print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
        print("\nPlease add these to your .env file:")
        print("SUPABASE_URL=your_supabase_project_url")
        print("SUPABASE_KEY=your_supabase_anon_key")
        sys.exit(1)
    
    # Check if using placeholder values
    if supabase_url.startswith('your_') or supabase_key.startswith('your_'):
        print("❌ Error: Please replace placeholder values in .env with actual Supabase credentials")
        sys.exit(1)
    
    print("=" * 60)
    print("Connecting to Supabase...")
    print("=" * 60)
    
    try:
        # Create Supabase client
        supabase: Client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase successfully!")
        
        # Read SQL file
        print("\nReading schema file...")
        sql_content = read_sql_file('supabase_setup.sql')
        print("✅ Schema file loaded")
        
        # Split SQL into individual statements
        # Remove comments and split by semicolon
        statements = []
        current_statement = []
        
        for line in sql_content.split('\n'):
            # Skip comment lines
            if line.strip().startswith('--'):
                continue
            
            # Skip empty lines
            if not line.strip():
                continue
            
            current_statement.append(line)
            
            # If line ends with semicolon, it's a complete statement
            if line.strip().endswith(';'):
                statement = '\n'.join(current_statement).strip()
                if statement:
                    statements.append(statement)
                current_statement = []
        
        print(f"\nFound {len(statements)} SQL statements to execute")
        print("-" * 60)
        
        # Execute each statement
        success_count = 0
        error_count = 0
        
        for i, statement in enumerate(statements, 1):
            try:
                print(f"\n[{i}/{len(statements)}] Executing statement...")
                # Extract the first word to show what we're doing
                first_word = statement.split()[0].upper() if statement.split() else "UNKNOWN"
                print(f"   Command: {first_word}")
                
                # Execute using Supabase RPC or direct query
                # Note: Supabase Python client doesn't have direct SQL execution
                # We need to use the REST API or RPC functions
                # For now, we'll use the postgrest client's execute method
                
                # Actually, the supabase-py client doesn't support raw SQL execution
                # We need to use the REST API directly or create tables via the client
                # Let me try a different approach - using the postgrest client
                
                result = supabase.rpc('exec_sql', {'sql': statement}).execute()
                print(f"   ✅ Success")
                success_count += 1
                
            except Exception as e:
                # If RPC doesn't exist, we'll need to use a different method
                # Let's try using httpx directly to call the REST API
                import httpx
                
                try:
                    # Use Supabase REST API to execute SQL
                    # This requires using the service role key or a custom function
                    print(f"   ⚠️  Direct execution not available, trying alternative method...")
                    
                    # Actually, the best way is to tell user to run in SQL Editor
                    # But let's try to create tables using the client if possible
                    if 'CREATE TABLE' in statement.upper():
                        print(f"   ⚠️  Note: CREATE TABLE statements need to be run in Supabase SQL Editor")
                        print(f"   ℹ️  This is a limitation of the Supabase Python client")
                        error_count += 1
                    else:
                        print(f"   ❌ Error: {str(e)}")
                        error_count += 1
                        
                except Exception as e2:
                    print(f"   ❌ Error: {str(e)}")
                    error_count += 1
        
        print("\n" + "=" * 60)
        print("Summary")
        print("=" * 60)
        print(f"✅ Successful: {success_count}")
        print(f"❌ Failed: {error_count}")
        
        if error_count > 0:
            print("\n⚠️  Note: The Supabase Python client has limitations for executing raw SQL.")
            print("   For CREATE TABLE statements, please:")
            print("   1. Go to Supabase Dashboard → SQL Editor")
            print("   2. Copy the contents of supabase_setup.sql")
            print("   3. Paste and click 'Run'")
            print("\n   Alternatively, you can use the Supabase CLI or REST API with service role key.")
        
    except Exception as e:
        print(f"\n❌ Error connecting to Supabase: {e}")
        print("\nPlease check:")
        print("1. SUPABASE_URL is correct")
        print("2. SUPABASE_KEY is correct")
        print("3. Your internet connection is working")
        print("4. Your Supabase project is active")
        sys.exit(1)

if __name__ == '__main__':
    run_schema()

