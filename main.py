import psycopg2
import json
#Establishing the connection
conn = psycopg2.connect(
   database="carbonemissiondata", user='postgres', password='1234', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
insert_stmt = (
  "INSERT INTO month (average, date, interpolated, num_days,trend) "
  "VALUES (%s, %s, %s, %s, %s)"
)
list = []
with open('../data/emissions_data.json') as data_file:    
    data = json.load(data_file)
    for v in data:
        data = (v['Average'], v['Date'], v['Interpolated'], v['Number of Days'],v['Trend'])
        list.append(data)
print(list)
# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()