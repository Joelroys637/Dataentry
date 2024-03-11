import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets
def authenticate_gspread():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = {
        "type": "service_account",
        "project_id": "coherent-coder-416710",
        "private_key_id": "4c8820c55d5267e84d8d193d377adeb36cb46afd",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCzzzt2lKo4tNjW\netCpgRdygaEnwz0dKBoPaa5M379dS0ITrl16NapmFNlc6uRtQ1EIaNq+J/5iYzTB\n5AZKdCwVl5DafAJ9Z2qu4LG8NdStd2HAoHd2nkUwwOJFer1EqI9EYac6iFcQr36z\n/m5ip09GgqzrDp0O3KTrZWE0aw24PYSzUyNLOZJAzYZck3xrZqTt/U7JUeUFmPRf\nPaQ0Q4gsH6PwMR1W6k4g9m/XPCZxy5a2xGopPlDsMffDyiIx/11nh1Jia4RM2imk\nMZDTia/dGUGtyWngbINAiRKJzIwTkBR3qIeGzAbeKnsS1TwgNoiMyc6oQnayIAkM\noHlhcxbXAgMBAAECggEAKukRr8LavJ2sAcNdeJYuGk2FQA//za18SqFVz1K2QHVt\nV3UNKdUUzTe8h8gmq0ydUfxz911j/+bc+EiKl8oRmzWIhBuEHJlJhGJrCBdwodUT\npvykhdJPgMsHNL2N3Yy8Y/1KA1X2MS0wd5QIk9KJwLH+wjnCkYFmeia/g9roc0cU\nm/090H14oXvDSvN7xp9eDLOqUKCL9zgbIuS6r96TVuuhB9FVcE3iz6lpDGqGiMvS\nUpxY3vPmHEYX4m2n5dDJcVJ6pzhOHsL8xjSfWAWaOvXHyJ6UuHKH3kbl6oDTw8CS\nuBTkhf+ZHZFl7ljn5eawFsMv7fnve8ur7q15XWv9QQKBgQDgG3immU2MSPGxuSAf\nvEs5+uND6GgtOMGa9nEA8h3YYcuuDjqTujV9Cf7mSICDhW6roweRberfp8nmGKHK\ntTcu/IjtG2OWbG47i7HZ9b3Wbpgpo8ILSkMCpK0QiQfHO0QCtzTcGFzg+ZXzkoLL\nmnjTm+RB2w+ICqcTfoslxI8JHQKBgQDNZe7BFgrHAAlSXjM4HZMGtYdmE+9niK63\npEBNi1NVm/1n4WaKogVMOCh/5zGzoUrL8ALYi/nsWpk8nEUcor7D7JD9ikn4PJb0\nGYYKNAJJQCYsGaNeu8GGnn+fPx6gXewcWQK39HSpilEqZxGE1rBiF/75mVBOSDkP\n1jYxhPiRgwKBgEKcB61EzYbPu36+bmzgU1+lUV1Cu4wNXYYIj6ffTr2cu6Q9OG3m\nH7XNfcTGceQlibJcH4i7Kd9WCK1qTtRoLkG575zB0kTIb68lIzSMVONiNbnSoX8n\nkGk9tu6+O+CcnedMutpcJ2b65/Xgax3HCPikUiC80o311Jj3uLX+CSGFAoGACdtP\nZtKw97XHvL0qhhHdQWAqvDpOrdBAWi22rEH4YM5YjciiTBrUWEEFqIWmu/EMjtbY\nvB2Tg8UhP2hcZLBmqS5MEu60+AWoVNR4uzqdtXgvnMQqM9ycv+IRS8oSpS18rCuV\nVtCTXKN3m6pQi+hllH+ES+QQl4Edw+XKufuglhMCgYA+xXRz3Pp55b8bOknZ4jSP\nRim4tUEDz0UtCCxuoKogyD/CoplNPsd1yutvel+sy1kwknqd4Z2XqFI8LO8WQUst\nTIV3s+O2m90iIW95CvoEE+zcW7gBbvCunuOpB4khrE8TulofBLyg50XzzFm6aV1s\nZ2ZTDcD4kx1OLQHpeOXxuQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "gsheets-python-access@coherent-coder-416710.iam.gserviceaccount.com",
        "client_id": "102473486296138254558",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/g
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
