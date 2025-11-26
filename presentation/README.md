Autism Spectrum Disorder (ASD) Early Prediction in Children  
Group 15 – Final Year Machine Learning Project with Refactory Academy
Presentations made on 27th november 2025

FINAL MODEL PERFORMANCE 
| Model             | Accuracy | Precision | Recall | F1-Score | Confusion Matrix          |
|-------------------|----------|-----------|--------|----------|---------------------------|
| Random Forest | 96.22% | 0.97    | 0.96   | 0.96     | [[165, 17]\n [13, 202]]   |
| Neural Network    | 92.95%   | 0.93      | 0.94   | 0.94     | [[168, 14]\n [13, 202]]   |

Live Deployment: https://your-streamlit-app.streamlit.app (update after deploy)

Unique Dataset  
- 1986 real clinical records (cleaned from 1986 → 1950+ rows after fixing bad entries)  
- 30+ rich features: A1–A10 screening, Q-CHAT-10, CARS, developmental milestones, comorbidities  
- Perfectly balanced target (`ASD_traits`: Yes/No)
- 
Models Used (As Per Your Training)
1. Random Forest →  96.22% (saved as best model)  
2. Deep Neural Network (TensorFlow/Keras) → 92.95%
## Repository Structure
