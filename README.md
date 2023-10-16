# Basketball Highlighting 🏀


## Prerequisites

Ensure you have met the following requirements:

- You have a **Windows/Linux/Mac** machine.
- You have installed **Python 3.8 or higher**.
- You have installed **pip** (comes installed with Python by default).
- You have installed **Git**.

## Installation

To install:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/basketball-detection.git
    ```
    Replace `your-username` with your GitHub username.

2. Navigate to the project directory:
    ```bash
    cd basketball-detection
    ```

3. (Recommended) Create a virtual environment to manage dependencies:
    ```bash
    python -m venv env
    ```
    Activate the virtual environment:
    - On Windows, use:
        ```bash
        .\env\Scripts\activate
        ```
    - On Linux/MacOS, use:
        ```bash
        source env/bin/activate
        ```

4. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Using Basketball Detection Application

To use the Basketball Detection Application, follow these steps:

1. Run the application script:
    ```bash
    python gui.py
    ```

2. Use the "Open Image" or "Open Video" button in the GUI to select an image or video file.

3. The application will process the file and highlight detected basketballs directly in the GUI.

