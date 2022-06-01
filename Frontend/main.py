
# QR-Your-NFT Landing Page
# -----------------------------------------------------------------

# pip install streamlit_option_menu
# pip install OpenCV 

# Initial Imports
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
# from apps import  Webcam_QRCode_Scanner # menu, mint home, user_account, about # import your app modules here
from more_itertools import one
import cv2
import qrcode
import pandas as pd


#page config function
st.set_page_config(
  page_title='Mint Your Product NFT', 
  # page_icon=favicon, 
  page_icon=":bounding-box:",
  layout="wide"
  )

# Turn off native Straemlit display features
hide_streamlit_features ="""
    <style>
      #MainMenu {visibility: hidden;}
      svg {visibility: hidden;}
      header {visibility: hidden;}   
      footer {visibility: hidden;}
    </style> """
st.markdown(hide_streamlit_features, unsafe_allow_html= True)

# Link local CSS
st.markdown('<link rel="stylesheet" href="./style/style.css" crossorigin="anonymous">', unsafe_allow_html=True)

# Product Authentication df
df= pd.read_csv("./products_DB/product_info.csv", index_col=3)

# Straemlit Menu
# Repo: https://github.com/victoryhb/streamlit-option-menu
def streamlit_menu():        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Mint NFT", "Account", "About"],  # required
            icons=["house", "bounding-box", "person", "exclamation-circle"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "small"},
                "nav-link": {
                    "font-size": "small",
                    "text-align": "center",
                    "margin": "0",
                    "--hover-color": "#FF5733"
                },
                "nav-link-selected": {"background-color": "#FF5733"},
            },
        )
        return selected


# Webcam QR Scanner
def scan():
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _,img = cap.read()    
        # detect and decode
        data, one, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if data:
            product_hashcode = data
            break
        cv2.imshow('Scan Your Product QR code', img)
        if cv2.waitKey(1) == 27:
            break
   
    cap.release()
    cv2.destroyAllWindows()
    
    return (product_hashcode)


# Main Page Content
# -----------------------------------------------------------------
# @st.cache

selected = streamlit_menu()

# Home ----------------------------
if selected == "Home":    
    st.title("Mint NFT of your Purchased Product By Scanning it's QR Code!")
    # st.write("Simply Scan to Connect your Metamask and Mint NFT")
    # st.image('./images/QR.png')    


# Mint NFT ----------------------------
if selected == "Mint NFT":
    st.title("Mint NFT via Metamask")
    st.text("******")
     
    if st.button("Authenticate My Shoes"):
        # st.text(" Run Webcam!")
        product_hashcode = scan()
        st.text(product_hashcode)
       



      
# My Account --------------------------
if selected == "Account":
    st.title("Account Balance")
    st.text("******")    

    st.header('**Gallery**')
    # st.dataframe(df)


# About ----------------------------
if selected == "About":
    st.title("About this dApp:")
    st.markdown("""Lorem Ipsum, sometimes referred to as 'lipsum', is the placeholder text used in design when creating content. It helps designers plan out where the content will sit, without needing to wait for the content to be written and approved. It originally comes from a Latin text, but to today's reader, it's seen as gibberish.""")
    
    st.title("Developers:") 
    devs ="""
        <p> Gaetano </p>
        <p> Ebad </p> 
        <p> Hari </p>
        <p> Charbel </p>
        """
    st.markdown(devs, unsafe_allow_html= True)
    st.title("Source Code")    
    st.markdown("""The Source Code can be found in our [Github Repository](https://github.com/charbelnehme/capstone-project)""")
    



# @st.cache
# Footer
# -----------------------------------------------------------------
