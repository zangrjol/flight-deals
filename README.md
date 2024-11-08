
# Flight Deals Finder

A Python program that tracks flight prices for specified destinations and notifies you when prices drop. The tool integrates with Google Sheets to manage target destinations and uses the Amadeus API to search for flight deals.

## Features
- **Data Management**: Syncs with Google Sheets to manage destinations and target prices.
- **Flight Search**: Finds flight deals using the Amadeus Flight Search API.
- **Notifications**: Alerts users via SMS, WhatsApp, or email when flight prices drop.

## Prerequisites

- **Python 3.x**
- **Google Sheets** (for storing target destinations and prices)
- **APIs**:
  - **Amadeus API**: for flight search
  - **Sheety API**: for managing Google Sheets
  - **Twilio API** (optional): for SMS and WhatsApp notifications

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/zangrjol/flight-deals-finder.git
   ```
2. Navigate to the project directory:
   ```
   cd flight-deals-finder
   ```
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file:
   ```
   SHEETY_BEARER=your_sheety_bearer_token
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_API_SECRET=your_amadeus_api_secret
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   MY_EMAIL=your_email_address
   MY_EMAIL_PASSWORD=your_email_password
   EMAIL_PROVIDER_SMTP_ADDRESS=smtp_provider_address
   ```

## Usage

1. **Run the main program** to retrieve and update destination data and search for flight deals:
   ```
   python main.py
   ```
2. The program will automatically notify you of low-price flights via your selected notification method.

## Code Overview

- **main.py**: Orchestrates the data retrieval, flight search, and notification processes.
- **DataManager**: Manages data retrieval and updates from Google Sheets via Sheety.
- **FlightSearch**: Interacts with the Amadeus API to find flight deals.
- **FlightData**: Processes and structures the flight data for easier analysis.
- **NotificationManager**: Sends notifications using Twilio (SMS/WhatsApp) and SMTP (email).

## License

This project is licensed under the MIT License. 
