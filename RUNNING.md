# Running StudyGenie

This guide provides step-by-step instructions to run the StudyGenie application locally.

## Prerequisites
-   Python 3.x installed
-   Terminal (Mac/Linux/Windows)

## Quick Start (Single Command)

The entire application (Frontend + Backend) runs on **port 2005**.

1.  Open a terminal.
2.  Navigate to the project root:
    ```bash
    cd /Users/chinmayjoshi/Desktop/StudyGenie
    ```
3.  Run the application:
    ```bash
    source backend/venv/bin/activate
    cd backend
    python3 app.py
    ```
4.  Open your browser and go to:
    [http://localhost:2005](http://localhost:2005)

    *(You will be automatically redirected to the Home Page)*

## One-time Setup (If needed)
If you need to recreate the environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Notes
-   To stop the server, press `Ctrl+C` in the terminal.
-   To deactivate the virtual environment, type `deactivate`.
