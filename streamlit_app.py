streamlit.header("Fruityvice Fruit Advice!")

import requests

import snowflake.connector
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
