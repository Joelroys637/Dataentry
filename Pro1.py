import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets
def authenticate_gspread():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('python.json', scope)
    gc = gspread.authorize(credentials)
    return gc

# Main function to run the app
def main():
    st.title("Mini Data Entry Website")

    # Authenticate with Google Sheets
    gc = authenticate_gspread()
    
    # Open the Google Sheet
    sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1oBWVyRBqCCBv3T8-0maFLO4nV4JRzuiZ0l1a8h6n4IQ/edit?usp=sharing").sheet1

    # Data Entry Form
    st.subheader("Data Entry")
    name = st.text_input("Enter Name:")
    email = st.text_input("Enter Email:")
    age = st.number_input("Enter Age:")
    submit_button = st.button("Submit")

    if submit_button:
        # Add data to Google Sheet
        sheet.append_row([name, email, age])
        st.success("Data submitted successfully!")

if __name__ == "__main__":
    main()
