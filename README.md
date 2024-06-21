# Hotel Recommendation System based on sentiment analysis

## Overview

This project aims to develop a hotel recommendation system by leveraging data from social media user interests and hotel reviews from Booking.com. The system includes the extraction and clustering of user interests, sentiment analysis of hotel reviews using deep learning models, and a web application built with Django. The project structure includes various components for web development, data extraction, clustering, sentiment analysis, and image scraping.

## Project Structure

- **web dev django/pfa_recommendation/**: This directory contains the Django web application for the hotel recommendation system.
- **PFA_User_Interests_Last_Version.ipynb/**: Scripts for extracting and clustering user interests from social media data.
- **pfa sentiment analysis.ipynb/**: Implementation of sentiment analysis on hotel reviews using BiLSTM and GloVe embeddings.
- **image_scraping/**: Scripts for scraping hotel images and details from Booking.com.
- **flask_backend/**: Flask application to connect the backend with the Django web application.

## Contents

### 1. Web Application 

- **Features**:
  - User authentication and profile management.
  - Display of recommended hotels based on user interests and review sentiments.
  - Integration with the Flask backend for real-time data processing.

### 2. Data Extraction and Clustering 

-  Scripts for extracting user data from social media and clustering their interests.
-  Extracts user data including username, user ID, followers count, posts count, posts, and interests.
-  Clusters user interests to generate meaningful groups using cosine similarity matrix .

### 3. Sentiment Analysis 

- Implementation of sentiment analysis on hotel reviews using deep learning models.- 
- Performs sentiment analysis ans aspects extraction using NLP, BiLSTM and GloVe embeddings.
- **Models**: Pre-trained BiLSTM model files and GloVe embeddings.

### 4. Image Scraping 

- Scripts for scraping images and information of hotels from Booking.com.
- Scrapes hotel images and details such as names, URLs, and ratings.

### 5. Flask Backend 

- Flask API to connect the backend processes with the Django web application.

## Installation

 **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Hotel-Recommendation-System-based-on-sentiment-analysis-NLP.git
   ```

## DEMO 
- **File**:  `project presentation demo.PDF`
- **LINK PDF**: https://drive.google.com/file/d/1SJZDFIIw6jbY7bZ-o8sOYQp3MAaS3YGV/view?usp=drive_link
- **LINK video demo**: https://drive.google.com/file/d/1SJZDFIIw6jbY7bZ-o8sOYQp3MAaS3YGV/view?usp=drive_link

   
