Health Prediction Application
Overview

The Health Prediction Application is a Django-based web application that allows users to manage patient health records and predict possible health conditions using a Machine Learning model.

The application performs CRUD (Create, Read, Update, Delete) operations, validates user inputs, stores patient records in SQLite, and automatically generates health predictions based on blood test values.

Features:

Add new patient records
View all patient records
Update patient information
Delete patient records
Automatic health prediction using Machine Learning
Input validation
SQLite database for persistent storage
Clean and responsive user interface

Technologies Used
Backend
Python 3
Django
Frontend
HTML5
CSS3
Database
SQLite
Machine Learning
Scikit-learn
Pandas
Joblib
Random Forest Classifier

Dataset

The Machine Learning model is trained using a dataset containing:

Glucose
Haemoglobin
Cholesterol
Health Condition

The trained model is stored as:

patients/ml/health_model.pkl

Future Improvements:

Integration with external Health AI APIs
Patient search and filtering
User authentication
Dashboard with charts and analytics
Email notifications
PDF report generation
