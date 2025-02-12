# **SaiGon Care Website**

**SaiGon Care Website** is a management system developed between October 2024 and December 2024. It is designed to streamline various clinic operations, including:

- Appointment scheduling.
- Prescription management for patients.
- Payment processing.
- Medication and appointment usage statistics.

## Table of Contents
- [Key Technologies](#key-technologies)
- [Usecase](#usecase)
- [Database Schema Diagram](#database-schema-diagram)
- [Demo](#demo)
- [Installation](#️installation)
- [Authors](#authors)

## **Key Technologies**

- **Flask-Admin**: Used for managing both the backend and the administration site’s frontend.
- **WTForms**: Facilitates easy and flexible form design.
- **ChartJS**: Used for drawing statistical charts.
- **Cloudinary**: Stores images on a remote database.
- **BCrypt**: Hashes passwords to enhance user security.
- **SQLAlchemy**: Manages database interactions with a powerful Python ORM.
- **Flask-Mail**: Used for sending emails to users, such as notifications and password resets.
- **itsdangerous**: Generates and verifies secure tokens for password reset functionality.
- **VNPay API**: Integrated for online payment processing and transactions.

## Usecase
<img src=".\hahhaha_clinic_final\photos\usecase.png" ></img>

## Database Schema Diagram
<img src=".\hahhaha_clinic_final\photos\database_cnpm.png" ></img>

## Demo   
Saigon Care website deployed at [Saigon Care Website](https://phuongouedu.pythonanywhere.com/)

**Account demo:**

```bash
# ROLE: username - password
ADMIN: admin - 123
PATIENT: patient1 - 123
NURSE: nurse1 - 123
DOCTOR: doctor1 - 123
```


## Installation
```bash
# Install the necessary libraries:
pip install -r requirements.txt
# Start project
run index.py
```

## Authors

- **[nglhongphuong](https://github.com/nglhongphuong)**  
  *Role*: Managed patient appointment scheduling, doctor prescription management, user account management, and medication management.

- **[ThaiBao107](https://github.com/ThaiBao107)**  
  *Role*: Handled payment transactions and financial processing.

- **[NguyenThiMai2k4](https://github.com/NguyenThiMai2k4)**  
  *Role*: Conducted medication usage statistics and analysis.