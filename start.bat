@echo off
chcp 65001 >nul

echo ========================================
echo      英语单词记忆小程序启动中...
echo ========================================
echo.

rem 检测Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未检测到Python环境!
    echo.
    echo 请先安装Python 3.6或更高版本:
    echo 下载地址: https://www.python.org/downloads/
    echo 安装时请勾选 "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo 检测到Python环境，启动程序...
echo.

rem 获取当前目录的绝对路径
set "CURRENT_DIR=%~dp0"

rem 切换到当前目录
cd /d "%CURRENT_DIR%"

echo 当前工作目录: %CD%
echo 程序文件: %CURRENT_DIR%vocab_trainer.py
echo.

rem 直接使用python命令启动，避免pythonw的路径问题
start "英语单词记忆训练" python vocab_trainer.py

echo 程序已启动，请检查桌面是否有程序窗口。
echo.
timeout /t 2 /nobreak >nul

