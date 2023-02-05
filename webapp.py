import streamlit as st
import pickle
import numpy as np

dt_model=pickle.load(open('dt_model.pkl','rb'))
knn_model=pickle.load(open('knn_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))

def price(num):
    if num==0.0:
        return 'Lowest Range Price'
    elif num == 1.0:
        return 'Low Range Price'
    elif num == 2.0:
        return 'Mid Range Price'
    else:
        return 'High Range Price'
    
def main():
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Mobile Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Decision Tree','K-Nearest Neighbors','Logistic Regression']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    battery_power=st.slider('Total energy a battery can store in one time measured in mAh', 0.0, 2000.0)
    clock_speed=st.slider('speed at which microprocessor executes', 0.0, 3.0)
    fc=st.slider('Front Camera mega pixels', 0.0, 50.0)
    int_memory=st.slider('Internal Memory in Gigabytes', 0.0, 64.0)
    m_dep=st.slider('Mobile Depth in cm', 0.0, 1.0)
    mobile_wt=st.slider('Weight of mobile phone', 0.0, 250.0)
    n_cores=st.slider('Number of cores of processor', 0.0, 8.0)
    pc=st.slider('Primary Camera mega pixels', 0.0, 50.0)
    px_height=st.slider('Pixel Resolution Height', 0.0, 2000.0)
    px_width=st.slider('Pixel Resolution Width', 0.0, 2000.0)
    ram=st.slider('Random Access Memory in Megabytes', 0.0, 8000.0)
    sc_h=st.slider('Screen Height of mobile in cm', 0.0, 20.0)
    sc_w=st.slider('Screen Width of mobile in cm', 0.0, 20.0)
    talk_time=st.slider('Talk time in hour', 0.0, 25.0)
    options = ["Yes", "No"]

    blue = st.selectbox("Has bluetooth?", options)
    if blue == "Yes":
        blue = 1.0
    else:
        blue = 0.0

    dual_sim = st.selectbox("Has dual sim support?", options)
    if dual_sim == "Yes":
        dual_sim = 1.0
    else:
        dual_sim = 0.0

    four_g = st.selectbox("Has 4G?", options)
    if four_g == "Yes":
        four_g = 1.0
    else:
        four_g = 0.0

    three_g = st.selectbox("Has 3G?", options)
    if three_g == "Yes":
        three_g = 1.0
    else:
        three_g = 0.0

    touch_screen = st.selectbox("Has touch screen?", options)
    if touch_screen == "Yes":
        touch_screen = 1.0
    else:
        touch_screen = 0.0

    wifi = st.selectbox("Use Wifi?", options)
    if wifi == "Yes":
        wifi = 1.0
    else:
        wifi = 0.0
    
    inputs=[[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]]
    if st.button('Predict'):
        if option=='Decision Tree':
            st.success(price(dt_model.predict(inputs)))
        elif option=='K-Nearest Neighbors':
            st.success(price(knn_model.predict(inputs)))
        else:
           st.success(price(log_model.predict(inputs)))


if __name__=='__main__':
    main()