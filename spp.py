import requests
import spacy
import os
import pandas as pd
import requests
import spacy

# Commented out IPython magic to ensure Python compatibility.
# %%writefile spp.py
# 
# import streamlit as st
# from streamlit_option_menu import option_menu
# from datetime import date
# import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
# from plotly import graph_objs as go
# import pandas as pd
# from smartapi import SmartConnect
# from spacy import displacy
# from bs4 import BeautifulSoup
# import matplotlib
# import spacy
# import streamlit as st
# import os
# 
# from spacy import displacy
# from bs4 import BeautifulSoup
# import matplotlib
# from PIL import Image
# 
# 
# hide_streamlit_style = """
#             <style>
#             footer {visibility: hidden;}
#             </style>
#             """
#             #MainMenu {visibility: hidden;}
# 
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 
# 
# #with st.sidebar:
#   #horizontal menu
# selected2 = option_menu(None, ["Home","Auto-Trade", "Prediction", "Compare", "Alert"], 
#     icons=['house',"robot", "graph-up-arrow", 'sliders',"bell-fill"], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2
# 
# 
# #HOME
# 
# 
# if selected2 == "Home":
# 
#   #opening the image
# 
#   image = Image.open('/content/Landing Page.png')
# 
# 
# 
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.2, 5, 0.2])
#   col2.image(image, use_column_width=True)
# 
#   st.title('An introduction to stock markets')
#   st.write('The stock market is a system of trade where shares of companies that are publicly-traded are issued, and can be bought and sold. The stock market can also be viewed as a group of traders who pit their expertise against each other. To begin trading in stocks, you need to create two accounts- a trading account and a DEMAT account. A DEMAT account is where your shares will be stored in a digital format. Your trading account will be used to buy and sell shares.')
# 
# 
#   image = Image.open('/content/bullsbear.jpg')
# 
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.1, 2.5, 0.1])
#   col2.image(image, use_column_width=True)
#   st.title('Why do Stock Prices Go Up and Down?')
#   st.write('To know how to understand share market, you need to understand why the stock prices go up and down. Stock prices are influenced by multiple factors that determine whether they will go up or down. Factors like media, opinions of famous investors, political upheaval, natural calamities, risk factors, and supply and demand. The complex interaction of these factors, along with all relevant information about the stocks, is responsible for the creation of a specific kind of sentiment, and a resultant number of sellers and buyers. If the number of sellers is more than the buyers, the prices tend to fall. When the opposite happens, prices generally rise.')
#   st.write("##")
# 
# 
#   #Chart analysis
# 
#   image = Image.open('/content/Chart analysis.png')
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.1, 2.5, 0.1])
#   col2.image(image, use_column_width=True)
#   st.title('Why is it so difficult to predict the Stock Market?')
#   st.write('Let’s imagine a scenario where there has been an increase in the stock prices for years. Investors know that a correction is round the corner which will upset the stock prices. What is unknown is the ‘what’ and the ‘when’- what will trigger it, and when will it happen. In that scenario, what can we do? Some will sit back with cash in hand, waiting for a suitable time to enter the trade. Some will be willing to take the risk and jump in. Now, the questions are- if you are waiting, how will you identify the right time to begin the trade? And how will you know when to exit it? In a world where the stock market was predictable, understanding the stock market would have been easier.')
# 
# #Auto-Trade
# 
# if selected2 == "Auto-Trade":
# 
#   #opening the image
# 
#   image = Image.open('/content/auto Trade.png')
# 
# 
# 
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.2, 5, 0.2])
#   col2.image(image, use_column_width=True)
# 
# 
# 
#   obj = SmartConnect(api_key = 'B94qZLC7')
#   data = obj.generateSession('P714176', 'P@ssw0rd@123')
# 
#   def place_order(orderparams):
#       try:
#           orderID = obj.placeOrder(orderparams)
#           placeholder1.success(f"The Order ID for Symbol {orderparams['tradingsymbol']} is: {orderID}")
#       except Exception as e:
#           placeholder1.error(f"Order placement for Symbol {orderparams['tradingsymbol']} failed: {e}")
# 
#   def generate_trade_list(uploaded_file):
# 
#       try:
#           df = pd.read_csv(uploaded_file)
#       except Exception as e:
#           df = pd.read_excel(uploaded_file)
#       trade_list = [] #empty list
# 
#     #looping over each row in the dataframe and storing
#     #the value in each column to generate orderparams dict
#     #we use str to convert to strings
#       for index, rows in df.iterrows():
#           new_dict = {"variety": str(rows['variety']), 
#                       "tradingsymbol" : str(rows['tradingsymbol']),
#                       "symboltoken" : str(rows['symboltoken']),
#                       "transactiontype": str(rows['transactiontype']), 
#                       "exchange": str(rows['exchange']),
#                       "ordertype": str(rows['ordertype']), 
#                       "producttype": str(rows['producttype']),
#                       "duration": str(rows['duration']), 
#                       "price": str(rows['price']), 
#                       "quantity": str(rows['quantity']),
#                       "triggerprice": str(rows['triggerprice'])}
# 
#           trade_list.append(new_dict)
# 
#       return trade_list
# 
#   if __name__ == '__main__':
# 
#       st.title("Trade Hassle-free")
# 
#       with st.form(key = 'angel_broking_execution'):
# 
#           uploaded_file = st.file_uploader("Upload your trades file", type = ['xlsx', 'csv'])
#           submitbutton = st.form_submit_button("Submit")
# 
#           if submitbutton:
#               trade_list = generate_trade_list(uploaded_file)
#               placeholder1 = st.empty()
#               for trade in trade_list:
#                   place_order(trade)
# 
#   #opening the image
# 
#   image = Image.open('/content/tableg.png')
# 
# 
# 
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.2, 5, 0.2])
#   col2.image(image, use_column_width=True)                 
# 
# 
# 
# #Prediction
# 
# if selected2 == "Prediction":
# 
#   START = "2015-01-01"
#   TODAY = date.today().strftime("%Y-%m-%d")
#   st.title('Stock Forecast App')
#   stocks = ('AAPL', 'ABBOTINDIA.NS', 'ADANIENT.NS', 'ADANIPORTS.NS',
#             'ADANIPOWER.NS', 'ADBE', 'ADSK', 'AEP', 'ALGN',
#             'AMA', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'APOLLOHOSP.NS',
#             'ARGU', 'ASIANPAINT.NS', 'ASML', 'AVGO', 'AXISBANK.NS',
#             'BAJAJ-AUTO.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS',
#             'BIIB', 'BOSCHLTD.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CANBK.NS',
#             'CDNS', 'CIPLA.NS', 'CMCSA', 'COALINDIA.NS', 'COST', 'CPRT',
#             'CRWD', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DIS', 'DMLP', 'DO',
#             'DOCU', 'DRREDDY.NS', 'DXCM', 'EA', 'EICHERMOT.NS', 'EXC',
#             'FAST', 'FB', 'GAIL.NS', 'GILD', 'GOOGL', 'GRASIM.NS', 
#             'HCLTECH.NS', 'HDFCBANK.NS', 'HDIL.NS', 'HEROMOTOCO.NS',
#             'HINDUNILVR.NS', 'HON', 'ICICIBANK.NS', 'IDXX', 'ILMN',
#             'INFY.NS', 'INTC', 'INTU', 'IOC.NS', 'ITC.NS', 'JD', 'JINDALSTEL.NS',
#             'JSWSTEEL.NS', 'KO', 'KOTAKBANK.NS', 'LT.NS', 'LTI.NS', 'M&M.NS',
#             'MARUTI.NS', 'MCHP', 'MELI', 'MRVL', 'MSFT', 'MUTHOOTFIN.NS',
#             'NESTLEIND.NS', 'NFLX', 'NTPC.NS', 'NVDA', 'OLPX', 'ONGC.NS',
#             'PEP', 'PNB.NS', 'POWERGRID.NS', 'PYPL', 'RELIANCE.NS', 'SBIN.NS',
#             'SHREECEM.NS', 'SIDU', 'SNPS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 
#             'TATASTEEL.NS', 'TCS.NS', 'TEAM', 'TECHM.NS', 'TSLA', 'TXN', 
#             'ULTRACEMCO.NS', 'UPL.NS', 'VTNR','WIPRO.NS')
#   
#   selected_stock = st.selectbox('Select the Stock of a Company', stocks)
#   n_years = st.slider('Years of prediction:', 1, 4)
#   period = n_years * 365
# 
#   @st.cache
#   def load_data(ticker):
#       data = yf.download(ticker, START, TODAY)
#       data.reset_index(inplace=True)
# 
#       return data
# 
#   
# 
#   data_load_state = st.text('Loading data...')
#   data = load_data(selected_stock)
#   data_load_state.text('Loading data... done!')
# 
#   st.subheader('Collected Data of the selected company')
#   st.write(data.tail())
# 
# #Plot raw data
# 
#   def plot_raw_data():
# 	  fig = go.Figure()
# 	  fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="open"))
# 	  fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="close"))
# 	  fig.layout.update(title_text='Opening & Closing Price Of Collected Data', xaxis_rangeslider_visible=True)
# 	  st.plotly_chart(fig)
# 	
#   plot_raw_data()
# 
# # Predict forecast with Prophet.
#   df_train = data[['Date','Close']]
#   df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
# 
#   m = Prophet()
#   m.fit(df_train)
#   future = m.make_future_dataframe(periods=period)
#   forecast = m.predict(future)
# 
# # Show and plot forecast
#   st.subheader('Forecasted data')
#   st.write(forecast.tail())
#     
#   st.write(f'Predictions of {n_years} year')
#   fig1 = plot_plotly(m, forecast)
#   st.plotly_chart(fig1)
# 
#   st.write("Trend, Weekly, Yearly Charts")
#   fig2 = m.plot_components(forecast)
#   st.write(fig2)
# 
# 
# 
#  #Compare
# 
# if selected2 == "Compare":
#   st.title('Compare Assets')
# 
#   tickers = ('AAPL', 'ABBOTINDIA.NS', 'ADANIENT.NS', 'ADANIPORTS.NS',
#             'ADANIPOWER.NS', 'ADBE', 'ADSK', 'AEP', 'ALGN',
#             'AMA', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'APOLLOHOSP.NS',
#             'ARGU', 'ASIANPAINT.NS', 'ASML', 'AVGO', 'AXISBANK.NS',
#             'BAJAJ-AUTO.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS',
#             'BIIB', 'BOSCHLTD.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CANBK.NS',
#             'CDNS', 'CIPLA.NS', 'CMCSA', 'COALINDIA.NS', 'COST', 'CPRT',
#             'CRWD', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DIS', 'DMLP', 'DO',
#             'DOCU', 'DRREDDY.NS', 'DXCM', 'EA', 'EICHERMOT.NS', 'EXC',
#             'FAST', 'FB', 'GAIL.NS', 'GILD', 'GOOGL', 'GRASIM.NS', 
#             'HCLTECH.NS', 'HDFCBANK.NS', 'HDIL.NS', 'HEROMOTOCO.NS',
#             'HINDUNILVR.NS', 'HON', 'ICICIBANK.NS', 'IDXX', 'ILMN',
#             'INFY.NS', 'INTC', 'INTU', 'IOC.NS', 'ITC.NS', 'JD', 'JINDALSTEL.NS',
#             'JSWSTEEL.NS', 'KO', 'KOTAKBANK.NS', 'LT.NS', 'LTI.NS', 'M&M.NS',
#             'MARUTI.NS', 'MCHP', 'MELI', 'MRVL', 'MSFT', 'MUTHOOTFIN.NS',
#             'NESTLEIND.NS', 'NFLX', 'NTPC.NS', 'NVDA', 'OLPX', 'ONGC.NS',
#             'PEP', 'PNB.NS', 'POWERGRID.NS', 'PYPL', 'RELIANCE.NS', 'SBIN.NS',
#             'SHREECEM.NS', 'SIDU', 'SNPS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 
#             'TATASTEEL.NS', 'TCS.NS', 'TEAM', 'TECHM.NS', 'TSLA', 'TXN', 
#             'ULTRACEMCO.NS', 'UPL.NS', 'VTNR','WIPRO.NS')
# 
#   dropdown = st.multiselect('Pick your assets', tickers)
# 
#   start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
#   end = st.date_input('End', value = pd.to_datetime('today'))
# 
#   def relativeret(df):
#     rel = df.pct_change()
#     cumret = (1+rel).cumprod() - 1
#     cumret = cumret.fillna(0)
#     return cumret
# 
# 
#   if len(dropdown) > 0:
#     df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
#     st.line_chart(df)
# 
# if selected2 == "Alert":
# 
#     #opening the image
# 
#   image = Image.open('/content/Alert.png')
# 
# 
# 
#   #displaying the image on streamlit app
#   col1, col2, col3 = st.columns([0.2, 5, 0.2])
#   col2.image(image, use_column_width=True)
# 
#  
#   st.title("STOCK ALERTS SO YOU CATCH THE ACTION LIVE!")
#   st.write('Never again settle for setting limit orders before going to bed and hoping for the best. Stop checking your phone during work to find yet another lost opportunity. We have made a Bot for keeping you Updated, Join our '"  ""[Telegram Channel](https://t.me/sppalert)"" " 'to get real-time price alerts! Or Follow us on'" ""[Twitter](https://twitter.com/sppalert)"" "'to get real-time updates')
#   st.write("")
#

