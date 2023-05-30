import streamlit as st
import pickle
import pandas as pd

literature_based_Model = pickle.load(open("CatBoost_based_on_gradation.pkl", "rb"))
Weibull_based_Model = pickle.load(open("Weibull_dist_catboost_model.pkl", "rb"))
Bailey_based_Model = pickle.load(open("Bailey_method_catboost_model.pkl", "rb"))


st.set_page_config(page_title='Dynamic Modulus Prediction',)

st.write("""
        ![](https://engfac.mans.edu.eg/images/logo22-EN.png)
        ## Highway and Airport Engineering Laboratory
        ---
        #### Predicting Dynamic Modulus in (MPa) of Asphalt Concrete Mixture using Catboost Models
        ---
        """
        )
st.markdown("""<div style="text-align: justify;">The prediction of dynamic modulus (E*) of asphalt mixtures is estimated using
three machine learning Catboost regression algorithms.
Both asphalt binder properties and mixture volumetrics are characterized in
the explored models using the same feeding features in the NCHRP 1-37A Witczak Model. However,
three approaches for characterizing aggregate gradation are involved in both types of models:
 literature-based (as provided in the NCHRP 1-37A Witczak Model), Weibull distribution factors, Bailey method parameters.
</div>""", unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["literature-based", "Weibull-based", "Bailey-based"])

with tab1:
    # st.header("literature-based Catboost model")
    st.write("The literature-based Catboost model was developed using sieves representation of gradation")
    Temperature_s = st.number_input('Temperature (C)', 0.00, 100.00,  step=0.1, value=21.1, key=17)
    Frequency_s = st.number_input('Frequency fc (Hz)', 0.00, 100.00,  step=0.1, value=5.00, key=18)
    Viscosity_s = st.number_input('Viscosity ηf,T(cP)', value=1301624000.00, key=19)
    sieve_3_4_s = st.slider('Retained on the 3/4-in. (19-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=2.00, key=20)
    sieve_3_8_s = st.slider('Retained on the 3/8-in. (9-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=24.00, key=21)
    sieve_4_s = st.slider('Retained on the No.4 (4.75-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=46.00, key=22)
    sieve_200_s = st.slider('Passing the No.200 (0.075-mm) sieve (%)', 0.00, 100.00,  step=0.1, value=3.60, key=23)
    va_s = st.slider('Volume of the air voids in the mixture (%)', 0.00, 100.00,  step=0.1, value=6.11, key=24)
    vbeff_s = st.slider('Volume of effective bitumen content (%)', 0.00, 100.00,  step=0.1, value=9.45, key=25)


    column_names_s = ['T (C)', 'fc (Hz)', 'ηf,T(cP)', 'ρ3/4 (%)', 'ρ3/8 (%)', 'ρ4 (%)', 'ρ200 (%)', 'Va (%)', 'Vbeff (%)']
    data_row_s = pd.DataFrame([[Temperature_s, Frequency_s, Viscosity_s, sieve_3_4_s, sieve_3_8_s, sieve_4_s, sieve_200_s, va_s, vbeff_s]], columns=column_names_s)
    print_line = ""
    def prediction_s(in_row):
        E_prediction = literature_based_Model.predict(in_row)[0]
        print_line = f"E* = {round(E_prediction, 3) } MPa"
        return print_line

    if st.button("Predict The E* Value", key="b1"):
        print_line = prediction_s(data_row_s)
    st.success(print_line)

with tab2:
    # st.header("The Weibull-based Catboost model")
    st.write("The Weibull-based Catboost model was developed using Weibull distribution factors (λ and κ)")
    Temperature_w = st.number_input('Temperature (C)', 0.00, 100.00,  step=0.1, value=21.1, key=1)
    Frequency_w = st.number_input('Frequency fc (Hz)', 0.00, 100.00,  step=0.1, value=5.00, key=2)
    Viscosity_w = st.number_input('Viscosity ηf,T(cP)', value=1301624000.00, key=3)
    lambda_w = st.number_input('λ', 0.00, 100.00,  step=0.01, value=5.584, key=4)
    kappa_w = st.number_input('κ', 0.00, 100.00,  step=0.01, value=0.7175, key=5)
    va_w = st.slider('Volume of the air voids in the mixture (%)', 0.00, 100.00,  step=0.1, value=6.11, key=6)
    vbeff_w = st.slider('Volume of effective bitumen content (%)', 0.00, 100.00,  step=0.1, value=9.45, key=7)


    Weibull_column_names = ['T (C)', 'fc (Hz)', 'ηf,T(cP)', 'λ', 'κ', 'Va (%)', 'Vbeff (%)']
    Weibull_data_row = pd.DataFrame([[Temperature_w, Frequency_w, Viscosity_w, lambda_w, kappa_w, va_w, vbeff_w]], columns=Weibull_column_names)
    Weibull_print_line = ""
    def Weibull_prediction(in_row):
        E_prediction = Weibull_based_Model.predict(in_row)[0]
        print_line = f"E* = {round(E_prediction, 3) } MPa"
        return print_line

    if st.button("Predict The E* Value", key="b2"):
        Weibull_print_line = Weibull_prediction(Weibull_data_row)
    st.success(Weibull_print_line)

with tab3:
    # st.header("The Bailey-based Catboost model")
    st.write("The Bailey-based Catboost model was developed using Bailey method parameters (CA, FAC, FAf ratios)")
    Temperature = st.number_input('Temperature (C)', 0.00, 100.00,  step=0.1, value=21.1, key=8)
    Frequency = st.number_input('Frequency fc (Hz)', 0.00, 100.00,  step=0.1, value=5.00, key=9)
    Viscosity = st.number_input('Viscosity ηf,T(cP)', value=1301624000.00, key=10)
    CA_Ratio = st.number_input('CA Ratio', 0.00, 100.00,  step=0.01, value=0.533333, key=11)
    FAc_Ratio = st.number_input('FAc Ratio', 0.00, 100.00,  step=0.01, value=0.574074, key=12)
    FAf_Ratio = st.number_input('FAf Ratio', 0.00, 100.00,  step=0.01, value=2.384615, key=13)
    va = st.slider('Volume of the air voids in the mixture (%)', 0.00, 100.00,  step=0.1, value=6.11, key=15)
    vbeff = st.slider('Volume of effective bitumen content (%)', 0.00, 100.00,  step=0.1, value=9.45, key=16)


    column_names = ['T (C)', 'fc (Hz)','ηf,T(cP)', 'CA Ratio', 'FAc Ratio', ' FAf Ratio', 'Va (%)', 'Vbeff (%)',]
    data_row = pd.DataFrame([[Temperature, Frequency, Viscosity, CA_Ratio, FAc_Ratio, FAf_Ratio, va, vbeff]], columns=column_names)
    print_line = ""
    def prediction(in_row):
        E_prediction = Bailey_based_Model.predict(in_row)[0]
        print_line = f"E* = {round(E_prediction, 3) } MPa"
        return print_line

    if st.button("Predict The E* Value", key="b3"):
        print_line = prediction(data_row)
    st.success(print_line)
