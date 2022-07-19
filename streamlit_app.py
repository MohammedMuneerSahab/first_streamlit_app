import Streamlit 
Streamlit.title("My parents new healthy Diner")
Streamlit.header('Breakfast Menu')
Streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
Streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
Streamlit.text('🐔 Hard-Boiled Free-Range Egg')
Streamlit.text('🥑🍞 Avocado Free-Range Egg')
Streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
Streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
Streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
Streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')


