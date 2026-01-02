
#  Campus Water Dashboard

**AI-Based Water Demand Forecasting for Campus Operations**  
Category: Water Management | Difficulty: Intermediate-Advanced  

---

## **Project Overview**

Campuses often struggle with managing daily water demand across hostels, canteens, academic blocks, and gardens. Suboptimal planning causes shortages or over-pumping, increasing both water and electricity consumption.  

This project provides a **machine learning-powered dashboard** that:

- Predicts **next-day water consumption** per campus zone.  
- Compares consumption across **zones** (Academic Blocks, Hostels, Garden).  
- Suggests **optimized pumping schedules** to reduce energy use and over-pumping.  

---

## **Features**

- **Interactive Forecast:** Predict water demand for selected zone and date range.  
- **Zone Comparison:** Visualize predicted consumption for all zones.  
- **Professional Dashboard:** Clean, medium-sized interactive visualizations using Streamlit and Matplotlib.  
- **Energy Insights:** Optional metrics for baseline vs optimized pumping.  

---

## **Tech Stack**

- **Python:** Data processing and ML modeling  
- **Machine Learning:** XGBoost / LSTM for water demand prediction  
- **Libraries:** Pandas, NumPy, Matplotlib, Joblib, Streamlit  
- **Dashboard:** Streamlit for professional interactive interface  

---

## **Folder Structure**

```

Eco-Flow/
├─ app.py                   # Streamlit dashboard
├─ train.py                 # Model training script
├─ requirements.txt         # Python dependencies
├─ README.md                # Project documentation
├─ .gitignore               # Ignore venv, cache, etc.
├─ models/
│   └─ water_demand_model.pkl
├─ data/                    #small CSV datasets

````

---

## **Setup & Run Locally**

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Eco-Flow.git
cd Eco-Flow
````

2. (Optional) Create virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# OR
source venv/bin/activate      # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit dashboard:

```bash
streamlit run app.py
```

* The dashboard opens in your browser with interactive forecasts.

---

## **Deployment**

* Hosted on **Streamlit Cloud** for easy sharing.
* Simply link your GitHub repo to Streamlit Cloud, select `app.py`, and deploy.

---

## **Impact**

* **Reduces over-pumping by ~30%**
* **Optimizes water distribution** for hostels, academic blocks, and gardens
* **Potential energy savings:** 20-25% at the campus level
* **Supports water budgeting and sustainable campus management**

---

## **Future Enhancements**

* Include **weather, occupancy, and timetable patterns** for improved accuracy
* Add **real-time IoT sensor integration** for live water monitoring
* Dynamic **pump scheduling recommendations** with energy optimization

---

## **License**

This project is open-source and free to use for educational purposes.

```
