import streamlit as st
from ExchangeRate import Currency_Converter , check_API_status
from Currencies import Currency_list

st.title(':dollar: Currency Converter')
st.markdown('This app converts one currency to another using the latest exchange rates.')

base_currency = st.selectbox('Base Currency', Currency_list)
target_currency = st.selectbox('Target Currency', Currency_list)
amount = st.number_input('Enter Amount', min_value=0.0)
if check_API_status() != 'API is working':
    st.write('API is not working. Please try again later')
    st.stop()
else:
    result = Currency_Converter(amount, base_currency, target_currency)
    st.write(f'{amount} {base_currency} is equal to {result:.4f} {target_currency}')

    col1, col2, col3 = st.columns(3)
    col1.metric(label=base_currency, value=f"{amount:.2f}")
    col3.metric(label=target_currency, value=f"{result:.2f}")
    arrow_html = """
    <div style='text-align: center;'>
        <span style='font-size: 50px; color: green;'>&#x2192;</span>
    </div>
    """
