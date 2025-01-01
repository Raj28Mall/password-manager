# Password Manager

A simple **Password Manager** built using Python and Tkinter. This application allows users to securely save their passwords for different websites in a CSV file. The app features a graphical user interface (GUI) and is designed to handle multiple email addresses for quick selection.

---

## Features

- **Password Entry Storage**: Save website names, email/username, and passwords to a `data.csv` file.
- **Graphical User Interface (GUI)**: User-friendly interface built with Tkinter.
- **CSV Integration**: Stores data in a CSV file, appending new entries while maintaining headers.
- **Email/Username Dropdown**: Allows selecting from predefined email options.
- **Password Validation**: Ensures that no fields are left empty before saving.
- **Random Password Generator**: (To be implemented) Generate strong, random passwords directly from the app.

---

## Application Preview

![App Preview](./logo.png)  
*Logo used as part of the GUI.*

---

## Prerequisites

- Python 3.x
- Required Libraries:
  - `tkinter` (built-in with Python)
  - `pandas` (`pip install pandas`)

---

## How to Use

1. Clone or download the repository to your local machine.
2. Ensure the required libraries are installed.
3. Place a `logo.png` image in the project directory (used for the app's GUI).
4. Run the Python script:
   ```bash
   python main.py
5. Fill in the following fields and click on Add
6. The data will be stored in a data.csv file in the project directory