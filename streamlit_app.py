import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena\'s Amazing Atheleisure Catalog")

#Snowflake Connection 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#Run a snowflake query and put in in a variable called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#Put to data into a Data Frame 
df = pandas.DataFrame(my_catalog)

#Temp:Write the dataframe to the screen to check the data frame is working 
streamlit.text(df)

#streamlit.text("Hello from Snowflake")
#streamlit.text(my_data_row)


