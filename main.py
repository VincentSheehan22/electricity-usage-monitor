import pandas as pd
import matplotlib.pyplot as plt


def get_entry():
    """Get input from user, and return as data frame."""
    date = input("Input date (yyyy-mm-dd): ")
    reading = input("Input reading (kWh): ")

    df_entry = pd.DataFrame([[date, reading]], columns=["Date", "Reading"])

    return df_entry


def add_to_df(df_log, df_entry):
    """Add entry as new row in main data frame."""
    df_out = df_log.append(df_entry)

    return df_out


def plot_trend():
    """Plot trend of meter readings."""
    df_readings = pd.read_csv("Meter Readings.csv", index_col=False)

    plt.plot(df_readings["Date"], df_readings["Reading"])
    plt.show()


def plot_delta_trend():
    """Plot trend of delta (n - (n-1)) in meter readings"""
    df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
    df_deltas = pd.DataFrame(columns=["Value"])

    df_deltas["Value"] = df_readings["Reading"].diff()

    plt.plot(df_deltas["Value"])
    plt.show()


def show_data_frame():
    """Print the meter readings data frame to screen."""
    df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
    print(df_readings)


def run_menu():
    """Launch menu."""
    option = input("""Select option: 
    1 - Add new entry.
    2 - Display trend.
    3 - Display delta trend.
    4 - Display data frame.
    5 - Exit.
    """)

    return option


if __name__ == '__main__':
    while True:
        menu_option = run_menu()

        if menu_option == '1':
            df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
            df_entry = get_entry()
            df_updated = add_to_df(df_readings, df_entry)
            csv = df_updated.to_csv("Meter Readings.csv", index=False)
        elif menu_option == '2':
            plot_trend()
        elif menu_option == '3':
            plot_delta_trend()
        elif menu_option == '4':
            show_data_frame()
        elif menu_option == '5':
            exit()
        else:
            print("Enter 1-5.")


