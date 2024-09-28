# SuppleezMoi

**SuppleezMoi** is a web-based application designed to streamline the process of requesting substitute teachers at the University of Namur. It simplifies the workflow for professors submitting substitute requests and allows the administrative team to manage, validate, and assign substitutes efficiently.

## Key Features:
- **Request Creation:** Professors can easily create substitution requests using a simple form.
- **Data Validation:** The application validates the completeness of all inputted data.
- **Admin Management:** Administrative personnel can manage requests, ensure data completeness, and assign substitutes.
- **User Access Control:** The application is designed for both professors and administrators, with role-specific access to different functionalities.

## Technology Stack:
- **Frontend:** HTML, CSS, JavaScript, Bootstrap, jQuery
- **Backend:** Django 5.0.2, Python 3.10
- **Database:** SQLite
- **Other Dependencies:** django-jazzmin, django-select2, python-dateutil, openpyxl, python-json-logger

## Installation Guide:
### Prerequisites:
- Ensure you have Python 3.10 or later installed on your system.
- Set up a virtual environment for the project for dependency isolation.

### Installation Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/UNamurCSFaculty/2324_INFOB318_SuppleezMoi.git
    ```
2. Navigate to the project folder and activate your virtual environment:
    ```bash
    cd SuppleezMoi
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run database migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Testing:
To run the test suite for models and views, use the following command:
```bash
python manage.py test
