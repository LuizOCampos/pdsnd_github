import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print("Hello! Let\'s explore some US bikeshare data!\n")

    while True:
        city = input("Would you like to see data for Chicago, New York or Washington?\n").lower()
        try:
            if city in ['chicago', 'new york', 'washington']:
                break
            else:
                print("Oops!'{}' isn't a valid city.".format(city))
        except:
            continue


    print("\nAwesome! Looks like we\'re analysing {}'s data. Now Let's choose how we are going to filter this data\n".format(city.title()))
    print("We can filter this data by month, day, both or none. Here's a brief explanation about each option \n\n\
    Month:  Data will be filtered by a speficic month but using all days\n\
    Day:    Data will be filtered by a specific day of the week but using all months\n\
    Both:   Data will be filtered by month and day of the week\n\
    None:   No filter applied. We will look at all data for that city\n"
    )

    while True:
        filter = input("How would you like to filter the data: month, day, both or not at all? Type \"none\" for no time filter ?\n").lower()
        try:
            if filter in ['day', 'month', 'none', 'both']:
                break
            else:
                print("Oops!'{}' isn't a valid filter option.".format(filter))
        except:
            continue

    #sets to all, in case user selects "none"
    day     = "all"
    month   = "all"

    if filter == "month" or filter == "both":
        while True:
            month = input("Which month? January, February, March, April, May or June?\n").lower()
            try:
                if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                    break
                else:
                    print("Oops!'{}' isn't a valid month option.".format(month))
            except:
                continue

    if filter == "day" or filter == "both":
        while True:
            try:
                dayInput = input("Which day? Please use the weekday as numbers (e.g 0-Sunday to 6-Saturday)\n")
                day = int(dayInput)

                if day in [0,1,2,3,4,5,6]:
                    break
            except:
                print("Oops!'{}' isn't a valid day option.".format(dayInput))
                continue

        
    print("-"*40)
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

    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time']            = pd.to_datetime(df['Start Time'])
    df['month']                 = df['Start Time'].dt.month
    df['day_of_week']           = df['Start Time'].dt.weekday
    df['day_of_week_name']      = df['Start Time'].dt.day_name()
    df['hour']                  = df['Start Time'].dt.hour

    #adding month name based on the month_map dict
    month_map = {1: "January", 2:"February", 3: "March", 4: "April", 5:"May", 6:"June"}   
    df['month_name']    =      df['month'].map(month_map)


    if month != "all":
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]    

  
    #renaming Unnamed column to a blank
    df.rename( columns={'Unnamed: 0':''}, inplace=True )


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    most_common_month           = df['month_name'].mode()[0]
    most_common_month_count     = list(df['month_name'].value_counts(ascending=False).head(1))[0]
    print("Monst common month is {}. With a count of {}\n".format(most_common_month,most_common_month_count))


    # display the most common day of week
    most_common_dow             = df['day_of_week_name'].mode()[0]
    most_common_dow_count       = list(df['day_of_week_name'].value_counts(ascending=False).head(1))[0]
    print("Monst common day of week is {}. With a count of {}\n".format(most_common_dow,most_common_dow_count))


    # display the most common start hour
    most_common_hour            = df['hour'].mode()[0]
    most_common_hour_count      = list(df['hour'].value_counts(ascending=False).head(1))[0]
    print("Monst common start hour is {}. With a count of {}\n".format(most_common_hour,most_common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print("-"*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    most_common_startstation             = df['Start Station'].mode()[0]
    most_common_startstation_count       = list(df['Start Station'].value_counts(ascending=False).head(1))[0]
    print("Monst commonly used start station is \"{}\". With a count of {}\n".format(most_common_startstation,most_common_startstation_count))


    # display most commonly used end station
    most_common_endstation             = df['End Station'].mode()[0]
    most_common_endstation_count       = list(df['End Station'].value_counts(ascending=False).head(1))[0]
    print("Monst commonly used end station is \"{}\". With a count of {}\n".format(most_common_endstation,most_common_endstation_count))


    # display most frequent combination of start station and end station trip
    #creates a new column with a concat 
    df['Trip'] = 'From: "'+ df['Start Station'] + '" To: "' + df['End Station'] + '"'
    most_common_trip = df['Trip'].mode()[0]
    most_common_trip_count = list(df['Trip'].value_counts(ascending=False).head(1))[0]
    print("Monst frequent combination of start station and end station trip is {}. With a count of {}\n".format(most_common_trip,most_common_trip_count))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_fmt = str(datetime.timedelta(seconds=int(total_travel_time)))
    print("The total Travel time is {} seconds. Which corresponds to {}".format(total_travel_time, total_travel_time_fmt))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_fmt = str(datetime.timedelta(seconds=int(mean_travel_time)))
    print("The mean Travel time is {} seconds. Which corresponds to {}".format(mean_travel_time, mean_travel_time_fmt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print("User type breakdown\n")
    for i,v in zip(user_types.index,user_types.values):
        print(i,":",v)


    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("\nGender breakdown:\n")
        for i,v in zip(gender.index,gender.values):
            print(i,":",v)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("\nYear of birth stats:\n")
        print("The earliest year of birth is: {}\n".format(int(df['Birth Year'].max())))
        print("The most recent year of birth is: {}\n".format(int(df['Birth Year'].min())))
        print("The most common year of birth is: {}".format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)       
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            records = input("\nWould you like to view a sample of the data (5 random records)? Enter yes or no.\n").lower()
            if records != 'yes':
                break
            else:
                #outputs the original columns from the DF  (5 random rows)
                if 'Gender' in df and 'Birth Year' in df:
                    df['Start Time']  = df['Start Time'].astype(str)
                    print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year']].sample(5).to_json(orient='records', indent = 4))
                else:
                    print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type']].sample(5).to_json(orient='records', indent = 4))


        restart = input("\nWould you like to restart? Enter yes or no.\n").lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()