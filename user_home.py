import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import joblib
user=st.session_state['user']
city=user[3]
import pyowm
owm = pyowm.OWM('11081b639d8ada3e97fc695bcf6ddb20')
try:
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    humd = weather.humidity
    sky = weather.detailed_status
    rain = weather.rain.get('1h', 0)
except:
    st.write(city)
    temp=25
    humd=50
    sky='Snow'
    rain=100
def seasonal():
    
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/226/390/small_2x/ai-generated-nature-landscapes-background-free-photo.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;  /* Ensure the background covers the whole screen */
            background-color: rgba(255, 255, 255, 0.7); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<h1 style='text-align: center; color:red;'>Seasonal Trend Analysis</h1>", unsafe_allow_html=True)
    st.markdown('---')
    df=pd.read_csv("Crop_recommendation.csv")
    col1, col2 = st.columns([5,5])
    district=col1.selectbox('Select District',df['District'].unique())
    season=col2.selectbox('Select Season',df['Season'].unique())   
    k=season.split('(')[0]
    df=df[(df['District']==district) & (df['Season']==k)]
    crops=df['Crop'].unique()
    k=str(k)
    crop_images=pd.read_csv('Crops.csv')
    crop_images=crop_images.set_index('Crop')
    col1, col2, col3=st.columns([10,5,10])
    if col2.button('Submit',type='primary'):
        st.markdown('---')
        col1,col2,col3=st.columns([5,5,5])
        try:
            for i in range(0,len(crops),3):
                with col1:
                    if i<len(crops):
                        st.image(crop_images.loc[crops[i],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i]}</h5>", unsafe_allow_html=True)
                with col2:
                    if i+1<len(crops):
                        st.image(crop_images.loc[crops[i+1],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i+1]}</h5>", unsafe_allow_html=True)
                with col3:
                    if i+2<len(crops):
                        st.image(crop_images.loc[crops[i+2],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i+2]}</h5>", unsafe_allow_html=True)
        except:
            pass

def fertilizer():
    try:
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-image: url('https://eos.com/wp-content/uploads/2023/11/components-of-different-types-of-fertilizers.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                min-height: 100vh;  /* Ensure the background covers the whole screen */
                background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent overlay */
                background-blend-mode: overlay; /* Blend the image with the overlay */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"<h1 style='text-align: center; color:blue;'>Fertilizer Recommendation System</h1>", unsafe_allow_html=True)
        pass
    except:
        pass
def yield_prediction():
    # Load the dataset
        data = pd.read_csv('crop_data.csv') 
        X = data.drop(['CROP_PRICE', 'CROP'], axis=1)  # Features
        y = data['CROP_PRICE']  # Target variable

        # One-hot encoding for categorical variables
        X = pd.get_dummies(X)
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area with transparency */
            .main {
                background-image: url('https://img.freepik.com/free-photo/detail-rice-plant-sunset-valencia-with-plantation-out-focus-rice-grains-plant-seed_181624-25838.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent overlay */
                background-blend-mode: overlay; /* Blend the image with the overlay */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
def user_home_page():
    # Navigation menu for user dashboard

    with st.sidebar:
        st.markdown(f"<h1 style='text-align: center; color: black;'><b>🏡Dashboard</b></h1>", unsafe_allow_html=True)

        selected_tab = option_menu(
            menu_title=None,
            options=["Seasonal Based Crops", "Fertilizers", 'Crop Recommendation','Yield Prediction','Logout'],
        styles={
        "nav-link-selected": {"background-color": "green", "color": "white", "border-radius": "5px"},
        }
        )
        user=st.session_state['user']
        location=user[3]
        col1,col2=st.columns([1,1])
        col1.markdown(f"<h1 style='text-align: center; color:black;'>{temp}🌞</h1>", unsafe_allow_html=True)
        col2.markdown(f"<h1 style='text-align: center; color:black;'>{sky}🌥️</h1>", unsafe_allow_html=True)

    if selected_tab == "Seasonal Based Crops":
        seasonal()
    elif selected_tab == "Fertilizers":
        fertilizer()
    elif selected_tab == "Yield Prediction":
        yield_prediction()
    elif selected_tab == "Crop Recommendation":
        pass
    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()