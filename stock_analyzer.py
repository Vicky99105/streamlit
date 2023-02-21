import pandas as pd
import  streamlit as st
import datetime 
import yfinance as yf


st.write(
    """
    # Stock Prize Analyzer

    Shown are the prices of the stock
    """
)

#stock name
ticker_symbol = st.text_input(
    "Enter the stock symbol",
    "AAPL",
    key = "placeholder"
)


#start and end date
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Input the starting date",
    datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Input the starting date",
    datetime.date(2020, 1, 1))


ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period = "1d",
                    start = start_date,
                    end = end_date
)

st.write("""
  ## {} stock price info: """.format(ticker_symbol))

st.dataframe(ticker_df)


#showing line chart

st.write("""
## Showing the line chart using streamlit""")

st.line_chart(ticker_df.Close)


col1, col2 = st.columns(2)

with col1:
   st.header("Opening Prices")
   st.line_chart(ticker_df.Open)

with col2:
   st.header("Closing Prices")
   st.line_chart(ticker_df.Close)