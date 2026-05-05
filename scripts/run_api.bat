@echo off
echo Starting IntelliGuard API...
cd /d "C:\Users\SANAD\makemore"
start http://127.0.0.1:8000/docs
python main.py
pause
