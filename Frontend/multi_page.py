# QR Your NFT Landing Page

# pip install streamlit_option_menu

# Initial Imports
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
# from sqlalchemy import Column


# favicon and page title
favicon = Image.open('./images/pg_icon.png')

#page config function
st.set_page_config(
  page_title='QR YOUR NFT', 
  # page_icon=favicon, 
  page_icon=":bounding-box:",
  layout="wide"
  )

# Link local CSS
# st.markdown('<link rel="stylesheet" href="./.streamlit/style.css" crossorigin="anonymous">', unsafe_allow_html=True)

# Link CSS for Bootstrap
# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


# Turn off native Straemlit display features
hide_streamlit_features ="""
    <style>
      #MainMenu {visibility: hidden;}
      svg {visibility: hidden;}
      header {visibility: hidden;}   
      footer {visibility: hidden;}
    </style> """
st.markdown(hide_streamlit_features, unsafe_allow_html= True)

# Straemlit Menu
# Repo: https://github.com/victoryhb/streamlit-option-menu
def streamlit_menu():        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Mint NFT", "My Account", "About"],  # required
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

selected = streamlit_menu()

# Main Page Content
# -----------------------------------------------------------------


# Home ----------------------------
if selected == "Home":    
    st.title("Mint Your NFT The Easy Way!")
    st.text("Simply Scan to Connect your Metamask and Mint NFT")
    st.image('./images/QR.png')
    

# Mint NFT ----------------------------
if selected == "Mint NFT":
    st.title("Mint NFT via Metamask")
    st.text("******")
      

# My Account --------------------------
if selected == "My Account":
    st.title("Account Balance")
    st.text("******")    
    st.header('**Gallery**')
    # st.dataframe(df)


# About ----------------------------
if selected == "About":
    st.title("About this dApp:")
    st.text("Lorem Ipsum, sometimes referred to as 'lipsum', is the placeholder text used in design when creating content. It helps designers plan out where the content will sit, without needing to wait for the content to be written and approved. It originally comes from a Latin text, but to today's reader, it's seen as gibberish.")
    
    st.title("Developers:")

    st.title("Github Repository")
    st.text("https://github.com/charbelnehme/capstone-project")
    st.markdown("""
    
    """)

# Main Page Content
# -----------------------------------------------------------------
# st.markdown('''# **Mint Your NFT The Easy Way!**
# Simply Connect your Metamask, Scan And Mint NFT:''')

# # st.markdown("""
# #     <img src="./images/QR.svg"></img>
# # """, unsafe_allow_html=True)
# st.image('./images/QR.png')


# st.header('**Select Your NFT**')


# # 3 Column Layout
# # col1, col2, col3 = st.columns(3)






# Footer
# -----------------------------------------------------------------
# st.markdown('''# **Mint Your NFT The Easy Way!**
# st.info('Team: Gaetano, Hari, Charbel, Ebad')

# st.markdown("""
# <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
# """, unsafe_allow_html=True)
