# Django Rest Framework Template Project

This project is built using Django Rest Framework (DRF). It provides a foundation for creating and managing RESTful APIs.

## Installation

To install this project, follow these steps:

1. **Clone the project:**
 ```bash
 git clone https://github.com/ok7uz/Django-DRF-Template.git
 cd Django-DRF-Template
```
2. **Set up a virtual environment (recommended)**:
```bash
python3 -m venv env
source env/bin/activate
```
3. **Install the requirements:**
```bash
pip install -r requirements.txt
```
4. **Create the .env file.** Copy the necessary values from the .example.env file and adjust them as needed:
```bash
cp example.env .env
```
5. **Apply migrations and create the database:**
```bash
python manage.py migrate
```
6. **Run the server:**
```bash
python manage.py runserver
```
You can install and configure the main parts of the project through these steps.

## Configuration
Modify the necessary values inside the ``.env`` file for configuration. Additional settings can be adjusted in the settings.py file.

## Issues and Suggestions
If you have any questions, suggestions, or encounter any issues related to this project, please feel free to raise an issue on GitHub. Your feedback is highly appreciated!
