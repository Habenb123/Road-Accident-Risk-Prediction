# Road Risk Intelligence

A machine learning and geospatial analytics project for understanding road accident patterns, identifying accident hotspots, and estimating accident risk from historical road safety data.

## About the Project

Road accidents are rarely caused by a single factor. Conditions such as weather, lighting, road type, speed limits, junctions, time of day, and road surface can all influence the likelihood and severity of a collision.

The idea behind **Road Risk Intelligence** is to bring these different factors together and build a system that can analyse historical accidents and identify areas and conditions associated with higher road risk.

The project uses the **STATS19 road safety dataset**, published by the UK Department for Transport (DfT). The project focuses on a selected police-force area in Great Britain rather than trying to analyse the entire country at once.

The final goal is to build a web-based platform where accident data can be explored on a map, hotspots can be identified, and a machine learning model can estimate accident risk based on different road and environmental conditions.

---

## What I will be building

The project is being developed around four main capabilities:

1. **Accident Hotspot Detection**

   * Find locations where accidents are concentrated.
   * Use geographical coordinates from historical collisions.
   * Apply spatial clustering techniques to identify accident hotspots.
   * Rank areas based on accident concentration and severity.

2. **Accident Risk Prediction**

   * Train a machine learning model using historical accident data.
   * Use factors such as time, weather, road conditions, speed limit, junction information, road type, and location.
   * Estimate the risk associated with a given set of conditions.

3. **Risk Factor Analysis**

   * Understand why the model predicts a particular level of risk.
   * Use model explainability techniques such as SHAP.
   * Identify which factors have the strongest relationship with predicted risk.

4. **Interactive Risk Map**

   * Display historical accident locations.
   * Show identified accident hotspots.
   * Display different levels of predicted risk.
   * Allow users to explore areas and understand the factors associated with risk.

---

# Dataset

## STATS19 — Great Britain Road Safety Data

The main dataset for this project is **STATS19**, published by the UK Department for Transport.

STATS19 contains police-reported personal-injury road collision information and is divided into three main datasets:

* Collisions
* Vehicles
* Casualties

The **collision dataset** provides information about the accident itself, while the vehicle and casualty datasets provide additional information that can be joined to the collision records.

Some of the important variables available in the data include:

* Accident date
* Accident time
* Latitude and longitude
* Road type
* Speed limit
* Junction details
* Weather conditions
* Road surface conditions
* Light conditions
* Number of vehicles
* Accident severity
* Number of casualties

The vehicle data can provide additional information about vehicles and drivers, while the casualty data provides information about people involved in the collisions.

The dataset is useful for this project because it combines **temporal, geographical, road, environmental, vehicle and accident information** in a single data ecosystem.

---

# Development Process

The project will be developed in several stages. Each stage builds on the previous one rather than trying to build the complete application at once.

## 1. Project Setup

The first step is to create a clean and reproducible project environment.

* Setting up the Python environment.
* Organising the project into separate modules.
* Defining project dependencies.
* Setting up logging.
* directory structure.

---

## 2. Data Collection

The next step is to obtain the STATS19 datasets from the UK Department for Transport.

The datasets will include:

* Collision records
* Vehicle records
* Casualty records

The project will initially focus on a **selected police-force area**.

Once the pipeline works correctly for the selected area, it can be expanded to other areas.

---

## 3. Data Inspection and Understanding

Before training any model, the data needs to be understood properly.

* Observing the dataset
* Checking missing values.
* Checking duplicate records.
* Looking for invalid geographical coordinates.
* Understanding categorical variables.
* Examining accident severity.
* Checking the distribution of accidents across time.
* Checking the geographical distribution of accidents.

---

## 4. Data Cleaning

The cleaning process will include:

* Removing or handling duplicate records.
* Handling missing values.
* Validating latitude and longitude values.
* Converting date and time fields into usable formats.
* Handling categorical values.
* Checking numerical values such as speed limits.
* Removing records that cannot be used reliably.
* Making sure the collision records can be joined correctly with vehicle and casualty data.

---

# 5. Exploratory Data Analysis

Exploratory data analysis will be performed to understand historical accident patterns.

The analysis will look at questions such as:

### When do accidents happen?

### Where do accidents happen?

### What conditions are associated with accidents?

### How severe are the accidents?

---

# 6. Geospatial Data Preparation

Because location is an important part of road accident analysis, the geographical information will be processed separately.

The latitude and longitude of each collision will be validated and converted into a suitable geospatial representation.

