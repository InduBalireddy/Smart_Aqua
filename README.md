🐟 Smart Aqua: Precision Monitoring & AI AdvisorSmart Aqua is an AI-powered aquaculture dashboard designed to help farmers monitor water quality and predict the best fish species for their current environmental conditions.
The app uses machine learning to analyze chemical and physical water parameters, providing real-time survival alerts and expert growth insights.

🚀 FeaturesAI-Driven Compatibility:

Predicts the best fish match (e.g., Salmon, Tilapia, Rohu) based on pH, Temperature, Turbidity, Dissolved Oxygen, and Ammonia. 
Interactive Oxygen Gauge: A visual Plotly-based gauge that categorizes Dissolved Oxygen levels into Lethal (Red), Stress (Orange), and Healthy (Green) zones. 
Survival Threshold Alerts: Instant visual warnings for lethal oxygen levels or toxic ammonia spikes to prevent livestock loss. 
Expert Growth Insights: Dynamic advice boxes that provide species-specific management tips based on AI predictions.

Live Demo:https://smartaqua-123.streamlit.app/

Tech Stack

    Frontend: Streamlit  

    Visualizations: Plotly  

    Machine Learning: Scikit-learn (Random Forest/SVM via fish_model.pkl)  

Data Processing: NumPy & Scikit-learn Scaler
📊 How it WorksThe application follows a simple four-step workflow:
Input: The user enters water chemistry and physical parameters into the sidebar. 
Scaling: Data is processed using scaler.pkl to match the model's training requirements.  
Prediction: The fish_model.pkl predicts the most suitable species with a confidence score.  
Alerting: Logic checks evaluate if parameters like Ammonia ($>0.05$ ppm) or Oxygen ($<3.0$ mg/L) have hit dangerous thresholds. 

🧠 Model Logic

The project utilizes a Random Forest Classifier. We chose this model because it handles non-linear relationships in agricultural data effectively by aggregating the decisions of multiple decision trees, preventing overfitting and ensuring high reliability.

🤝 Contributing

This was my very next project followed by agri_smart_predicto. If you have suggestions on how to improve the model or the UI, feel free to fork the repo and create a pull request.
