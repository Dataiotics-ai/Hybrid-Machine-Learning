import pandas as pd
import streamlit as st
import pickle
import warnings
import base64
warnings.filterwarnings("ignore")

with open('./assests/model_pkl' , 'rb') as f:
    model = pickle.load(f)

def predict(holiday, temperature, rain, snow, cloudCoverage, weatherMain, weatherDescription, weekday,hour,month, year):
    Prediction = model.predict([[holiday, temperature, rain, snow, cloudCoverage, weatherMain, weatherDescription, weekday,hour,month, year]])
    return (Prediction[0])


def main():
    html_temp = """
        <div style="background-color:grey;padding:10px">
        <h1 style="color:white;text-align:center;">Traffic Volume Prediction</h1>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    holiday = st.selectbox(
     'Was it a Holiday ?',
     ('Yes', 'No'))
    if holiday == 'Yes':
        holiday = 0
    else:
        holiday = 1
    temperature = st.slider('What was the Temperature?', -50, 50, 0)
    rain = st.selectbox(
     'Was there any Rain today?',
     ('Yes', 'No'))
    if rain == 'Yes':
        rain = 1
    else:
        rain = 0
    snow = st.selectbox(
     'Was there any Snow today?',
     ('Yes', 'No'))
    if snow == 'Yes':
        snow = 1
    else:
        snow = 0
    cloudCoverage =  st.slider('What was the Cloud Coverage Percentage?', 0,100,0)
    weatherMain = st.selectbox('How was the Weather?',
    ('Clear', 'Clouds', 'Drizzle', 'Fog', 'Haze', 'Mist','Rain', 'Smoke', 'Snow', 'Squall', 'Thunderstorm'))
    if weatherMain == 'Clear':
        weatherMain = 0
    elif weatherMain == 'Clouds':
        weatherMain = 1
    elif weatherMain == 'Drizzle':
        weatherMain = 2
    elif weatherMain == 'Fog':
        weatherMain = 3
    elif weatherMain == 'Haze':
        weatherMain = 4
    elif weatherMain == 'Mist':
        weatherMain = 5
    elif weatherMain == 'Rain':
        weatherMain = 6
    elif weatherMain == 'Smoke':
        weatherMain = 7
    elif weatherMain == 'Snow':
        weatherMain = 8
    elif weatherMain == 'Squall':
        weatherMain = 9
    elif weatherMain == 'Thunderstorm':
        weatherMain = 10
    weatherDescription = st.selectbox('What was the Weather Description?',
    ('Broken Clouds','Drizzling','Few Clouds','Foggy','Haze','Heavy Intensity Rain','Heavy Snow','Light Intensity Rain','Light Snow','Mist','Moderate Rain','Overcast Clouds','Scattered Clouds','Clear Sky','Snow','Others'))
    if weatherDescription == 'Broken Clouds':
        weatherDescription = 0
    elif weatherDescription == 'Drizzling':
        weatherDescription = 1
    elif weatherDescription == 'Few Clouds':
        weatherDescription = 2
    elif weatherDescription == 'Foggy':
        weatherDescription = 3
    elif weatherDescription == 'Haze':
        weatherDescription = 4
    elif weatherDescription == 'Heavy Intensity Rain':
        weatherDescription = 5
    elif weatherDescription == 'Heavy Snow':
        weatherDescription = 6
    elif weatherDescription == 'Light Intensity Rain':
        weatherDescription = 7
    elif weatherDescription == 'Light Snow':
        weatherDescription = 8
    elif weatherDescription == 'Mist':
        weatherDescription = 9
    elif weatherDescription == 'Moderate Rain':
        weatherDescription = 10
    elif weatherDescription == 'Overcast Clouds':
        weatherDescription = 12
    elif weatherDescription == 'Scattered Clouds':
        weatherDescription = 13
    elif weatherDescription == 'Clear Sky':
        weatherDescription = 14
    elif weatherDescription == 'Snow':
        weatherDescription = 15
    elif weatherDescription == 'Others':
        weatherDescription = 11
    hour = st.slider('What was the Hour of the Day?', 0, 23, 0)
    date = st.date_input('What was the date?')
    dateConvert = pd.Timestamp(date)
    weekday = dateConvert.dayofweek
    month = dateConvert.month-1 
    year = dateConvert.year
    if st.button("Predict"):
        result = predict(holiday, temperature, rain, snow, cloudCoverage, weatherMain, weatherDescription, weekday,hour,month, year)
        st.success('The Traffic Volume is {}'.format(round(result)))
if __name__=='__main__':
    main()
