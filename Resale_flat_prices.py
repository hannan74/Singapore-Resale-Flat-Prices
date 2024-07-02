import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle

#Town Mapping
def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(1)
    elif town_map == 'BEDOK':
        town_1 = int(2)
    elif town_map == 'BISHAN':
        town_1= int(3)
    elif town_map == 'BUKIT BATOK':
        town_1= int(4)
    elif town_map == 'BUKIT MERAH':
        town_1= int(5)
    elif town_map == 'BUKIT PANJANG':
        town_1= int(6)

    elif town_map == 'BUKIT TIMAH':
        town_1= int(7)
    elif town_map == 'CENTRAL AREA':
        town_1= int(8)
    elif town_map == 'CHOA CHU KANG':
        town_1= int(9)
    elif town_map == 'CLEMENTI':
        town_1= int(10)
    elif town_map == 'GEYLANG':
        town_1= int(11)
    
    elif town_map == 'HOUGANG':
        town_1 = int(12)
    elif town_map == 'JURONG EAST':
        town_1= int(13)
    elif town_map == 'JURONG WEST':
        town_1= int(14)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1= int(15)
    elif town_map == 'MARINE PARADE':
        town_1= int(16)

    elif town_map == 'PASIR RIS':
        town_1= int(17)
    elif town_map == 'PUNGGOL':
        town_1= int(18)
    elif town_map == 'QUEENSTOWN':
        town_1= int(19)
    elif town_map == 'SEMBAWANG':
        town_1= int(20)
    elif town_map == 'SENGKANG':
        town_1= int(21)

    elif town_map == 'SERANGOON':
        town_1= int(22)
    elif town_map == 'TAMPINES':
        town_1= int(23)
    elif town_map == 'TOA PAYOH':
        town_1= int(24)
    elif town_map == 'WOODLANDS':
        town_1= int(25)        
    elif town_map == 'YISHUN':
        town_1= int(26)      
    elif town_map == 'LIM CHU KANG':
        town_1 = int(27)

    return town_1


#Flat Type Mapping
def flat_type_mapping(flt_type):

    if flt_type == '1 ROOM':
        flat_type_1= int(1)
    elif flt_type == '2 ROOM':
        flat_type_1= int(2)
    elif flt_type == '3 ROOM':
        flat_type_1= int(3)
    elif flt_type == '4 ROOM':
        flat_type_1= int(4)
    elif flt_type == '5 ROOM':
        flat_type_1= int(5)
    elif flt_type == 'EXECUTIVE':
        flat_type_1= int(6)
    elif flt_type == 'MULTI-GENERATION':
        flat_type_1= int(7)

    return flat_type_1


#Flat Model Mapping
def flat_model_mapping(fl_m):

    if fl_m == 'Improved':
        flat_model_1= int(1)
    elif fl_m == 'New Generation':
        flat_model_1= int(2)
        
    elif fl_m == 'Model A':
        flat_model_1= int(3)
    elif fl_m == 'Standard':
        flat_model_1= int(4)
    elif fl_m == 'Simplified':
        flat_model_1= int(5)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(6)
    elif fl_m == 'Apartment':
        flat_model_1= int(7)
    elif fl_m == 'Maisonette':
        flat_model_1= int(8)
    elif fl_m == 'Terrace':
        flat_model_1= int(9)
    elif fl_m == '2-room':
        flat_model_1= int(10)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(11)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(12)
    elif fl_m == 'PREMIUM Apartment':
        flat_model_1= int(13)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(14)
    elif fl_m == 'Premium Apartment':
        flat_model_1= int(15)
    
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(16)
    elif fl_m == 'Model A2':
        flat_model_1= int(17)
    elif fl_m == 'DBSS':
        flat_model_1= int(18)
    elif fl_m == 'Type S1':
        flat_model_1= int(19)
    elif fl_m == 'Type S2':
        flat_model_1= int(20)
    

    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(21)
    elif fl_m == '3Gen':
        flat_model_1= int(22)

    return flat_model_1


#Model
def predict_price(town, flat_type, block, street_name, floor_area_sqm, flat_model, lease_commence_date,
              remaining_lease, resale_year, resale_month, storey_lower_bound, storey_upper_bound):
    
    town_model= town_mapping(town)
    flat_type_model= flat_type_mapping(flat_type)
    block_model= int(block)
    street_name_model= int(street_name)
    floor_area_sqm_model = int(floor_area_sqm)
    flat_model_model= flat_model_mapping(flat_model)
    lease_commence_date_model= int(lease_commence_date)
    remaining_lease_model= float(remaining_lease)
    resale_year_model= int(resale_year)
    resale_month_model= int(resale_month)
    storey_lower_bound_model= int(storey_lower_bound)
    storey_upper_bound_model= int(storey_upper_bound)
    
    


    with open(r"Singapore_Resale_Flat_Prices_Model.pkl","rb") as f:
        regg_model= pickle.load(f)

    user_data = np.array([[town_model, flat_type_model, block_model ,street_name_model,
                           floor_area_sqm_model, flat_model_model, lease_commence_date_model, remaining_lease_model, 
                           resale_year_model, resale_month_model, storey_lower_bound_model, storey_upper_bound_model]])
    
    price = regg_model.predict(user_data)

    return price


