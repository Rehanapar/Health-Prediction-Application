# Health Prediction Application

## Overview

The **Health Prediction Application** is a Django-based web application that allows users to manage patient health records and predict possible health conditions using an external AI service.

The application performs CRUD (Create, Read, Update, Delete) operations, validates user inputs, stores patient records in SQLite, and automatically generates AI-based health predictions from blood test values using the OpenRouter API.

## Features

- Add new patient records
- View all patient records
- Update patient information
- Delete patient records
- AI-powered health prediction using the OpenRouter API
- Automatic generation of health remarks
- Input validation
- SQLite database for persistent storage
- Clean and responsive user interface

## Technologies Used

### Backend

- Python 3
- Django

### Frontend

- HTML5
- CSS3

### Database

- SQLite

### AI Integration

- OpenRouter API
- OpenAI GPT-4.1 Nano (via OpenRouter)

## How It Works

1. The user enters the patient's:
   - Full Name
   - Date of Birth
   - Email Address
   - Glucose
   - Haemoglobin
   - Cholesterol

2. Django validates the entered data.

3. The application sends the blood test values to the OpenRouter AI API.

4. The AI predicts the patient's possible health condition.

5. The predicted result is automatically stored in the **Remarks** field.

6. The patient record is saved in the SQLite database.

## Input Validation

The application validates:

- Full Name must contain at least 3 characters.
- Email must be in a valid format and unique.
- Date of Birth cannot be a future date.
- Glucose must be greater than 0.
- Haemoglobin must be greater than 0.
- Cholesterol must be greater than 0.

## Future Improvements

- Integration with specialized healthcare AI services
- Patient search and filtering
- User authentication and role-based access
- Dashboard with charts and analytics
- Email notifications
- PDF report generation
- Export patient records to Excel or CSV
