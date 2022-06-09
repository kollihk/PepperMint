
# Ebad's Functions
# -----------------------------------------------------------------

# pip install OpenCV 
# pip install webbrowser ( built in )
# Run in CLI: python QR_Scanner_webcam.py

from more_itertools import one
import cv2
from streamlit_option_menu import option_menu
import streamlit as st
import json
import os
from web3 import Web3
from pathlib import Path


# Straemlit Menu
# -----------------------------------------------------------------
# Repo: https://github.com/victoryhb/streamlit-option-menu
def main_menu():        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "About"],  # required
            icons=["house", "exclamation-circle"],  # optional
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



# WEBCAM QR-CODE SCANNER
# -----------------------------------------------------------------
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
    
    return product_hashcode


