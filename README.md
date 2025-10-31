# 🚀 How to Clone & Run the API

This guide will walk you through cloning the project, setting up the Python virtual environment, and running the FastAPI server.

### Prerequisites

Before you start, make sure you have the following installed on your computer:
* **Git**
* **Python 3.8** or newer
* **FFmpeg** (This is a system-level install, *not* a Python package. You may need to use `brew install ffmpeg` on macOS or download it for Windows.)

---

## 1. 📥 Clone the Project

First, get the code from your team's repository.

1.  Open your terminal.
2.  Clone the repository (replace the URL with your team's actual Git URL):
    ```bash
    git clone [https://github.com/bikilaketema/dynamic-ad-platform.git](https://github.com/bikilaketema/dynamic-ad-platform.git)
    ```
3.  Move into the new project folder:
    ```bash
    cd dynamic-ad-platform
    ```

---

## 2. 🐍 Create the Virtual Environment

Next, create a "bubble" (virtual environment) to hold all your Python packages. This prevents conflicts with other projects.

1.  Create the virtual environment (we'll call it `venv`):
    ```bash
    python3 -m venv venv
    ```
2.  **Activate** the environment. This is a critical step!

    * **On macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
    * **On Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    
    You'll know it worked because your terminal prompt will now show **`(venv)`** at the beginning.

---

## 3. 📦 Install Dependencies

With your virtual environment active, you can now install all the necessary libraries.

1.  Your project should have a `requirements.txt` file. Install everything from it:
    ```bash
    pip install -r requirements.txt
    ```

2.  **(If `requirements.txt` doesn't exist)**, install the packages manually:
    ```bash
    pip install fastapi "uvicorn[standard]" python-multipart ffmpeg-python
    ```
    *(**For the team member who *adds* new packages**: After you install something, always run `pip freeze > requirements.txt` to update the file for everyone else.)*

---

## 4. 🚀 Run the API Server

You're all set. It's time to run the server.

1.  From the root of your project folder (the same place you ran `pip install`), run Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
    * `main`: This tells Uvicorn to look for the file `main.py`.
    * `app`: This tells it to find the object named `app` inside that file.
    * `--