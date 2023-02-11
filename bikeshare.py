import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','new york city' ,'washington' ]

months = ['all','january', 'february', 'march', 'april', 'may', 'june',
          'july',  'august', 'september', 'october', 'november', 'december']

days = ['all',"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    cityCorrect=False

    while not cityCorrect:
        city=input(" Enter city  '(chicago, new york city, washington).' ")
        city=city.lower()


        if city  in cities:
            cityCorrect=True
        else:
            print("Not valid city , please enter correct city")

    # TO DO: get user input for month (all, january, february, ... , june)

    monthCorrect=False

    while not monthCorrect:
        month=input(" Enter Month  '(all, january, february, ... , june)' ")
        month=month.lower()

        if month  in months:
            monthCorrect=True
        else:
            print("Not valid month , please enter correct month")


    dayCorrect=False
    while not dayCorrect:
        day=input(" Enter Day  '(all, monday, tuesday, ... sunday)' ")
        day=day.lower()

        if day  in days:
            dayCorrect=True
        else:
            print("Not valid day , please enter correct day")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
   
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 # type: ignore    
   
    
    
 

    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = months.index(month)  
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        day= day.capitalize()
         
        df = df[ df['day_of_week'] == day ]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print(df.size)

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}" \
          .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))






    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        # iteratively print out the total numbers of genders
        for index, gender_count in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
    except:
        print(" No Gender column  Gender ")

    print()

    try:

        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("The most common birth year:", most_common_year)

        # the most recent birth year
        most_recent = df['Birth Year'].max()
        print("The most recent birth year:", most_recent)

        # the most earliest birth year
        earliest_year = df['Birth Year'].min()
        print("The most earliest birth year:", earliest_year)


    except:
        print(" No column Birth Year ")
    # TO DO: Display earliest, most recent, and most common year of birth




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
       

        df = load_data(city, month, day)
        if df.empty:
            print('DataFrame is empty.')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            prntRows='yes'
            strt=0
            end=5
            while prntRows.lower()=='yes':
                prntRows = input('\nWould you like to print 5 rows of data? Enter yes or no.\n')
                            
                if prntRows.lower() == 'yes':
                    My_list = [*range(strt, end, 1)]
                    print( df.iloc[My_list])
                    
                    strt=strt+5
                    end=end+5
                    
                    
                
            
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()