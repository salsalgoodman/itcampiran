@echo off
REM Prevent Windows from going to sleep
REM Run as Administrator for best results

echo Preventing Windows sleep mode...
echo.

REM Set sleep timeout to never (0 = never)
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
powercfg /change monitor-timeout-ac 10

echo.
echo ✅ Sleep mode disabled!
echo    PC will not go to sleep while plugged in.
echo.
echo To re-enable sleep mode:
echo    powercfg /change standby-timeout-ac 30
echo    (30 = sleep after 30 minutes)
echo.
pause

