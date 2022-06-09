
# Peppermint NFT Landing Page
# -----------------------------------------------------------------

# pip install streamlit_option_menu
# pip install OpenCV 

# Initial Imports
# ----------------------------
import json
import os
from eth_utils import to_list
from sympy import product
from web3 import Web3
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from apps import  pepper_functions as pepper_fn
from more_itertools import one
import cv2
import time
import qrcode
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

#page config function
st.set_page_config(
  page_title='Mint Your Product NFT', 
  page_icon="./images/pg_icon.png",
  initial_sidebar_state="expanded",
  layout="wide"
  )

# Turn off native Straemlit display features
hide_streamlit_features ="""
    <style>
      #MainMenu {visibility: hidden;}      
      header {visibility: hidden;}   
      footer {visibility: hidden;}
    </style> """
st.markdown(hide_streamlit_features, unsafe_allow_html= True)

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Product Authentication df
df= pd.read_csv("./products_DB/product_info.csv")

#################################################################
# Main Page Content
#################################################################

@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():
    
    # Load ABI
    with open(Path('./contracts/compiled/peppermint_abi.json')) as f:
        peppermint_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
   
    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=peppermint_abi
    )
    # Return the contract from the function
    return contract

#Load the contract
contract = load_contract()

accounts = w3.eth.accounts
account = accounts[0]
customer_account = st.sidebar.selectbox("Select Account", options=accounts)

# Initializing Main Menu
# ----------------------------------------
selected = pepper_fn.main_menu()

# Home ----------------------------
if selected == "Home":    
    st.markdown(" ### IS YOUR PRODUCT GENUINE ? ")

    if st.button("Authenticate My Product and Mint NFT!"):
        st.warning(" #### Webcam window may open minimized!")
        with st.spinner('Accessing Webcam ...'):
                time.sleep(3)
        # scanning product QR-code
        product_hashcode = pepper_fn.scan()    
        
        # Authenticating product agains manufacturer's df
        row = df.loc[df['hashcode'] == product_hashcode].set_index(["hashcode"])    
        
        if not row.empty and row['minted'].bool():
            #converting row series to dict
            row["minted"] = "FALSE"
            df.loc[df["hashcode"] == product_hashcode, ["minted"]] = "FALSE"
            product_info = row.to_dict()

            st.success("Your Product Authenticated!")

            tx_hash = contract.functions.mintCEGH(customer_account, json.dumps(product_info)).transact({'from': account, 'gas': 1000000})
            #print transaction receipt
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Your NFT has been PepperMinted!")
            
            #updating the minted status
            df.to_csv("./products_DB/product_info.csv",index=False)        
            st.write(dict(product_info))
            image = row.iloc[0,3]        
            st.image(image)        
            st.success("### Transaction Receipt")       
            st.write(dict(receipt))

        else:
            st.warning("Invalid or already used hashcode")
 

# About ----------------------------
elif selected == "About":
    st.title("About this dApp:")
    st.markdown(""" By using Peppermint you can mint NFT of your genuine product, ONLY 1 STEP : Scan product's QR-code !""")
    st.markdown(""" Current version works with Ganache accounts and peppermints NFT using Solidity. """)
    
    st.success("Developers:") 
    devs ="""
        <p> Gaetano </p>
        <p> Ebad </p> 
        <p> Hari </p>
        <p> Charbel </p>
        """
    st.markdown(devs, unsafe_allow_html= True)
    st.success("Source Code")    
    st.markdown("""The Source Code can be found in our [Github Repository](https://github.com/charbelnehme/capstone-project)""")
    



# @st.cache
# Footer
# -----------------------------------------------------------------
