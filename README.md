# Heating Load Prediction 🔥

This project is deployed on Hugging Face Spaces using **Gradio**.  
You can try the app here: [Heating Load Prediction](https://huggingface.co/spaces/boomiikas/Heating-Load-Prediction)

---

## 🚀 App Screenshot


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



### 2. Feature Correlation Heatmap
A correlation heatmap was generated to visualize the relationships between features:



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
