import os
import json
import pandas as pd
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from  authenticate_sneakers import Product, Database

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load Art Gallery ABI
    with open(Path('./contracts/compiled/certificate_abi.json')) as f:
        certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    # Return the contract from the function
    return contract

################################################################################
# Test Code to create a database of product hashes to authenticate against
################################################################################

# Static database for testing, A csv to be generated and used subsequently
product_dict = {
    'Name': ['Nike','Adidas', 'Sketchers', 'New Balance', 'Fila', 'Nike Jordan', 'Adidas'],
    'Serial Number': [0,1,2,3,4,5,6],
    'Invoice Number': [11,22,33,44,55,66,77],
    'Timestamp': ['2022-03-11 10:00:46','2022-03-12 01:00:46','2022-02-11 11:45:46','2021-12-01 03:00:46','2022-05-11 00:00:46','2022-04-11 12:20:46','2022-04-11 00:10:41']
    }
product_database = pd.DataFrame(product_dict)
# Initialize database

product_hashes = Database([])
#product_database = Database([Products(name="Nike", serial_no=1,invoice=11)])


for index,product in product_database.iterrows():
    db_product = Product(name=product['Name'],serial_no=product['Serial Number'],invoice=product['Invoice Number'],timestamp=product['Timestamp'])
    product_hashes.add_product_hash(db_product.hash_product())

hashes_df = pd.DataFrame(product_hashes.database, columns=['Hash'])
st.write(hashes_df)
################################################################################
# Award Certificate
################################################################################
# Load the contract
contract = load_contract()

accounts = w3.eth.accounts
account = accounts[0]
student_account = st.selectbox("Select Account", options=accounts)

# Create a dict of a product {Name:"",Serial No: int, invoice:int,Timestamp:str, Hash:str}
product_details = {}

product_details['pr_name'] = st.text_input("Enter Product Name:")
product_details['pr_service_no'] = st.text_input("Enter service number:")
product_details['pr_invoice'] = st.text_input("Enter invoice details:")
product_details['pr_timestamp'] = st.text_input("Enter Timestamp:")

# calculate hash and validate

new_product = Product(
                name=product_details['pr_name'],
                serial_no=product_details['pr_service_no'],
                invoice=product_details['pr_invoice'],
                timestamp=product_details["pr_timestamp"]
                )
new_hash = new_product.hash_product()
if st.button("Award Certificate"):

    st.write(new_hash)
# json.dumps(dict)
    if new_hash in product_hashes.database:
        _id = contract.functions.awardCertificate(student_account, json.dumps(product_details)).transact({'from': account, 'gas': 1000000})

################################################################################
# Display Certificate
################################################################################
certificate_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1)

if st.button("Display Certificate"):
    # Get the certificate owner
    certificate_owner = contract.functions.ownerOf(certificate_id).call()
    st.write(f"The certificate was awarded to {certificate_owner}")

    # Get the certificate's metadata
    certificate_uri = contract.functions.tokenURI(certificate_id).call()
    st.write(f"The certificate's tokenURI metadata is {certificate_uri}")
