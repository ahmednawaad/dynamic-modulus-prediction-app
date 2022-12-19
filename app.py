import streamlit as st
import pickle
import pandas as pd

literature_based_Model = pickle.load(open("CatBoost_based_on_gradation.pkl", "rb"))


st.set_page_config(page_title='Dynamic Modulus Prediction',)

st.write("""
        ![](https://www.mans.edu.eg/images/mans_en_logo.png)
        ## Highway and Airport Engineering Laboratory
        ---
        #### Predicting Dynamic Modulus in (MPa) of Asphalt Concrete Mixture using Catboost Model
        ---
        
        """
        )

Temperature = st.number_input('Temperature (C)', 0.00, 100.00,  step=0.1, value=21.1,)
Frequency = st.number_input('Frequency fc (Hz)', 0.00, 100.00,  step=0.1, value=5.00)
Viscosity = st.number_input('Viscosity ηf,T(cP)', value=1301624000.00)
sieve_3_4 = st.slider('Retained on the 3/4-in. (19-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=2.00)
sieve_3_8 = st.slider('Retained on the 3/8-in. (9-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=24.00)
sieve_4 = st.slider('Retained on the No.4 (4.75-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=46.00)
sieve_200 = st.slider('Passing the No.200 (0.075-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=3.60)
va = st.slider('Volume of the air voids in the mixture (%)', 0.00, 100.00,  step=0.1, value=6.11)
vbeff = st.slider('Volume of effective bitumen content (%)', 0.00, 100.00,  step=0.1, value=9.45)


column_names = ['T (C)', 'fc (Hz)', 'ηf,T(cP)', 'ρ3/4 (%)', 'ρ3/8 (%)', 'ρ4 (%)', 'ρ200 (%)', 'Va (%)', 'Vbeff (%)']
data_row = pd.DataFrame([[Temperature, Frequency, Viscosity, sieve_3_4, sieve_3_8, sieve_4, sieve_200, va, vbeff]], columns=column_names)
print_line = ""
def prediction(in_row):
    E_prediction = literature_based_Model.predict(in_row)[0]
    print_line = f"E* = {round(E_prediction, 3) } MPa"
    return print_line

if st.button("Predict The E* Value"):
    print_line = prediction(data_row)
st.success(print_line)