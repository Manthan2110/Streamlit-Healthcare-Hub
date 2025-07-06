import streamlit as st
import pickle
import joblib
from streamlit_option_menu import option_menu
from datetime import datetime

st.set_page_config(layout="wide")

def local_css(css_code):
    st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)

local_css("""
/* Center titles and give space */
h1{
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Sidebar styling */
.css-1d391kg {
    padding-top: 20px;
}

[data-testid="stSidebar"] {
    background-color: #1E1E1E;
    color: white;
}

/* Predict button */
button[kind="secondary"] {
    border: 1px solid #00C4CC !important;
    color: #00C4CC !important;
}

button:hover {
    background-color: #00C4CC !important;
    color: black !important;
}

/* Download button */
button[title="Download Report"] {
    background-color: #252525;
    color: white;
    border: 1px solid #666;
    border-radius: 8px;
}

/* Multiselect pills */
.css-1hynsf2 {
    background-color: #ff4b4b !important;
    color: white !important;
}
""")

# Load models with error handling
try:
    diabetes_model = pickle.load(open('C:/Users/manth/Deep_Learning_Project/diabetes_model.pkl', 'rb'))
    heart_disease_model = pickle.load(open('C:/Users/manth/Deep_Learning_Project/heart_disease_model.pkl', 'rb'))
    parkinsons_model = pickle.load(open('C:/Users/manth/Deep_Learning_Project/parkinsons_model.pkl', 'rb'))
    breast_cancer_model = pickle.load(open('C:/Users/manth/Deep_Learning_Project/breast_cancer_model.pkl', 'rb'))
    model = joblib.load("Random_forest_model.pkl")
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    st.stop()

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Smart Medical Diagnosis Tool',
                           ['Infectious/Skin Disease Prediction',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            "Parkinson's Prediction",
                            'Breast Cancer Prediction'],
                           menu_icon="hospital",
                           icons=['clipboard2-pulse', 'activity', 'heart', 'person', 'heart-pulse'],
                           default_index=0)