The project will use geospatial Python tools to:

* Represent collisions as geographical points.
* Analyse their spatial distribution.
* Calculate accident density.
* Group nearby accident locations.
* Prepare geographical information for mapping.

Depending on the analysis, coordinates may also be transformed into an appropriate projected coordinate system when distance-based calculations are required.

---

# 7. Accident Hotspot Detection

One of the main objectives of the project is identifying accident hotspots.

Instead of simply displaying every accident on a map, the system will attempt to identify areas where accidents are geographically concentrated.

considered approaches are

* DBSCAN
* Spatial clustering
* Grid-based accident density
* Kernel density estimation

The hotspot analysis will consider:

* Number of accidents
* Spatial concentration
* Accident severity
* Potentially the time period of the accidents

The resulting clusters will represent areas that require further investigation.

The hotspot detection stage will eventually provide the geographical foundation for the risk map.

---

# 8. Feature Engineering

Potential features include:

### Time-based features

* Hour
* Day of week
* Month
* Weekend indicator
* Rush-hour indicator

### Road features

* Road type
* Speed limit
* Junction type
* Junction control

### Environmental features

* Weather conditions
* Road surface conditions
* Light conditions

### Accident/location features

* Latitude
* Longitude
* Geographic cluster
* Accident density
* Distance to identified hotspots

Additional features may be created if exploratory analysis shows that they provide useful information.

The aim is to create features that represent the conditions under which an accident occurred and the characteristics of its location.

---

# 9. Defining the Problem

The problem I am trying to solve is that road accidents are affected by multiple factors, but it is difficult to identify where accident risk is concentrated and which conditions contribute to that risk. My project uses STATS19 data to detect accident hotspots, analyse risk factors, predict accident risk using machine learning, and visualize the results on an interactive map.

---

# 10. Data Preprocessing

Data preprocessing include:

* Selecting relevant features.
* Encoding categorical variables.
* Scaling numerical variables where required.
* Handling remaining missing values.
* Checking class imbalance.
* Splitting the data into training and testing sets.

---

# 11. Model Development

Possible models include:

* Random Forest
* Gradient Boosting
* XGBoost

---

# 12. Model Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion matrix
  
---


# 13. Creating a Risk Score

After selecting and evaluating the model, its predictions will be converted into a format that is easier for users to understand.

The application can represent predictions using risk categories such as:

* Low Risk
* Moderate Risk
* High Risk
* Very High Risk

---

# 14. Interactive Risk Map

The final application will include an interactive geographical interface.

The map will be display:

* Historical accident locations.
* Accident hotspots.
* Risk levels.
* High-risk areas.
* Location information.
* Relevant risk factors.

---

# 15. Logging and Error Handling

Logging will help track:

* Application startup
* Data loading
* Data-processing stages
* Model training
* Prediction requests
* Errors
* Exceptions
* Important pipeline events

A dedicated `logger.py` module is being used to keep the logging configuration separate from the main application logic.

---

# 20. Testing

The testing process will cover important components such as:

* Data loading
* Data cleaning
* Feature engineering
* Hotspot detection
* Model prediction
* API endpoints
* Input validation

---
# Expected Final Result

The final result will be a **Road Risk Intelligence Platform** that brings together historical road accident data, machine learning and geospatial analysis.

The system should allow a user to move from a broad view of accident patterns to a more detailed understanding of individual locations.

For example, instead of simply showing that a location has experienced many accidents, the system should eventually be able to show:

* How many accidents occurred in the area.
* Whether the area forms part of an identified hotspot.
* The predicted level of risk.
* The conditions associated with that risk.
* Which factors contributed most strongly to the prediction.

The objective is therefore not just to build an accident prediction model, but to create a system that turns historical road safety data into information that is easier to explore, interpret and use.

---

# Tech Stack

### Programming

* Python
* SQL

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost / gradient boosting models
* SHAP

### Geospatial Analysis

* GeoPandas
* Shapely
* Scikit-learn spatial clustering

### Visualization

* Matplotlib
* Plotly
* Interactive mapping libraries

### Backend

* FastAPI

---

# Data Source

**STATS19 — Road Safety Data**

Publisher: UK Department for Transport (DfT)

The STATS19 datasets are used for research and analysis of reported personal-injury road collisions in Great Britain.

---

# Project Status

**Status: In Development**

The project is currently being developed incrementally, starting with the project foundation and data pipeline before moving toward geospatial hotspot detection, machine learning, explainability and the final interactive application.
