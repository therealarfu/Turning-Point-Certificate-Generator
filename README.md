<img width="3943" height="990" alt="image" src="https://github.com/user-attachments/assets/421e2f1a-f3c7-4b13-9d80-868616fb5ac6" />

# Turning Point Certificate Generator

A web application for generating personalized certificates from a PDF template.

This project was developed for **Turning Point**, a volunteer initiative focused on expanding access to quality education and empowering students through leadership opportunities.

The application allows users to enter a participant's name and an optional issue date, generating a customized PDF certificate instantly in the browser.

## Features

* Generate personalized certificates from a predefined PDF template.
* Dynamic insertion of participant names.
* Optional issue date generation.
* Automatic PDF download.
* Responsive interface for desktop and mobile devices.
* Modern user experience built with HTML, CSS, JavaScript, and Tabler Icons.
* In-memory PDF processing using `BytesIO`.
* No temporary files written to disk.

## Tech Stack

### Backend

* FastAPI
* ReportLab
* pypdf

### Frontend

* HTML5
* CSS3
* JavaScript
* Tabler Icons

## Architecture

The application follows a simple workflow:

1. The user enters a participant's name and optional date.
2. FastAPI receives the form submission.
3. ReportLab generates a temporary PDF layer containing the personalized text.
4. pypdf merges the generated layer with the certificate template.
5. The final PDF is streamed back to the browser.
6. The user downloads the generated certificate.

## Performance and Memory Management

A key design decision in this project was avoiding temporary files on the server.

Instead of writing intermediate PDFs to disk, all processing is performed using Python's `io.BytesIO`, keeping files entirely in RAM during generation.

This approach:

* Reduces disk I/O operations.
* Improves performance.
* Simplifies deployment.
* Avoids accumulation of temporary files.
* Enhances scalability for concurrent requests.

## Project Structure

```text
.
├── main.py
├── templates/
│   └── certificate_template.pdf
├── static/
│   ├── css/
│   ├── js/
│   └── img/
└── style/
    └── fonts/
```

## Running Locally

### Clone the repository

```bash
git clone https://github.com/therealarfu/Turning-Point-Certificate-Generator.git
cd Turning-Point-Certificate-Generator
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install fastapi uvicorn reportlab pypdf python-multipart
```

### Run the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

Developed with ❤️ for the Turning Point project.
