# AI-Powered Sustainable Farming Advisor

## 1M1B AI for Sustainability Virtual Internship Project

An AI-powered decision-support application designed to provide sustainable farming guidance based on crop, weather, soil, and irrigation conditions.
## Live Demo

Try the deployed application here:

[AI-Powered Sustainable Farming Advisor](https://ai-sustainable-farming-advisor-kwsasrr6gv8ew4kcvh47vy.streamlit.app/)

## Problem Statement

Farmers need accessible and understandable guidance for making better decisions about crop suitability, water management, fertilizer use, soil conditions, and environmental risks.

Poor decisions can lead to excessive use of water, fertilizers, and pesticides, which may increase costs and negatively affect sustainability.

## Proposed Solution

The AI-Powered Sustainable Farming Advisor provides farmers with decision-support guidance based on:

- Crop
- Season
- Farm area
- Irrigation method
- Rainfall
- Temperature
- Humidity
- Soil pH
- Soil moisture
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)

The application provides:

- AI-based crop suitability recommendation
- Soil and pH guidance
- Fertilizer and nutrient guidance
- Water management guidance
- Disease and pest environmental risk awareness
- Sustainable farming practices
- Responsible AI guidance

## AI Technique

The project uses a **Random Forest Classification** model for crop recommendation.

### Model Inputs

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### Dataset

**Crop Recommendation Dataset**

- Total records: 2,200
- Training records: 1,760
- Testing records: 440
- Model accuracy on the held-out test set: 99.55%

The test accuracy represents performance on this dataset and does not guarantee the same performance under real-world farming conditions.

## Technology Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- HTML/CSS
- IBM Bob

## IBM Bob Usage

IBM Bob was used as an AI-assisted software development environment during the project development workflow.

It supported:

- Project setup and organization
- Code development and refinement
- Reviewing and improving application code
- Streamlit application organization

More details are available in `IBM_BOB_USAGE.md`.

## Sustainable Development Goals

### SDG 2 – Zero Hunger

Supports sustainable agriculture and informed farming decisions.

### SDG 6 – Clean Water and Sanitation

Promotes responsible water management and efficient irrigation practices.

### SDG 12 – Responsible Consumption and Production

Encourages responsible use of fertilizers, pesticides, and other agricultural resources.

### SDG 13 – Climate Action

Promotes climate-aware farming practices based on environmental conditions.

## Responsible AI

The application is designed as a decision-support tool and not as a replacement for qualified agricultural experts.

Users should verify recommendations using:

- Soil tests
- Local agricultural conditions
- Reliable weather information
- Advice from qualified agricultural experts

The project also considers transparency, responsible resource use, privacy, fairness, and human oversight.

## Project Structure

```text
AI-Sustainable-Farming-Advisor/
│
├── app.py
├── style.css
├── train_model.py
├── Crop_recommendation.csv
├── crop_recommendation_model.pkl
└── IBM_BOB_USAGE.md