# Infectious/Skin Disease Prediction
if selected == 'Infectious/Skin Disease Prediction':

    disease_mapping = {
        0: '(vertigo) Paroymsal  Positional Vertigo', 1: 'AIDS', 2: 'Acne', 3: 'Alcoholic hepatitis',
        4: 'Allergy', 5: 'Arthritis', 6: 'Bronchial Asthma', 7: 'Cervical spondylosis',
        8: 'Chicken pox', 9: 'Chronic cholestasis', 10: 'Common Cold', 11: 'Dengue',
        12: 'Diabetes ', 13: 'Dimorphic hemmorhoids(piles)', 14: 'Drug Reaction',
        15: 'Fungal infection', 16: 'GERD', 17: 'Gastroenteritis', 18: 'Heart attack',
        19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E',
        23: 'Hypertension ', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 26: 'Hypothyroidism',
        27: 'Impetigo', 28: 'Jaundice', 29: 'Malaria', 30: 'Migraine', 31: 'Osteoarthristis',
        32: 'Paralysis (brain hemorrhage)', 33: 'Peptic ulcer diseae', 34: 'Pneumonia',
        35: 'Psoriasis', 36: 'Tuberculosis', 37: 'Typhoid', 38: 'Urinary tract infection',
        39: 'Varicose veins', 40: 'hepatitis A'
    }

    symptom_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
                    'shivering', 'chills', 'stomach_pain', 'acidity',
                    'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
                    'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets']

    st.title("Symptom-to-Disease Analyzer")
    st.markdown("### 👨‍⚕️ Doctor-Trusted Symptom Checker")

    selected_symptoms = st.multiselect("🔍 Select Symptoms:", symptom_list)

    if st.button("🩺 Predict Disease"):
        if not selected_symptoms:
            st.warning("⚠️ Please select at least one symptom.")
        else:
            input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptom_list]
            prediction_encoded = model.predict([input_data])[0]
            predicted_disease = disease_mapping.get(prediction_encoded, "Unknown Disease")
            st.success(f"Predicted Disease: **{predicted_disease}**")

            recommendations = {
                '(vertigo) Paroymsal Positional Vertigo': "Perform targeted vestibular exercises and avoid rapid head movements; consult your ENT specialist if episodes persist.",
                'AIDS': "Strictly follow your antiretroviral therapy, maintain a balanced diet, and have regular check-ups to monitor your immune status.",
                'Acne': "Maintain a gentle skincare routine, avoid harsh products, and consider seeing a dermatologist for persistent breakouts.",
                'Alcoholic hepatitis': "Abstain from alcohol immediately and adhere to a specialized treatment plan and liver-friendly diet under your doctor’s guidance.",
                'Allergy': "Identify and avoid known allergens, use antihistamines as needed, and consider professional advice for long-term management.",
                'Arthritis': "Engage in low-impact exercises, incorporate anti-inflammatory foods in your diet, and use pain management strategies as advised by your doctor.",
                'Bronchial Asthma': "Follow your inhaler regimen without fail, avoid known triggers, and monitor symptoms regularly with your pulmonologist’s help.",
                'Cervical spondylosis': "Practice proper posture, perform neck-strengthening exercises, and use prescribed therapies to alleviate discomfort.",
                'Chicken pox': "Rest well, stay hydrated, use soothing lotions for itching, and isolate yourself to prevent spreading the virus.",
                'Chronic cholestasis': "Follow your doctor’s treatment plan, monitor liver function tests regularly, and adhere to dietary recommendations that reduce liver strain.",
                'Common Cold': "Rest, keep yourself well-hydrated, and use over-the-counter remedies to ease symptoms while your body recovers.",
                'Dengue': "Stay hydrated, use paracetamol for fever (avoiding NSAIDs), and seek medical care promptly if symptoms worsen.",
                'Diabetes ': "Monitor your blood sugar levels consistently, follow dietary and exercise guidelines, and take medications as prescribed.",
                'Dimorphic hemmorhoids(piles)': "Increase your fiber intake, drink plenty of water, and use topical treatments or seek medical advice to ease discomfort.",
                'Drug Reaction': "Discontinue the suspected medication immediately and consult your healthcare provider for proper evaluation and treatment.",
                'Fungal infection': "Maintain good hygiene, keep affected areas dry, and apply antifungal medications as directed by your doctor.",
                'GERD': "Avoid trigger foods, eat smaller meals, and consider lifestyle modifications alongside your prescribed acid-reducing treatments.",
                'Gastroenteritis': "Stay well-hydrated with oral rehydration solutions, follow a bland diet, and rest until your symptoms improve.",
                'Heart attack': "Follow your cardiologist’s rehabilitation program, adopt a heart-healthy lifestyle, and strictly adhere to your medication schedule.",
                'Hepatitis B': "Stick to your antiviral regimen, monitor your liver function regularly, and maintain lifestyle adjustments that support liver health.",
                'Hepatitis C': "Complete your full course of antiviral therapy, keep regular appointments for liver monitoring, and consider dietary modifications for overall wellness.",
                'Hepatitis D': "Follow your doctor's treatment plan diligently, avoid alcohol, and have regular liver function evaluations to manage your condition.",
                'Hepatitis E': "Rest, maintain proper hydration, and follow your healthcare provider’s recommendations for supportive recovery of liver function.",
                'Hypertension ': "Monitor your blood pressure at home, reduce sodium intake, exercise regularly, and take your antihypertensive medications as prescribed.",
                'Hyperthyroidism': "Adhere to your prescribed treatment plan, avoid stimulants that exacerbate symptoms, and have your thyroid levels monitored regularly.",
                'Hypoglycemia': "Eat balanced, frequent meals that include complex carbohydrates, keep quick-sugar snacks available, and adjust medications only as advised by your doctor.",
                'Hypothyroidism': "Take your thyroid hormone replacement consistently, have your levels checked periodically, and maintain a balanced diet to support overall health.",
                'Impetigo': "Keep the affected area clean, avoid scratching, and use the prescribed topical or oral antibiotics to contain the infection.",
                'Jaundice': "Follow your physician’s advice for liver support, maintain adequate hydration, and avoid strenuous activities while recovering.",
                'Malaria': "Complete the full course of antimalarial medications, ensure rest and hydration, and seek medical attention if symptoms do not improve.",
                'Migraine': "Identify and avoid known triggers, rest in a quiet darkened room during episodes, and use your prescribed migraine medications for relief.",
                'Osteoarthristis': "Engage in gentle, regular exercises, manage your weight, and use pain relief strategies as recommended by your healthcare provider.",
                'Paralysis (brain hemorrhage)': "Participate in a comprehensive rehabilitation program with physical and occupational therapy under close medical supervision.",
                'Peptic ulcer diseae': "Avoid spicy and acidic foods, follow your medication regimen, and adopt stress-reduction techniques to support ulcer healing.",
                'Pneumonia': "Complete your prescribed antibiotics, get plenty of rest, and monitor your breathing while following up with your doctor for recovery.",
                'Psoriasis': "Maintain a regular skincare routine, manage stress, and explore treatment options like topical therapies or light therapy under your dermatologist’s care.",
                'Tuberculosis': "Strictly adhere to the full course of TB medications, ensure proper nutrition, and attend all follow-up appointments to track your progress.",
                'Typhoid': "Complete your prescribed antibiotics, maintain good hydration and sanitation, and follow dietary advice during the illness recovery.",
                'Urinary tract infection': "Drink plenty of water, complete your full course of antibiotics, and practice proper hygiene to reduce the risk of recurrence.",
                'Varicose veins': "Elevate your legs when resting, engage in regular low-impact exercises, and discuss options like compression stockings with your specialist.",
                'hepatitis A': "Rest adequately, follow a light and nutritious diet, stay hydrated, and adhere to your healthcare provider’s advice for liver recovery."
            }

            recommendation = recommendations.get(predicted_disease, "Please consult a doctor for further evaluation.")
            st.info(f"💡 Recommendation: {recommendation}")

            # Download Report
            report = f"""Smart Medical Diagnosis Report
            Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

            Selected Symptoms: {', '.join(selected_symptoms)}
            Predicted Disease: {predicted_disease}
            Recommendation: {recommendation}
            """
            st.download_button("📥 Download Report", report, file_name="Infectious_Disease_Report.txt")

    st.markdown("---")
    st.caption("© 2025 Smart Diagnosis | Built for educational and assistive purposes.")

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using ML")
    st.markdown("""
    Diabetes is a chronic metabolic condition that affects how the body processes blood sugar. 
    Early detection and lifestyle management are key to preventing complications such as nerve damage,
    kidney failure, and heart disease. 
    This tool leverages machine learning to predict the likelihood of diabetes based on vital health
    indicators like glucose levels, insulin, and BMI.
     
    🧾 **Please fill in the details below to test diabetes risk.**
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
        skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.0, format="%.1f")
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.4f")

    with col2:
        glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0, format="%.1f")
        insulin = st.number_input("Insulin Level (mu U/mL)", min_value=0.0, format="%.1f")
        age = st.number_input("Age (years)", min_value=1, step=1)

    with col3:
        blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0.0, format="%.1f")
        bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, format="%.2f")

    if st.button("🩺 Predict Diabetes Test Result"):
        input_values = [pregnancies, glucose, blood_pressure, skin_thickness,
                        insulin, bmi, dpf, age]

        prediction = diabetes_model.predict([input_values])[0]

        if prediction == 1:
            st.error("💀 The person is likely **Diabetic**.")
            recommendation = "Monitor blood sugar regularly, follow a low-carb diet, and take prescribed medication."
        else:
            st.success("✅ The person is **Not Diabetic**.")
            recommendation = "Maintain a healthy lifestyle and schedule regular check-ups."

        st.info(f"💡 Recommendation: {recommendation}")

        report = f"""
        Diabetes Risk Report
        -------------------------
        Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        Diagnosis: {'Diabetic' if prediction else 'Not Diabetic'}
        Recommendation: {recommendation}
        """

        st.download_button("📥 Download Report", report, file_name="Diabetes_Report.txt")

    st.markdown("---")
    st.caption("© 2025 Smart Diagnosis | Built for educational and assistive purposes.")

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    st.markdown("""
    Heart disease remains one of the leading causes of death worldwide. Risk factors such 
    as high cholesterol, elevated blood pressure, and abnormal ECG results can be early indicators. 
    This ML-powered tool evaluates multiple clinical parameters to assess the likelihood of heart-related
    conditions, helping users make proactive decisions for heart health.

    🧾 **Please fill in the details below to test diabetes risk.**
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120)
        resting_bp = st.number_input("Resting Blood Pressure")
        rest_ecg = st.selectbox("Resting ECG Results", [0, 1, 2])
        ex_angina = st.selectbox("Exercise Induced Angina", [0, 1])
    with col2:
        sex = st.selectbox("Sex", ["Female", "Male"])
        chol = st.number_input("Serum Cholesterol (mg/dl)")
        max_hr = st.number_input("Max Heart Rate Achieved")
        slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
    with col3:
        chest_pain = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        st_depression = st.number_input("ST Depression Induced by Exercise")
        ca = st.number_input("Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)

    thal = st.selectbox("Thalassemia", [1, 2, 3])
    if st.button('🩺 Heart Disease Test Result'):
        inputs = [Age, Sex, cp, trestbps, chol, fbs, restecg, thalach,
                  exang, oldpeak, slope, ca, thal]
        if '' in inputs:
            st.warning("⚠️ Please fill in all the fields.")
        else:
            inputs = [float(i) for i in inputs]
            heart_prediction = heart_disease_model.predict([inputs])
            if heart_prediction[0] == 1:
                st.success('💓 The person has Heart Disease.')
            else:
                st.success('✅ The person does not have Heart Disease.')

            recommendations = {
                1: "Adopt a heart-healthy lifestyle—limit salt and saturated fats, quit smoking, manage stress, and strictly follow your cardiologist’s advice.",
                0: "Keep maintaining a healthy heart with regular physical activity and routine checkups."
            }
            st.info(f"💡 Recommendation: {recommendations[heart_prediction[0]]}")

            report = f"""Heart Disease Diagnosis Report
                       Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

                       Prediction: {'Heart Disease Detected' if heart_prediction else 'No Heart Disease'}
                       Recommendation: {recommendation}
                       """
            st.download_button("📥 Download Report", report, file_name="Heart_Report.txt")

    st.markdown("---")
    st.caption("© 2025 Smart Diagnosis | Built for educational and assistive purposes.")

# Parkinson's Prediction
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    st.markdown("""
    Parkinson’s Disease is a progressive neurological disorder that affects movement, 
    speech, and balance. It can be challenging to diagnose in its early stages. 
    This predictive model uses vocal measurements and signal processing features to analyze 
    potential signs of Parkinson’s, offering early alerts for further medical assessment and intervention.

    🧾 **Please fill in the details below to test parkinsons risks.**
    """)

    features = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
                'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
                'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
                'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
                'spread1', 'spread2', 'D2', 'PPE']

    inputs = []
    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(features):
                with cols[j]:
                    inputs.append(st.text_input(features[i + j]))

    if st.button("🩺 Parkinson's Test Result"):
        if '' in inputs:
            st.warning("⚠️ Please fill in all the fields.")
        else:
            inputs = [float(i) for i in inputs]
            parkinson_prediction = parkinsons_model.predict([inputs])
            if parkinson_prediction[0] == 1:
                st.success("🧾 The person has Parkinson's Disease.")
            else:
                st.success("✅ The person does not have Parkinson's Disease.")

            recommendations = {
                1: "Take prescribed medications on schedule, engage in physical and speech therapy, and maintain a supportive daily routine to enhance mobility.",
                0: "Maintain brain health with regular activity and report any early symptoms to a neurologist."
            }
            st.info(f"💡 Recommendation: {recommendations[parkinson_prediction[0]]}")

            report = f"""Parkinson's Disease Diagnosis Report
            Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

            Prediction: {'Parkinson Disease Detected' if parkinson_prediction else 'No Parkinson Disease'}
            Recommendation: {recommendation}
            """
            st.download_button("📥 Download Report", report, file_name="Parkinson_Report.txt")

    st.markdown("---")
    st.caption("© 2025 Smart Diagnosis | Built for educational and assistive purposes.")

