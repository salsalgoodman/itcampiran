# Get Supabase Access Token

After completing browser authentication, you need to get the access token:

## Method 1: From Supabase Dashboard
1. Go to https://app.supabase.com
2. Click on your profile (top right)
3. Go to "Access Tokens" or "API Settings"
4. Create a new access token or copy an existing one
5. The token format should be: `sbp_0102...1920`

## Method 2: Complete CLI Login Flow
1. Run: `npx --yes supabase login`
2. Press Enter to open browser
3. Complete authentication in browser
4. The token will be automatically saved

## Method 3: Use Access Token Directly
Once you have the token, run:
```bash
npx --yes supabase login --token YOUR_ACCESS_TOKEN
```

Then we can proceed with linking and executing the schema.

