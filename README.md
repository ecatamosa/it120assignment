 # IT 120 - INTEGRATIVE PROGRAMMING TECHNOLOGIES 2 - Build a Django Web Application to Send SMS Using Twilio


Submitted by:


GROUP 3 - Eisan Carlos Atamosa, Michelle Malto, Guilbert Jan Cabual


### Table of Contents

- Introduction

- Getting Started

- Prerequisites

- Installation Steps

- Usage

- How the Application Works

- Important Notes




## Introduction

This project is a Django web application that uses the Twilio API to send SMS messages. The application is designed to simplify the process of integrating SMS functionality into your Django projects.

---

## **Getting Started**


Follow the steps below to set up and run the application on your local machine.

---

## **Prerequisites**


Ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

---

## **Installation Steps**


### **1. Install Django**

Install Django using pip:

``` bash
pip install django
```



#### Verify the installation:


```bash
pip show django
```


### 2. Install Python-Decouple

Install the python-decouple package for managing environment variables:


```bash
pip install python-decouple
```



### 3. Create a .env File

In the root directory of your project (same folder as manage.py), create a file named .env.

Add the following variables:


```bash
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
SECRET_KEY=your_secret_key
DEBUG=True
```


#### If you don’t have a SECRET_KEY yet, generate one using the following command:


```bash

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```


## **Setting Up the Project**

### 4. Run the Development Server

Start the Django development server:


```bash
python manage.py runserver
```



### 5. Apply Migrations

Create and apply database migrations:


```bash
python manage.py makemigrations
python manage.py migrate
```



### 6. Create a Superuser

Create an admin user for the application:


```bash
python manage.py createsuperuser
```



---
## Twilio Integration



### 7. Create a Twilio Account

- Sign up at Twilio.
- Retrieve your Account SID, Auth Token, and a Twilio Phone Number.



### 8. Update .env with Twilio Credentials

Add the following values to your .env file:


```bash
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```



### 9. Install Twilio SDK

Install the Twilio Python SDK:


```bash
pip install twilio
```



### 10. Verify Installed Packages

Confirm the required packages are installed:


```bash
pip list
```






## Usage

### Run the Server

Start the server:


```bash
python manage.py runserver
```




### Access the Application

Open a browser and go to:


```arduino
http://127.0.0.1:8000/
```



### Send SMS

Use the provided functionality in the application to send SMS using the Twilio API.



---




## How the Application Works

### Environment Variables

- Securely stores sensitive credentials like SECRET_KEY and Twilio API credentials in a .env file.


### Twilio Integration

- Uses the Twilio SDK to connect with Twilio's API for sending SMS messages.


### Admin Interface

- Manage the application via the Django Admin interface.


---




## Important Notes

- Do not share your .env file: It contains sensitive credentials.
- DEBUG Setting: Ensure DEBUG=False in production for security.
- Twilio Free Tier: If you're using a free Twilio account, verify the phone numbers before sending SMS.













