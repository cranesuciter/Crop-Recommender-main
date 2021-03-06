import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

from model import Movies , hybrid


st.beta_set_page_config(page_title="Movies Recommender", page_icon="đŦ", layout='centered', initial_sidebar_state="collapsed")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Movies Recommendation  đŦ </h1>
    </div>
    <style>
    body {
    background-image: url("https://s.studiobinder.com/wp-content/uploads/2020/04/Best-Movies-of-2014-Featured.jpg");
    background-size: cover;
    }
    </style>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.beta_columns([2,2])
    
    with col1: 
        with st.beta_expander(" âšī¸ Information", expanded=True):
            st.write("""
            Crop recommendation is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. 
            However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.

            """)
        '''
        ## How does it work â 
        Complete all the parameters and the machine learning model will predict the most suitable crops to grow in a particular farm based on various parameters
        '''


    with col2:
        st.subheader(" Find out the most suitable crop to grow in your farm đ¨âđž")

        option = st.selectbox(
        'How would you like to be contacted?',Movies.title)
        
        if st.button('Predict'):
            col1.write('You selected:', option)
            test = hybrid(1, option)
            col1.write('''
		    ## Results đ 
		    ''')
            col1.success(f"{test.title}")
      #code for html âī¸ đž đŗ đ¨âđž  đ

    st.warning("Note: This A.I application is for educational/demo purposes only and cannot be relied upon.")
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
