@echo off
REM Re-enable Windows sleep mode

echo Re-enabling Windows sleep mode...
echo.

REM Set sleep timeout to 30 minutes
powercfg /change standby-timeout-ac 30
powercfg /change hibernate-timeout-ac 30

echo.
echo ✅ Sleep mode re-enabled!
echo    PC will sleep after 30 minutes of inactivity.
echo.
pause

