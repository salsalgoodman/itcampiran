# -*- coding: utf-8 -*-
"""
Create storage bucket via Supabase API
"""

import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

def create_bucket():
    """Create receipts bucket"""
    supabase_url = os.environ.get("SUPABASE_URL", "").strip()
    supabase_key = os.environ.get("SUPABASE_KEY", "").strip()
    
    if not supabase_url or not supabase_key or 'your_' in supabase_url.lower():
        print("⚠️  SUPABASE_URL and SUPABASE_KEY needed in .env")
        print("\nProject created: npzffoovhbmikjwrzdhw")
        print("Project URL: https://npzffoovhbmikjwrzdhw.supabase.co")
        print("\nTo get API key:")
        print("1. Go to: https://app.supabase.com/project/npzffoovhbmikjwrzdhw/settings/api")
        print("2. Copy 'anon public' key")
        print("3. Add to .env:")
        print("   SUPABASE_URL=https://npzffoovhbmikjwrzdhw.supabase.co")
        print("   SUPABASE_KEY=your_anon_key_here")
        return False
    
    try:
        client = create_client(supabase_url, supabase_key)
        
        # Try to create bucket
        try:
            result = client.storage.create_bucket("receipts", {
                "public": True,
                "allowed_mime_types": ["image/jpeg", "image/png", "image/jpg"],
                "file_size_limit": 10485760  # 10MB
            })
            print("✅ Storage bucket 'receipts' created successfully!")
            return True
        except Exception as e:
            if "already exists" in str(e).lower() or "duplicate" in str(e).lower():
                print("✅ Storage bucket 'receipts' already exists!")
                return True
            else:
                print(f"⚠️  Error creating bucket: {e}")
                print("\n💡 Create bucket manually:")
                print("1. Go to: https://app.supabase.com/project/npzffoovhbmikjwrzdhw/storage/buckets")
                print("2. Click 'New bucket'")
                print("3. Name: receipts")
                print("4. Make it Public")
                print("5. Create")
                return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    print("="*70)
    print("Creating Storage Bucket")
    print("="*70)
    create_bucket()

