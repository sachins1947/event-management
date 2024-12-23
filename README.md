
# Hackathon Assignment: Event Management Dashboard

**Description**  

Welcome to the **Event Management App** repository! This application is designed to manage events, attendees, and tasks associated with events.

---

**Table of Contents**  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

---

## Prerequisites
Ensure the following are installed:

- Python
- pip (Python package manager)
- Node.js and npm

---

## Installation

**Requirements**  
- List any prerequisites or dependencies needed to run your project.

**Steps to Install**  
### 1. Clone the repository:
   ```bash
   git clone https://github.com/AnmolShubhamsteam/Event-Management.git
   cd Event-Management
   ```

### 2. Create and Activate a Virtual Environment

#### On Windows:
```bash
python -m venv env
env\Scriptsctivate
```

#### On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Django and rest framework
```bash
pip install Django
pip install djangorestframework
pip install markdown    
pip install django-filter 
```

### 4. Install Tailwind
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### 5. Install Tailwind CSS in Django
Install the required packages:

```bash
pip install django-tailwind
pip install 'django-tailwind[reload]'
```

### 6. Install Tailwind in your project:
**Before installing in settings.py:**
```bash
(in terminal) which node

Then add the path in your settings.py:

NPM_BIN_PATH = '/usr/local/bin/npm'  # Adjust for Linux/Mac
# Or for Windows:
NPM_BIN_PATH = r"C:\Program Files
odejs
pm.cmd"
```

```bash
python manage.py tailwind install
```

### 7. In one terminal, keep tailwind activated by running:

```bash
python manage.py tailwind start
```

### 8. In another terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Create a Superuser

Create an admin user to access the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your superuser credentials.

### 10. Run the Development Server

Start the Django development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your web browser to view the application.

---

## Usage

### Access the Admin Panel
- Navigate to `http://127.0.0.1:8000/admin`.
- Log in using the superuser credentials you created earlier.

### Add Events, Attendees, and Tasks
1. Go to the admin panel.
2. Use the **Event**, **Attendee**, and **Task** sections to add and manage entries.

### Access the API 
- Navigate to `http://127.0.0.1:8000/api`

---

## Made by Sachin Singh (Acharya Institute of Technology)
