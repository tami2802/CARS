import streamlit as st
import joblib

# Charger le modèle
model = joblib.load('model_2.joblib')

# Titre de l'application
st.title('Prédiction de la dépréciation des voitures d\'occasion')

# Fonction pour faire la prédiction
def predict_depreciation(car_age, present_price, kms_driven, fuel_type, seller_type, transmission):
    features = [[car_age, present_price, kms_driven, fuel_type, seller_type, transmission]]
    prediction = model.predict(features)
    return prediction[0]

# Inputs utilisateur
car_age = st.slider('Âge de la voiture (années)', 0, 20, 1)
present_price = st.number_input('Prix actuel de la voiture (en milliers)', min_value=0.0, max_value=100.0, step=0.1)
kms_driven = st.number_input('Kilomètres parcourus', min_value=0, max_value=500000, step=1000)
fuel_type = st.selectbox('Type de carburant', ('Diesel', 'Petrol'))
seller_type = st.selectbox('Type de vendeur', ('Dealer', 'Individual'))
transmission = st.selectbox('Type de transmission', ('Automatic', 'Manual'))

# Convertir les inputs en indices
fuel_type = 0 if fuel_type == 'Diesel' else 1
seller_type = 0 if seller_type == 'Dealer' else 1
transmission = 0 if transmission == 'Automatic' else 1

# Bouton de prédiction
if st.button('Prédire la dépréciation'):
    result = predict_depreciation(car_age, present_price, kms_driven, fuel_type, seller_type, transmission)
    st.write(f'La dépréciation estimée est de: {result}')

# Commande pour exécuter l'application : streamlit run app.py
