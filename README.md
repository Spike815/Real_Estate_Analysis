
# Real Estate Analysis

## Description
This project aims to build and deploy machine learning models for predicting real estate property prices in Belgium. By leveraging historical property data, I seek to create accurate models that can provide insights into property valuation. The project consists of several steps, including data scraping, data cleaning, exploratory data analysis (EDA), and machine learning model creation.

#### -Data scraping
The dataset is scraped from
<a href = 'https://www.immoweb.be/en'> Immoweb</a> .The scraping process involved accessing individual property pages and extracting details such as price, location, size, number of bedrooms, and other relevant features. More details about the scraping and dataset can be found in my previous project <a href = 'https://github.com/Spike815/Immo_Scraping'> Immo_Scraping </a>.

#### -Data cleaning
Once the data was scraped, a rigorous data cleaning process was implemented to ensure data quality and consistency. This involved handling missing values, removing duplicate entries, and addressing any inconsistencies or anomalies in the data. The cleaning process aimed to create a clean and reliable dataset for subsequent analysis.

#### -Data exploration
The preliminary data exploration / analysis can be found in [Analysis.ipynb](/data-exploration/Analysis.ipynb). It consists two main part. The first part is about the geographic distribution of the listed real estate properties. The second part is the analysis of the various factors that may affect housing prices.

#### -Machine learning modeling
The machine learning modeling process can be found in [regression-model.ipynb](/model-building/regression-model.ipynb). It includes feature engineering, data preprocessing, and split the data into training and testing sets. I have built 4 models:

* Linear Regression

* Decision Tree

* Random Forest

* XGBoost

Finally I choose XGBoost as my machine learning model.


#### -Deployment
This project can be deplyed in two ways:

* Local deployment with Docker

* Access the API deployed on render.com


## Overview of analysis
The main results of the priliminary analysis are presented through a series of informative graphs and visualizations.
For a more detailed analysis and in-depth exploration of the findings, please refer to the accompanying Jupyter Notebook file, [Analysis.ipynb](/data-exploration/Analysis.ipynb).
### Geographic map about the distributions of the listed properties
![overall view of the listed properties on map](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/490ae895-0859-4ac5-977c-6044461104b3)
### Detailed graphs to study the average price for each provinces
![price per province](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/7d97dfe3-4f02-4f41-84fa-26fca5488bab)

## Implementing XGBoost model
Train score is 0.9437028882953589

Test score is 0.7989333449284743

![XGBoost](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/5bd4e416-3e8b-4a4e-bca2-87d92ecfa233)



## Usage

You can either use the API provided below or locally deploy it with Docker.

### API-Fastapi
You can access the API running here:

`https://predict-real-estate-price.onrender.com/`

or follow the below link to directly send the property :

`https://predict-real-estate-price.onrender.com/docs/`

The response you received should be in this format:
`{
  "status": 200,
  "prediction": "219076 euro"
}`

### Local deployment

1. Install Docker:


Ensure Docker is installed on your machine. If not, you can download and install it from the official Docker website: https://www.docker.com/get-started

2. Build the Docker Image:
Use the provided Dockerfile in the project's root directory to build the Docker image. Run the following command:

`docker build -t myimage .`

3. Run the Docker Container:

`docker run -d --name mycontainer -p 80:80 myimage`

4. You should now be able to access the model at:

`http://127.0.0.1/docs`


## Installation
This program requires python 3.11.3. 
In this repository there is a requirements.txt file included. To install the required packages, you can run `python3 -m pip install -r requirements.txt`

To aviod version conflicts, I suggest you do so in a virtual environment.
    
## ⌛ Time frame
Data exploration takes 30 working hours, and machine learning modeling takes 24 working hours. 

## 🚀 About Me
This project is done by Bo Cao, Junior Data Engineer in Becode, Gent. Here below you can find the contact:
<a href = 'https://www.linkedin.com/in/bo-cao-313ab244'> Linkedin </a>

