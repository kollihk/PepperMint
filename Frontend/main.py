
# Secret NFT Collection Landing Page
# -----------------------------------------------------------------

# pip install streamlit_option_menu
# pip install OpenCV 

# Initial Imports
# -----------------------------------------------------------------
from ast import While
from cProfile import run
import pandas as pd
import streamlit as st
from PIL import Image
from apps import  my_functions as myfn    # import your app modules here. menu, mint home, user_account, about 
import time


# @st.cache(suppress_st_warning=True)

#page config function and CSS styling
# -----------------------------------------------------------------
st.set_page_config(
  page_title='Secret NFT Collection', 
  # page_icon=favicon,   
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


#################################################################
# Main Page Content
#################################################################


# Product Authentication df
# -----------------------------------------------------------------
df= pd.read_csv("./products_DB/product_info.csv") #hashcode indexed

# Initializing Main Menu
# -----------------------------------------------------------------
selected = myfn.main_menu()

# Home ----------------------------
if selected == "Home":
    st.title("Secret NFT Collection")
    st.markdown(""" Scan your QR-Code and Mint Your NFT via Metamask! """)        
        
    if st.button("Authenticate My Shoes"):
        st.text("Webcam window may open minimized!")
        with st.spinner('Accessing Webcam ...'):
            time.sleep(2)                       
        scanned_hashcode = myfn.scan()
        
        # Authenticating product agains manufacturer's df
        for i in range(len(df)):
            if df.iloc[i, 0] == scanned_hashcode:        
                prd_index = df.iloc[i]
                print("Scanned Hashcode:" , scanned_hashcode, "\n")        
        
                # single-product df via scanned_hashcode 
                prd_df = pd.DataFrame(prd_index).T
                prd_df.set_index(['hashcode'], inplace=True)
                st.dataframe(prd_df)


    # st.write("")
    # st.image('./images/QR.png')


# Mint NFT ----------------------------
if selected == "Mint NFT":
    st.title("Mint NFT via Metamask")
    st.text("******")



      
# Account --------------------------
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
