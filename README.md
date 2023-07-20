
# Real_Estate_Analysis

## Description
This project is the preliminary analysis of 19000 properties listed for sale in Belgium. The goal was to gather information on house prices for 19,000 properties and conduct a comprehensive analysis on the data.The project consists of several steps, including data scraping, data cleaning, exploratory data analysis (EDA), and machine learning model creation.

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


## Overview of analysis
The main results of the priliminary analysis are presented through a series of informative graphs and visualizations.
For a more detailed analysis and in-depth exploration of the findings, please refer to the accompanying Jupyter Notebook file, [Analysis.ipynb](/data-exploration/Analysis.ipynb).
### Geographic map about the distributions of the listed properties
![overall view of the listed properties on map](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/490ae895-0859-4ac5-977c-6044461104b3)
### Detailed graphs to study the average price for each provinces
![price per province](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/7d97dfe3-4f02-4f41-84fa-26fca5488bab)
### Correlation study of the various factors that may affect housing prices
![heatmap](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/f574b4b0-501c-4f0b-be66-9abf5483907d)

## Implementing machine learning models
### Implementing Linear regression model
Train score is 0.588061234204633

Test score is 0.549888815469199

![Linear regression](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/b57660f6-a341-46a5-8c5c-7b51b6c2e1d0)

### Implementing Decision tree model
Train score is 0.793576253189495

Test score is 0.6375768136633881

![Decision tree](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/dfeee9c6-fc96-47d4-ac1b-2a2afb9433bc)

### Implementing Random Forest model
Train score is 0.9673342932331284

Test score is 0.782201260543899

![Random Forest](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/2c6955d6-35d2-4741-90ba-c6742ed5dd58)

### Implementing XGBoost model
Train score is 0.9437028882953589

Test score is 0.7989333449284743

![XGBoost](https://github.com/Spike815/Real_Estate_Analysis/assets/97194496/5bd4e416-3e8b-4a4e-bca2-87d92ecfa233)



## Usage
Execute [Analysis.ipynb](/data-exploration/Analysis.ipynb) to go through the whole data cleaning and analysis process.

Execute [regression-model.ipynb](/model-building/regression-model.ipynb) to go through the whole machine learning model building process.

Execute `main.py` in terminal to implement the whole data cleaning and modeling, testing process mentioned above.

## Installation
This program requires python 3.11.3. 
In this repository there is a requirements.txt file included. To install te required packages, you can run `python3 -m pip install -r requirements.txt`

To aviod version conflicts, I suggest you do so in a virtual environment.
    
## ⌛ Time frame
Data exploration takes 30 working hours, and machine learning modeling takes 24 working hours. 

## 🚀 About Me
This project is done by Bo Cao, Junior Data Engineer in Becode, Gent. Here below you can find the contact:
<a href = 'https://www.linkedin.com/in/bo-cao-313ab244'> Linkedin </a>

