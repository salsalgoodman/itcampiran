# -*- coding: utf-8 -*-
"""
Run bot in background (Windows)
"""

import subprocess
import sys
import os

def run_in_background():
    """Run bot as background process"""
    # Use START command on Windows to run in new window
    script_path = os.path.abspath("workshop_signup_bot.py")
    
    print("="*70)
    print("Starting bot in background window...")
    print("="*70)
    print("\nThe bot will run in a separate window.")
    print("You can close this terminal - the bot will keep running.")
    print("\nTo stop the bot, close the bot window or use Task Manager.")
    print("="*70)
    
    # Start in new window (Windows)
    subprocess.Popen(
        f'start "Workshop Bot" python "{script_path}"',
        shell=True
    )
    
    print("\n✅ Bot started in background!")
    print("   Check the new window for bot status.")

if __name__ == '__main__':
    run_in_background()

