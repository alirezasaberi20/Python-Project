# Currency Converter Application

This project is a web-based currency converter application built using Streamlit. It uses the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch real-time currency exchange rates and convert from one currency to another.

<img src='https://ps.w.org/currency-converter-calculator/assets/icon.svg?rev=1838182' width=200>

## Features

- Convert between any two supported currencies.
- Real-time exchange rates fetched from ExchangeRate-API.
- Select base and target currencies from a list of available currencies.
- Caching is implemented using `cachetools` to optimize API requests.
- Displays the conversion result, along with visual elements for clarity.

## How it Works

1. **API Status Check**: The application checks if the ExchangeRate API is working before proceeding with any conversions.
2. **Currency Conversion**: Users input the base currency, target currency, and amount to be converted. The app fetches the conversion rate from the API and returns the converted amount.
3. **Caching**: The app caches exchange rates for 6 hours to avoid making too many requests to the API.
   
## Libraries Used

- `os`: For reading environment variables (API key).
- `requests`: For making HTTP requests to the ExchangeRate API.
- `cachetools`: For implementing a time-to-live (TTL) cache to reduce API calls.
- `streamlit`: For building the web interface.
   
## Requirements

To run this application, you'll need the following:
   
- Python 3.8 or higher
- Streamlit
- Requests
- Cachetools
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/)
   
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alirezasaberi20/Python-Project.git
   cd currency-converter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   - Get an API key from [ExchangeRate-API](https://www.exchangerate-api.com/).
   - Add it to your environment variables:
     ```bash
     export EXCHANGE_RATE_API_KEY='your_api_key_here'
     ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Use

1. Open the app in your browser.
2. Select the base currency from the dropdown.
3. Select the target currency.
4. Enter the amount you want to convert.
5. The app will display the converted amount, the original amount, and provide a visual arrow for direction.

## Example Usage

- Convert USD to EUR
- Convert GBP to JPY

## Troubleshooting

If the API is not working, the app will notify you and halt further operations. Ensure that your API key is valid and the ExchangeRate API is functioning.

## License

This project is licensed under the MIT License.

