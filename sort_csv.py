#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 04 2024
Stock Data Analysis and Reporting Automation
@author: Ilya
"""

import pandas as pd
import numpy as np
import os
import datetime
import mysql.connector

# Load data from CSV file
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'data', 'stocks.csv')
df = pd.read_csv(file_path)

df.columns #column labels of the df

datetime.datetime(2024, 2, 22) #(year, month, day)

df['Date-py'] = np.empty(len(df), dtype = str)

for i in range(len(df)):
    year = int(df['Date'][i].split('/')[2])
    month = int(df['Date'][i].split('/')[0])
    day = int(df['Date'][i].split('/')[1])
    try: 
        df.loc[i,'Date-py'] = datetime.date(year,month, day)
    except: df.loc[i,'Date-py']  = np.nan #some rows have wrong date formats

# Calculate daily percentage change in closing price
df = df.sort_values(['Symbol', 'Date-py'])
df['Daily_Pct_Change'] = df.groupby('Symbol')['Close'].pct_change()
df['Daily_Pct_Change'].fillna(0, inplace=True)

# Identify the stock with the largest absolute percentage change for each day
df['Abs_Pct_Change'] = abs(df['Daily_Pct_Change'])
df['Top_Performer'] = df.groupby('Date-py')['Abs_Pct_Change'].rank(method='dense', ascending=False).astype(int)
top_performers = df[df['Top_Performer'] == 1][['Date-py', 'Symbol', 'Abs_Pct_Change']]

# Calculate average percentage change for each stock
avg_pct_change = df.groupby('Symbol')['Daily_Pct_Change'].mean().reset_index()

# Store data in MySQL database
db_config = {
    'host': '127.0.0.1', #replace with your IP address
    'user': 'root', #replace with your username
    'password': 'Ahuntsic@2023!', #replace with your password
}

# Create MySQL connection without a database
conn = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
)
cursor = conn.cursor()

# Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS stock_analysis")
cursor.execute("USE stock_analysis")

# Create tables
# Insert data into top_performers table
for index, row in top_performers.iterrows():
    cursor.execute("""
        INSERT INTO top_performers (date, symbol, abs_pct_change)
        VALUES (%s, %s, %s)
    """, (row['Date-py'], row['Symbol'], row['Abs_Pct_Change']))
conn.commit()

# Insert data into avg_pct_change table
for index, row in avg_pct_change.iterrows():
    cursor.execute("""
        INSERT INTO avg_pct_change (symbol, avg_pct_change)
        VALUES (%s, %s)
    """, (row['Symbol'], row['Daily_Pct_Change']))
conn.commit()

# Count the number of days the symbol was Top performing asset
cursor.execute("""
    SELECT symbol, COUNT(*) as top_performer_days
    FROM top_performers
    GROUP BY symbol
""")
top_performer_counts = cursor.fetchall()

# Print results
print("Top Performers Report:")
print(top_performers)
print("\nAverage Percentage Change per Stock:")
print(avg_pct_change)
print("\nTop Performer Counts:")
for row in top_performer_counts:
    print(f"Symbol: {row[0]}, Top Performer Days: {row[1]}")

# Close database connection
conn.close()

# Save the files to data folder
top_performers.to_csv('data/top_performers.csv', index=False)
avg_pct_change.to_csv('data/avg_pct_change.csv', index=False)

