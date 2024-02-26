#Streamlit app for QR Code generator
#To run, go to command line and run:
# streamlit run this_filename.py
#Must first run pip install streamlit if needed

import streamlit as st
import qrcode

#Add title
st.title('QR Code Generator :rocket:')

#Add App description
with st.expander("App Description"):
    st.write("""
    This app allows you to generate QR Codes for any url or any text string you want to encode.  QR Codes are generated using the [qrcode](https://pypi.org/project/qrcode/) python package.
    
    POC: Your Name, first.last@nps.edu
    """)

#Add text input
text = st.text_input(label='Enter Text or URL to encode as QR Code')

# Encoding data using qrcode.make() function
if text:
    #Create the qrcode image object
    qr_img = qrcode.make(text)
    
    #Extract the actual image
    img = qr_img._img
    
    #Display the QR Code in the app
    st.write(f'QR Code generated for {text}:')
    st.image(img)
    

