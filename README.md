# Heating Load Prediction 🔥

This project is deployed on **Hugging Face Spaces** using **Gradio**.  

You can try the app here 👉 [Heating Load Prediction](https://huggingface.co/spaces/boomiikas/Heating-Load-Prediction)  

> **Note:** To access the web app, use the following credentials:  
> - **Username:** `admin`  
> - **Password:** `1234`  

---

## 🚀 App Screenshot
<img width="1919" height="740" alt="image" src="https://github.com/user-attachments/assets/0a7301d3-5c89-419f-b2d4-bf4fde2a1263" />
<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/707eb198-92fd-454b-8be4-7ee59f03e829" />


## 📈 Model Performance
- **Best Model:** XGBoost Regressor
- **MSE:** ~1.93
- **R² Score:** ~0.97

---

## 📊 Features Used
- **X1 Relative Compactness**
- **X3 Wall Area**
- **X5 Overall Height**
- **X6 Orientation**
- **X7 Glazing Area**
- **X8 Glazing Area Distribution**

## 🎯 Target Variable
- **Y1 Heating Load**

---

## 📊 Data Visualizations

To better understand the dataset, the following visualizations were created:

### 1. Feature Distributions
The distribution of each input feature (X1–X8) was plotted using Kernel Density Estimation (KDE):
<img width="1986" height="989" alt="image" src="https://github.com/user-attachments/assets/914b9cb2-74b3-4b69-8630-0da52d6ee2df" />



### 2. Feature Correlation Heatmap
A correlation heatmap was generated to visualize the relationships between features:
<img width="536" height="418" alt="image" src="https://github.com/user-attachments/assets/d5dd306b-a1a9-41a1-b395-ac8323d1dbb2" />


These visualizations help in identifying patterns, skewness, and correlations between the features, which are important for model training and evaluation.


## 🚀 Tech Stack
- **Python**
- **Scikit-learn**
- **XGBoost**
- **Streamlit**
- **Pickle** (for model deployment)

---

## 🛠️ Installation & Usage
```bash
# Clone repo
git clone https://huggingface.co/spaces/boomiikas/Heating-Load-Prediction

# Install dependencies
pip install -r requirements.txt

# Run app locally
python app.py
```

---

## 📜 License
This project is for learning and demonstration purposes.
