
# Straemlit Menu ----------------------------

# pip install streamlit_option_menu
# Repo: https://github.com/victoryhb/streamlit-option-menu

# Initial Imports
import streamlit as st
from streamlit_option_menu import option_menu

# Main menu
def app():        
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

selected = app()