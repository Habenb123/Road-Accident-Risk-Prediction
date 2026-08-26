# 🚦 Road Risk Intelligence

A machine learning and geospatial analytics system for analyzing road accident risk, detecting accident hotspots, and understanding the factors associated with road collisions.

The project uses **STATS19 road safety data published by the UK Department for Transport (DfT)** and focuses on a selected police-force area in Great Britain.

---

## 📌 Project Overview

Road accidents are influenced by multiple factors, including road characteristics, weather conditions, lighting, time of day, junctions, speed limits, and traffic conditions.

The goal of this project is to develop a **Road Risk Intelligence Platform** that can:

- Identify accident hotspots
- Analyze historical accident patterns
- Predict accident risk under given conditions
- Identify factors contributing to predicted risk
- Visualize accident and risk information on an interactive map

The final system will combine **machine learning, geospatial analysis, and interactive visualization** into a web-based application.

---

## 🎯 Objectives

### 1. Accident Hotspot Detection

Identify geographical areas where road collisions are concentrated using historical accident coordinates and spatial clustering techniques.

### 2. Accident Risk Prediction

Develop a machine learning model capable of estimating accident risk based on factors such as:

- Time of day
- Day of week
- Weather conditions
- Road surface conditions
- Light conditions
- Road type
- Speed limit
- Junction characteristics
- Traffic conditions
- Location

### 3. Risk Factor Analysis

Analyze which factors contribute most strongly to accident risk using model explainability techniques such as **SHAP**.

### 4. Interactive Risk Map

Develop an interactive map displaying:

- Accident locations
- Accident hotspots
- Risk levels
- High-risk areas
- Risk factor information

---

## 📊 Dataset

### STATS19 — Great Britain Road Safety Data

The primary dataset used in this project is **STATS19**, published by the UK Department for Transport.

STATS19 contains police-reported personal-injury road collision records and provides several linked datasets:

- **Collisions**
- **Vehicles**
- **Casualties**

The collision data includes information such as:

- Date and time
- Geographic location
- Road type
- Speed limit
- Junction details
- Weather conditions
- Road surface conditions
- Light conditions
- Number of vehicles
- Number of casualties
- Accident severity

Vehicle and casualty tables provide additional information about vehicles, drivers, and casualties.

> Dataset source: UK Department for Transport (DfT)

---

## 🧠 Planned Methodology

```text
                 STATS19 DATA
                      │
                      ↓
              Data Ingestion
                      │
                      ↓
              Data Cleaning
                      │
                      ↓
           Feature Engineering
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
   Spatial Analysis         ML Risk Prediction
          │                       │
          ↓                       ↓
  Hotspot Detection        Risk Probability
          │                       │
          └───────────┬───────────┘
                      ↓
               Risk Analysis
                      │
                      ↓
               SHAP Analysis
                      │
                      ↓
             Interactive Map
                      │
                      ↓
             Web Application
