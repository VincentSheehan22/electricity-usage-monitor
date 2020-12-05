

import pandas as pd
import matplotlib.pyplot as plt


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

def menu_option_1():
    df_entry = get_entry()
    add_to_df(df_log, df_entry)


#def menu_option_2():


#def menu_option_3():


#def menu_option_4():



if __name__ == '__main__':
    # To do: load CSV as data frame. If not present create empty data frame
    #run_menu()
    #df_log = pd.DataFrame([], columns=["Date", "Reading"])
    #df_entry = get_entry()
    #print(add_to_df(df_log, df_entry))
    # Write data frame to CSV - to persist over separate runs.

    df_readings = pd.read_csv("Meter Readings.csv")

    plt.plot(df_readings["Date"], df_readings["Reading"])
    plt.show()

