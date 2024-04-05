# Ilya Belyaev Submisison

> An awesome project.

# Stock Data Analysis and Reporting Automation

## Features

- **Load Stock Data from CSV File:** The script reads the stock data from a CSV file located in the `data` subdirectory.
- **Calculate Daily Percentage Change:** It calculates the daily percentage change in the closing price for each stock.
- **Identify Top Performers:** It identifies the stock with the largest absolute percentage change for each day and stores the relevant information (date, symbol, and absolute percentage change) in a DataFrame.
- **Generate Top Performer Report:** The script generates a CSV report named `top_performers_report.csv` that contains the information about the top-performing stocks for each day.
- **Calculate Average Percentage Change:** It calculates the average percentage change for each stock over the entire dataset.
- **Store Data in MySQL Database:** It stores the "top_performers" and "average_pct_change" data in a MySQL database named "stock_analysis". It creates the necessary tables and inserts the data.
- **Count Top Performer Days:** The script counts the number of days each stock was the top performer and prints the results.
- **Save Data to CSV Files:** It saves the "top_performers" and "avg_pct_change" DataFrames to CSV files in the `data` subdirectory.

## Requirements

- Python 3.x
- Libraries: pandas, numpy, os, datetime, mysql.connector
- A MySQL database with the necessary permissions

## Usage

1. Ensure you have the required Python libraries installed.
2. Update the MySQL database connection details in the `db_config` dictionary with your own credentials.
3. Place the `stocks.csv` file in the `data` subdirectory.
4. Run the script.

The script will perform the stock data analysis, generate the reports, store the data in the MySQL database, and save the DataFrames to CSV files in the `data` subdirectory.

## Output

- **top_performers_report.csv:** A CSV file containing the top-performing stocks for each day, including the date, stock symbol, and absolute percentage change.
- **top_performers.csv:** A CSV file containing the "top_performers" DataFrame, which includes the date, stock symbol, and absolute percentage change.
- **avg_pct_change.csv:** A CSV file containing the "avg_pct_change" DataFrame, which includes the stock symbol and the average percentage change.

**Console output:**

- The "Top Performers Report"
- The "Average Percentage Change per Stock"
- The count of the number of days each stock was the top performer
