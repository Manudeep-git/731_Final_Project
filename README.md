# 731_Final_Project
Predicting climate change depending on various features for the Final project

## Team-Members
  - Ashwin Rathore
  - Sandhagala Francis Lazarus
  - Sai Manudeep Gadde
  - Likitha Vemulapalli
  
---

# Climate Change
![](https://static.stacker.com/s3fs-public/styles/properly_sized_image/s3/croppedshutterstock656066002jpg.JPEG)

## Background and Motivation
- Climate change is accelerating, bringing World `Dangerously close` to Irreversible Change.
- More devastating fires in California
- Persistent drought in the Southwest.
- Record flooding in Europe and Africa.
- A heat wave, of all things, in Greenland.

## Our Approach
- To show the effects and future outcomes we do not want to just use  global average data which would even out the differences across different parts of globe as it would represent the effects generally.
- We want to take a more specific approach, by working on 4 politically major countries from different parts of the world. From here on we will be working on these countries:
- United States of America
- Russia
- Australia
- United Kingdom (Britain)


## Exploratory Data Analysis

Notebooks related to Exploratory Data Analysis on Global Data can be found in this folder:


- [Global Temperature](Notebooks/Exploratory%20Data%20Analysis/World/Global_Temperatures.ipynb)
- [CO2-Emissions](Notebooks/Exploratory%20Data%20Analysis/World/Co2-emissions.ipynb)
- [Fossil Fuels](Notebooks/Exploratory%20Data%20Analysis/World/fossilfuels.ipynb)



Notebooks related to Exploratory Data Analysis on Four major countries:

- [Exploratory_Data_Analysis_UK](Notebooks/Exploratory%20Data%20Analysis/Four%20countries/Exploratory%20Data%20Analysis%20UK.ipynb)
- [Exploratory_Data_Analysis_Australia](Notebooks/Exploratory%20Data%20Analysis/Four%20countries/Exploratory%20Data%20Analysis%20Australia.ipynb)
- [Exploratory_Data_Analysis_Russia](Notebooks/Exploratory%20Data%20Analysis/Four%20countries/Exploratory%20Data%20Analysis%20Russia.ipynb)
- [Exploratory_Data_Analysis_USA](Notebooks/Exploratory%20Data%20Analysis/Four%20countries/Exploratory%20Data%20Analysis%20USA.ipynb)


## Regression
Regression Analysis was done to predict daily `Temperature` and `Precipitation` for all four countries using data from the last 50 years.

Following models are used for Regression Purposes

1. Multi-Linear Regression
2. K-Nearest Neighbours 
3. Gradient Boost 
4. Support Vector Machine
5. Decision Tree
### Notebooks related to Regression

- [United Kingdom](Notebooks/Regression/United%20Kingdom/Uk_Regression.ipynb)
- [Australia](Notebooks/Regression/Australia/Australia_regression.ipynb)
- [Russia](Notebooks/Regression/Russia/Russia_Regression.ipynb)
- [United States](Notebooks/Regression/United%20States/United_States_regression.ipynb)

## Classification

We did classification of Temperature and Conditions for four major countries. 

We used five classification models:<br>
- Linear SVC<br>
- Decision Tree Classifier<br/>
- KNN Classifier<br/>
- Random Forest Classifier<br/>
- Gaussian NB Classifier<br/>
### Results:
![](https://github.com/SFLazarus/731_Final_Project/blob/main/Reports/Classification/CompareModels_Conditions_US.png)

### Notebooks related to Classification:

- [Classification_UK](Notebooks/Classification/Classification_UK.ipynb)
- [Classification_US](Notebooks/Classification/Classification_US.ipynb)
- [Classification_Australia](Notebooks/Classification/Classification_Australia.ipynb)
- [Classification_Russia](Notebooks/Classification/Classification_Russia.ipynb)

From all those classifiers Linear SVC and Guassian NB Classifiers performed consistently for all the countries used and gave better results.

## Anomaly Detection
- Used Isolation Forest and Local Outlier Factor models to detect outliers.

### Notebook for Anomaly Detection:

- [Anomaly Detection](Notebooks/Anomaly%20Detection/Anomaly-Detection.ipynb)
### Results:
- In almost all cases Isolation Forest performed better than Local Outlier Factor, as there is no standard evaluation metric we can only judge by looking at the outliers detected by these models such as:

![](https://github.com/SFLazarus/731_Final_Project/blob/main/Reports/Anomaly%20Detection/Precipitation_USA_IsoForest.png)

![](https://github.com/SFLazarus/731_Final_Project/blob/main/Reports/Anomaly%20Detection/Precipitation_USA_LOF.png)
- We can clearly see that LOF could not point out obvious outliers where as Isolation Forest perfectly did the job.

## Time Series Forecasting
- Used ARIMA model to Forecast.


### Notebook for Time Series Forecasting

- [Forecasting](Notebooks/Time_series_Forecasting/Forecasting.ipynb)

Predicted the Weather and Fuel Consumption values  for near future using ARIMA model.

### Results:

![](https://github.com/SFLazarus/731_Final_Project/blob/main/Reports/Time_series_Forecasting/Predictions/USA_Temp.png)

![]()

![]()

![]()

![]()


---

## Conclusions and Further improvements

- Predicted Daily Temperatures of Four Major countries using various regression models from the existing data of last 50 years.
- Predicted Temperatures and Conditions using different classification models with Linear SVM and Decision Tree classifiers giving best accuracy, respectively.
- Detected Anomalies to understand the severity of the Climate change effects in recent times.
- Predicted future values of Weather Attributes and Fuel Consumption using ARIMA model for Time series forecasting.

- We can work on Ice sheets data to understand how the rise in temperature affecting melting process.
- We will extend Classification further by classifying temperature and conditions using the other Classification models to get the best accuracies.
- We will extend the Time Series Forecasting based on the correlation of different attributes for Weather and the changes based on the patterns of Geographical locations.

---

# Project Structure:
### Readme.md
- Project description
### Data
- countries_data (contains data files of four countries)
- modified_data(contains modified data files)
- world (contains world climate data files )
### Notebooks
- Anomaly Detection (contains notebooks)
- Classification (contains notebooks)
- Regression (contains notebooks)
- Time Series Forecasting (contains notebooks)
- Exploratory Data Analysis (contains notebooks)
### Reports
- Anomaly Detection (contains plots)
- Classification (contains plots)
- Regression (contains plots)
- Time Series Forecasting (contains plots)
- Exploratory Data Analysis (contains plots)
### Final Presentation
- EECS_731_Group_Presentation.ppt
### Requirements.txt
- Info about Tools, frameworks and libraries required to reproduce the work flow
