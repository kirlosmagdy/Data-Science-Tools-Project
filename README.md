# Data-Science-Tools-Project
# Bayut Real Estate Price Prediction Project

# Project Overview

This project involves scraping real estate data from the Bayut website, cleaning and preprocessing the data, and building a predictive model to estimate house prices. The cleaned data is stored in an SQL Server database, and insightful analysis has been performed to better understand the housing market trends.

# Features

1 - Data Scraping: Extracted data from the Bayut website, including:

    1- Property names

    2- Locations

    3- Features (e.g., number of bedrooms, bathrooms, area size)

    4- Prices

2 - Data Cleaning: Processed the raw data to handle missing values, remove duplicates, and standardize formats.

3 - Predictive Modeling: Built a machine learning model to predict house prices based on features such as location, size, and number of rooms.

4 - Database Integration: Stored the cleaned data in an SQL Server database for efficient querying and management.

5 - Data Analysis: Performed exploratory data analysis to uncover trends and patterns in the housing market.

# Tech Stack

Programming Language: Python

Libraries:

Web Scraping: BeautifulSoup, requests

Data Processing: pandas, numpy

Machine Learning: scikit-learn

Data Visualization: matplotlib, seaborn

Database: SQL Server

Other Tools: Jupyter Notebook, SQL Server Management Studio (SSMS)

# Steps

1. Web Scraping

Scraped data from Bayut's website using BeautifulSoup and requests.

Extracted relevant information such as property descriptions, prices, and features.

2. Data Cleaning

Handled missing and inconsistent data entries.

Converted data into structured formats suitable for analysis and modeling.

3. Predictive Modeling

Split the data into training and testing sets.

Used regression algorithms to predict house prices.

Evaluated the model using metrics such as Mean Absolute Error (MAE) and R-squared.

4. SQL Server Integration

Designed a relational database schema to store the cleaned data.

Inserted data into the database for further analysis and querying.

5. Data Analysis

Visualized key trends such as average house prices by location and price distributions.

Provided insights into the factors affecting house prices.
