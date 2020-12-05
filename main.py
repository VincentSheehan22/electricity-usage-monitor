

import pandas as pd


# Get input from user, and return as data frame.
def get_entry():
    date = input("Input date (yyyy-mm-dd): ")
    reading = input("Input reading (kWh): ")

    df_entry = pd.DataFrame([[date, reading]], columns=["Date", "Reading"])

    return df_entry


# Add entry as new row in main data frame.
def add_to_df(df_log, df_entry):
    df_out = df_log.append(df_entry)

    return df_out


# Launch menu.
def run_menu():
    option = input("""Select option: 
    1 - Add new entry.
    2 - Display trend.
    3 - Display data frame.
    4 - Exit.
    """)

    return option


if __name__ == '__main__':
    # To do: load CSV as data frame. If not present create empty data frame
    run_menu()
    df_log = pd.DataFrame([], columns=["Date", "Reading"])
    df_entry = get_entry()
    print(add_to_df(df_log, df_entry))
    # Write data frame to CSV - to persist over separate runs.
