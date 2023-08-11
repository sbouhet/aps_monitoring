import requests
from datetime import datetime
import urllib.parse
import json

class apsMonitoring:

    def get_session(self):
        session = requests.Session()
        return session

    def get_power_values(self, user_name, pwd):
        session = self.get_session()
        self.step_home(session)
        self.step_login(session,user_name, pwd)
        power_data = self.step_dashboard(session)
        return power_data

    def step_login(self, session,user_name,pwd):
        # Define the URL and payload for the first POST request
        url = "https://www.apsema.com/ema/loginEMA.action"

        # Define the headers for the first request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Get the current date and time
        now = datetime.now()

        # Format the date and time as a string
        formatted_date = urllib.parse.quote(now.strftime("%Y-%m-%d %H:%M:%S"))

        payload = {
            "today": formatted_date,
            "code": "",
            "username": user_name,
            "password": pwd,
            "verifyCode": "+"
        }

        response = session.post(url, data=payload,  headers=headers)


    def step_dashboard(self, session):
        # Define the URL and payload for the first POST request
        url = "https://www.apsema.com/ema/ajax/getDashboardApiAjax/getDashboardProductionInfoAjax"

        # Define the headers for the first request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json;charset=utf-8"
        }

        response = session.post(url, headers=headers)

        data_dict = json.loads(response.text)

        return data_dict

    def step_home(self, session):
        # Define the URL and payload for the first POST request
        url = "https://www.apsema.com/ema/index.action"

        # Define the headers for the first request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        response = session.get(url, headers=headers)




