@echo off
title IntelliGuard Full Stack
color 0A
echo.
echo  ============================================
echo   IntelliGuard Full Stack Launcher
echo   Backend: http://127.0.0.1:8000
echo   Frontend: http://127.0.0.1:8501
echo  ============================================
echo.

:: Start Backend API (IntelliGuard FastAPI)
echo [1/2] Starting IntelliGuard API (port 8000)...
start "IntelliGuard-API" cmd /k "cd /d C:\Users\SANAD\IntelliGuard\scripts && python -m uvicorn main:app --host 127.0.0.1 --port 8000"

:: Wait for backend to load models
echo      Waiting 15 seconds for models to load...
timeout /t 15 /nobreak >nul

:: Start Frontend (Streamlit RAG Portal)
echo [2/2] Starting RAG Portal (port 8501)...
start "IntelliGuard-Portal" cmd /k "cd /d C:\Users\SANAD\IntelliGuard && python -m streamlit run rag_portal.py --server.port 8501"

:: Wait and open browser
timeout /t 5 /nobreak >nul
echo.
echo  ============================================
echo   All services running!
echo   Opening portal in browser...
echo  ============================================
echo.
start http://localhost:8501

echo Press any key to stop all services...
pause >nul

:: Cleanup
taskkill /FI "WINDOWTITLE eq IntelliGuard-API*" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq IntelliGuard-Portal*" /F >nul 2>&1
echo Services stopped.
