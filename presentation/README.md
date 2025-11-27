Autism Spectrum Disorder (ASD) Early Prediction in Children  
Group 15 – Final Year Machine Learning Project with Refactory Academy
Presentations made on 27th november 2025

FINAL MODEL PERFORMANCE 
| Model             | Accuracy | Precision | Recall | F1-Score | Confusion Matrix          |
|-------------------|----------|-----------|--------|----------|---------------------------|
| Random Forest | 96.22% | 0.97    | 0.96   | 0.96     | [[165, 17]\n [13, 202]]   |
| Neural Network    | 92.95%   | 0.93      | 0.94   | 0.94     | [[168, 14]\n [13, 202]]   |

Live Deployment: https://your-streamlit-app.streamlit.app (update after deploy)

Type of Dataset: 
1.Structured tabular data which is  ideal for supervised binary classification
2.Each row = One child
3.Each column = Behavioral, developmental, clinical, or demographic feature

Original Dataset : 
1,985 children
31 columns (including redundant & noisy features)
Target Variable - ASD_traits (Yes/No) — indicates whether the child is diagnosed/likely autistic (Yes/No or 1/0)

Models Used (As Per Your Training):
1. Random Forest →  96.22% (saved as best model)  
2. Deep Neural Network (TensorFlow/Keras) → 92.95%
## Repository Structure

Tools & Libraries
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn

Authors 1.Sisco Cherop 2.Salha Oweci 3.Nabukenya Florence
