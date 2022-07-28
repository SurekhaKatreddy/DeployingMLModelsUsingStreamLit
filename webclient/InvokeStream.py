#pip install streamlit

import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
model = pickle.load(open('model.pkl','rb'))

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Country, Region, Std_error, Economy, Family, Health, Freedom, Trust, Generosity, Dystopia):
    inference_df = pd.DataFrame({'Country': [Country],
                   'Region': [Region],
                   'Standard Error': [Std_error],
                    'Economy (GDP per Capita)': [Economy],      
                    'Family':[Family],
                    'Health (Life Expectancy)': [Health],
                    'Freedom': [Freedom],
                    'Trust (Government Corruption)':[Trust],
                    'Generosity':[Generosity],
                    'Dystopia Residual': [Dystopia]})
    prediction = model.predict(inference_df)
    #model.predict([[Country, Region, Std_error, Economy, Family, Health, Trust, Generosity, Dystopia]])
    print(prediction)
    return prediction
    

# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    #st.title("World Happiness Indicator")
    
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:8px">
    <h1 style ="color:black;text-align:center;">Happiness Score Prediction ML App </h1>
    </div>
    """
    
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Country = st.text_input("Country", "Sweden")
    Region = st.text_input("Region", "Western Europe")
    Std_error = st.text_input("Std_error", 0.03157)
    Economy = st.text_input("Economy (GDP per Capita)", 1.33171)
    Family = st.text_input("Family", 1.33171)
    Health = st.text_input("Health (Life Expectancy)", 1.28907)
    Freedom = st.text_input("Freedom", 0.91087)
    Trust = st.text_input("Trust (Government Corruption)",0.43844)
    Generosity = st.text_input("Generosity", 0.36262)
    Dystopia = st.text_input("Dystopia Residual", 0.09)

    result =""
    
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Country, Region, Std_error, Economy, Family, Health, Freedom, Trust, Generosity, Dystopia)
    st.success('The output is {}'.format(result))
    
if __name__=='__main__':
    main()