#streamlit
st.set_page_config(page_title= "Singapore Flat Resale Price Detection",
                   page_icon="🏨",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Hannanstreamlit run  *!
                                        """}
                  )

st.backgroundColor = '6739B7'

st.header(':violet[SINGAPORE FLAT RESALE PRICE DETECTION]',anchor=False)
st.balloons()

with st.sidebar:
    st.title(":green[CAPSTONE PROJECT-7]")
    st.header("Introduction about Myself")
    st.caption("Name : Mohamed Hannan. S")
    st.caption("Course : Master in DataScience")
    st.caption("Batch : MDE88")

options = option_menu(
                menu_title = "Explore",
                options=["Home", "Price Prediction","About"],
                icons=["house-fill","database-fill","bar-chart-line"],
                default_index = 0,
                menu_icon="cast",
                orientation="horizontal",
                key="navigation_menu",
                styles={
                        "font_color": "#DC143C",   
                        "border": "2px solid #DC143C", 
                        "padding": "10px 25px"   
                    }
            )


if options == "Home":

    st.header("Sinagpore HDB Flats:")

    st.write('''The majority of Singaporeans live in public housing provided by the HDB.
    HDB flats can be purchased either directly from the HDB as a new unit or through the resale market from existing owners.''')
    
    st.header("Resale Process:")

    st.write('''In the resale market, buyers purchase flats from existing flat owners, and the transactions are facilitated through the HDB resale process.
    The process involves a series of steps, including valuation, negotiations, and the submission of necessary documents.''')
    
    st.header("Valuation:")

    st.write('''The HDB conducts a valuation of the flat to determine its market value. This is important for both buyers and sellers in negotiating a fair price.''')
    
    st.header("Eligibility Criteria:")

    st.write("Buyers and sellers in the resale market must meet certain eligibility criteria, including citizenship requirements and income ceilings.")
    
    st.header("Resale Levy:")

    st.write('''For buyers who have previously purchased a subsidized flat from the HDB, there might be a resale levy imposed 
             when they purchase another flat from the HDB resale market.''')
    
    st.header("Grant Schemes:")

    st.write('''There are various housing grant schemes available to eligible buyers, such as the CPF Housing Grant, 
             which provides financial assistance for the purchase of resale flats.''')
    
    
    st.header("Market Trends:")

    st.write('''The resale market is influenced by various factors such as economic conditions, interest rates, and government policies.
              Property prices in Singapore can fluctuate based on these factors.''')
    
    st.header("Online Platforms:")

    st.write("There are online platforms and portals where sellers can list their resale flats, and buyers can browse available options.")


elif options == "Price Prediction":

    col1,col2= st.columns(2)
    with col1:

        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'LIM CHU KANG',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        

        flat_type= st.selectbox("Select the Flat Type", ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE',
                                                        'MULTI-GENERATION'])

        
        block = st.number_input("Enter the Value of Block (Min : 1 / Max: 980)")
        

        street_name = st.number_input("Enter the Value of Street_Name (Min : 1 / Max : 584)")
        
        floor_area_sqm= st.number_input("Enter the Value of Floor Area sqm (Min: 28 / Max: 173)")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Model A-Maisonette', 'Apartment', 'Maisonette', 'Terrace',
                                                        '2-room', 'Improved-Maisonette', 'Multi Generation', 'PREMIUM Apartment', 'Adjoined flat',
                                                        'Premium Apartment', 'Premium Maisonette', 'Model A2',
                                                        'DBSS', 'Type S1', 'Type S2', "Premium Apartment Loft", '3Gen'])
        
    with col2:

        storey_lower_bound= st.number_input("Enter the Value of Storey Lower Bound")

        storey_upper_bound= st.number_input("Enter the Value of Storey Upper Bound")

        resale_year= st.number_input("Enter the Value of Resale Year ")

        resale_month= st.number_input("Enter the Value of Resale Month")
        
        lease_commence_date= st.selectbox("Select the Lease_Commence_Date", [str(i) for i in range(1966,2023)])

        remaining_lease = st.number_input("Enter the Value of Remaining Lease Period (Min: 42 / Max: 98)")

    button= st.button("Predict the Price", use_container_width= True)

    if button:

            
        pre_price= predict_price(town, flat_type, block, street_name, floor_area_sqm, flat_model, lease_commence_date,
                                remaining_lease, resale_year, resale_month, storey_lower_bound, storey_upper_bound)

        st.write("## :green[**The Predicted Price is :**]",pre_price)


elif options == "About":

    st.header(":blue[Data Collection and Preprocessing:]")
    st.write('''Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. 
             Preprocess the data to clean and structure it for machine learning.''')

    st.header(":blue[Feature Engineering:]")
    st.write('''Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date.
              Create any additional features that may enhance prediction accuracy.''')
    
    st.header(":blue[Model Selection and Training:]")
    st.write("Choose an appropriate machine learning model for regression. Train the model on the historical data, using a portion of the dataset for training.")

    st.header(":blue[Model Evaluation:]")
    st.write('''Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), 
              or Root Mean Squared Error (RMSE) and R2 Score.''')

    st.header(":blue[Streamlit Web Application:]")
    st.write('''Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). 
             Utilize the trained machine learning model to predict the resale price based on user inputs.''')

