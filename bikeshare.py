"""
This script was written by Robert Buelteman III 
03/2021
For Udacity's Data Science with Python Nanodegree
robbuelteman3@gmail.com
Certain sections were completed with help from the student community & Github
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\nPlease note all data entries default to lower case.')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    
    # while loop accounts for invalid data entered by user, and terminates when the user enters a valid city name from the list.
    # use input().lower() method to standardize input to lower case letters
    # print answer string after formatting city variable as a string
    while city not in CITY_DATA.keys():
        print('Choose Chiacgo, New York, or Washington, please.')
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('Please enter data properly-\nThe block loop will now restart.')    
    print("\nYou have chosen " + str(city.title()) + " as your city.")
    
    # get user input for month (all, january, february, ... , june)
    # use input().lower() method to standardize input to lower case letters
    # create empty object to store user data
    # create while loop to account for mistakes made in data entry
    # print answer string after formatting city variable as a string
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print('Enter the month you want to analyze, by name, between January and June or choose all.')
        month = input().lower()
        if month not in MONTH_DATA.keys():
            print('Please enter data properly-\nThis block loop will now restart.')
    print("\nWe will analyze " + str(month.title()))
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # use input().lower() method to standardize input to lower case letters
    # same methods as above but without a dict object as the names are not keys to values
    # while loop asks user for data entry, if condition handles bad data input
    DAY_LIST = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in DAY_LIST:  
        print('Enter the day of the week to analyze, or "all" for all days.')
        day = input().lower()
        if day not in DAY_LIST:
            print('Please enter data properly-\nThe block loop will now restart.')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data for city
    # create DataFrame object using Pandas Package in Python
    # tell Pandas to read the CSV data for the city terurned above
    print("\nLoading target city data for human user...")
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    # tell Pandas how to convert a column called "start time" to a Datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    # crete a new DF column from "start time" called "month" in datetime format using month
    # crete a new DF column from "start time" called "day_of_week" in datetime format using weekday name
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    # use the index of the months list to get the corresponding integer value for their order
    # filter by month to create the new dataframe called 'month'
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    # filter by day of week to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    # returns the selected file as a dataframe (df) with relevant columns
    return df

def display_data(df):
    """
    User can look at DF created by Pandas
    Arguments:
    parameter 1, (df) the Pandas DataFrame you wish to analyze
    Returns:
    none
    """

    # set index to 0, and user_input is created a variable for input()
    # while loop sets conditions for accepted responses
    # print DataFrame iloc (index location)
    # Iterate index by 5 values, and ask again
    index = 0
    user_input = input('would you like to display 5 rows of raw data?\n ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display 5 more rows of raw data?\n ').lower()

    
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Arguments: 
    parameter 1, (df) the Pandas DataFrame you wish to analyze 
    Returns: 
    none.
    """
    
    # display the most common month
    # use time() method on start_time
    # assign freq_traveled variable to mode() method on DF 'month' column
    # print answer string after formatting variable as a string
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    freq_traveled = df['month'].mode()[0]
    print('Most frequently traveled month, by number, was ' + str(freq_traveled))
    
    # display the most common day of week
    # Assign popular_day variable to mode() method on 'day_of_week' column
    # print answer string after formatting variable as a string
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day: ' + str(popular_day))
    
    # display the most common start hour
    # create a DF object with a column called 'hour' in datetime format
    # Use mode() method to find most popular hour
    # print answer string after formatting variable as a string
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ' + str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Arguments:
    parameter 1, (df) the Pandas DataFrame you wish to analyze
    Returns:
    none.

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station.
    # assign common_start_station to the mode() method of DF column 'Start Station'.
    # print answer string after formatting variable as a string
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: ' + str(common_start_station))

    # display most commonly used end station.
    # assigns common_end_station to the mode() method of DF column 'End Station'.
    # print answer string after formatting variable as a string
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: ' + str(common_end_station))

    # display most frequent combination of start station and end station trip.
    # concatenate the 'Start Station' and 'End Station' columns into a new DF object 
    # with a column called 'Start to End' using ' to ' to separate the two data sets.
    # assign start_end to the mode() method of DF column 'Start to End'.
    # print answer string after formatting variable as a string
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    start_end = df['Start To End'].mode()[0]
    print('The most frequent combination of trips are from ' + str(start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Arguments:
    parameter 1, (df) the Pandas DataFrame you wish to analyze
    Returns: 
    none
    
    This section completed after consulting other students' projects to help me figure out how
    to forulate the code. This was the hardest part of the project for me.
    """
    # get trip duration
    # assign start_time variable to time() method of time object
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time, using sum() 
    # assign total_duration variable to the sum() of the 'Trip Duration' DataFrame column
    # divmod() is used to return a tuple of the two numbers quotient and remainder
    # use formatted string to print results
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")
   
    # display mean travel time
    # assign average_duration variable to the mean() of the 'Trip Duration' column, rounded to the closest whole number
    # account for variation in the data using an if/ else statement
    # print formatted strings to show results
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"The average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"The average trip duration is {mins} minutes and {sec} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Arguments:
    parameter 1, (df) the Pandas DataFrame you wish to analyze
    Returns:
    none.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Use value_counts() method on the DF column called 'User Type'
    # Print formatted string to show result
    user_type = df['User Type'].value_counts()
    print(f"The types of users by number are given below:\n{user_type}")
    
    # Display counts of gender
    # Use "Try" loop to handle errors encountered from holes in data
    # Print formatted string to show result
    try:
        gender = df['Gender'].value_counts()
        print(f"The types of users by gender are given below:\n{gender}")
    except:
        print("There is no 'Gender' column in this file.")


    # Display earliest, most recent, and most common year of birth
    # Use try loop to call min(), max(), and mode() on age data
    # Print formatted string to show result
    # int(df) is used to make sure the results from the DF object are all integers
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"The earliest year of birth: {earliest}\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
"""
This function runs the script itself. Called by bottom text.
Arguments: 
none
Returns: 
none
"""

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Restart option
        restart = input('Would you like to analyze more data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
