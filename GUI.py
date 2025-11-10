import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('Home')
st.write('Invoice Upload')
invoice = st.file_uploader('Upload Invoice', type="pdf")


if invoice is not None:
    st.write('File Uploaded...')
    link = 'https://olukaa.app.n8n.cloud/webhook-test/upload-invoice'
    files = {'file' : (invoice.name, invoice.getvalue(), invoice.type or 'application/pdf' )} # I am using get value instead of seek because i dont want to reset my cursor instead just get all of the bytes at once instead of chunks 
    resp = requests.post(link, files=files, auth=('Femi','NEA'), timeout=60)