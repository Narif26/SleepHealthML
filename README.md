# Sleep Health & Stress Level Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-✔️-green)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Random_Forest,_XGBoost,_SVM-orange)
![Visualization](https://img.shields.io/badge/Data_Visualization-Seaborn,_Plotly,_Matplotlib-teal)

---

## Overview

This project investigates how sleep health metrics — such as **sleep duration**, **quality of sleep**, and **physical activity** — influence an individual's **stress level**. Leveraging machine learning techniques, we build models that predict stress levels and uncover key insights from real-world lifestyle data.

---

## Problem Statement

Poor sleep has long been correlated with elevated stress, often accompanied by increased cortisol, adrenaline, and norepinephrine levels. This project explores:

- The relationship between sleep patterns and stress
- Predicting stress levels from lifestyle and physiological indicators
- Providing interpretable visualizations for model insights

---

## Dataset

**Name**: Sleep Health and Lifestyle Dataset  
**Rows**: 400  
**Features**:
`Age`, `Gender`, `Occupation`, `Sleep Duration`, `Sleep Quality`, `Stress Level`,  
`Daily Steps`, `Physical Activity Level`, `BMI`, `Heart Rate`, `Blood Pressure`, `Sleep Disorder`

[Link to Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

---

## Tools & Technologies

- **Language**: Python  
- **Environment**: Jupyter Notebook  
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `seaborn`, `matplotlib`, `plotly`
  - Modeling: `scikit-learn`, `xgboost`

---

## Machine Learning Models Used

| Model                   | Accuracy | Avg Error |
|------------------------|----------|-----------|
| Logistic Regression     | 88.00%   | 17.33%       |
| Random Forest Classifier| 93.33%   | 12.00%        |
| XGBoost Classifier      | 92.00%   | 13.33%      |
| K-Nearest Neighbors     | 92.00%   | 13.33%       |
| Support Vector Machine  | 90.67%   | 14.67%     |

✅ **Evaluation**: Feature importance and confusion matrices.

---

## Visualizations

- Correlation heatmaps
- Feature importance bar charts
- Pair plots and histograms showing stress distribution
- Boxplots: Stress vs. Physical Activity Level

---

## Key Findings

- **Sleep Duration** and **Quality of Sleep** were the strongest predictors of stress.
- Individuals with **low** or **very high** physical activity levels tended to have higher stress.
- **Sleep Disorders** such as Insomnia and Sleep Apnea showed strong correlation with elevated stress levels.

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