# Breast Cancer Prediction
if selected == 'Breast Cancer Prediction':
    # 💗 Title and description
    st.title("Breast Cancer Prediction using ML")
    st.markdown("""
    Breast cancer is one of the most common cancers affecting women worldwide. Early detection significantly increases the chances of successful treatment and survival. This tool uses advanced machine learning algorithms to analyze clinical features and predict whether a breast tumor is likely **Malignant** (cancerous) or **Benign** (non-cancerous).

    🧾 **Please fill in the details below to test breast cancer risk.**
    """)

    # 🎛️ Create 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        worst_area = st.number_input("Worst Area", min_value=0.0, format="%.2f")
        mean_concavity = st.number_input("Mean Concavity", min_value=0.0, format="%.5f")
        mean_radius = st.number_input("Mean Radius", min_value=0.0, format="%.2f")
        mean_area = st.number_input("Mean Area", min_value=0.0, format="%.2f")

    with col2:
        worst_concave_points = st.number_input("Worst Concave Points", min_value=0.0, format="%.5f")
        worst_perimeter = st.number_input("Worst Perimeter", min_value=0.0, format="%.2f")
        worst_concavity = st.number_input("Worst Concavity", min_value=0.0, format="%.5f")
        area_error = st.number_input("Area Error", min_value=0.0, format="%.3f")

    with col3:
        mean_concave_points = st.number_input("Mean Concave Points", min_value=0.0, format="%.5f")
        worst_radius = st.number_input("Worst Radius", min_value=0.0, format="%.2f")
        mean_perimeter = st.number_input("Mean Perimeter", min_value=0.0, format="%.2f")
        worst_compactness = st.number_input("Worst Compactness", min_value=0.0, format="%.5f")

    # Predict button
    if st.button("🎯 Predict Breast Cancer Likelihood"):
        inputs = [
            worst_area, worst_concave_points, mean_concave_points,
            worst_radius, worst_perimeter, mean_perimeter,
            mean_concavity, mean_area, worst_concavity,
            mean_radius, area_error, worst_compactness
        ]

        try:
            float_inputs = [float(i) for i in inputs]
            prediction = breast_cancer_model.predict([float_inputs])[0]

            if prediction == 1:
                st.success("✅ The breast cancer is **Benign**.")
                recommendation = "Benign tumors are non-cancerous. Regular monitoring is advised to ensure early detection of any changes."
            else:
                st.error("💀 The breast cancer is **Malignant**.")
                recommendation = "Follow your oncologist’s treatment plan immediately. This may include surgery, chemotherapy, or other medical procedures."

            st.info(f"💡 Recommendation: {recommendation}")

            # Report generation
            report = f"""
            Breast Cancer Diagnosis Report
            -------------------------------
            Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            Diagnosis: {'Benign' if prediction == 1 else 'Malignant'}
            Recommendation: {recommendation}
            """

            st.download_button("📥 Download Report", report, file_name="Breast_Cancer_Report.txt")

        except Exception as e:
            st.error("❌ Prediction failed. Please check your inputs or model.")
            st.exception(e)

    st.markdown("---")
    st.caption("© 2025 Smart Diagnosis | Built with Streamlit")
