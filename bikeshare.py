import time
import datetime
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('You can choose from any of the following cities: Chicago, New York City, or Washington. Please type in the city name: ').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        city = input('Sorry, that doesn\'t seem to be valid input, please try again: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Please choose a month (January until June): ').lower()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        month = input('Sorry, that doesn\'t seem to be valid input, please try again: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose a day of the week: ').lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input('Sorry, that doesn\'t seem to be valid input, please try again: ').lower()

    print('Thank you! You will see data filtered by this input:\nCity: ', city.title(), '\nMonth: ', month.title(), '\nDay: ' , day.title())
    print('-'*40)
    return city, month, day

# Fake change for project: Chose grouped filter for the data input.

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    
    # filter by input
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    popular_month = df['month'].mode()[0]
    # display the most common day of week
    popular_dayofweek = df['day of week'].mode()[0]
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('The most popular hour to start renting a bike is at', popular_hour, 'o\'clock. If you did not use filters for \'day\' and \'month\', this is the most popular day of the week:', popular_dayofweek, 'and month:', popular_month)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    see_data = input('\nWould you like to see the raw data for this statistic? Enter yes or no.\n')
    i = 0
    while see_data.lower() == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        see_data = input('\nWould you like to see more? Enter yes or no.\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('This is the station that most people have started renting bikes on the filter you asked for:', popular_start)
    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('This is the station that most people have returned their bikes on the filter you asked for:', popular_end)
    # display most frequent combination of start station and end station trip
    df['startend'] = df['Start Station'] + ' to ' + df['End Station']
    popular_startend = df.startend.mode().iloc[0]
    print('And this is the most popular route (most frequent start and end station combination):', popular_startend)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    see_data = input('\nWould you like to see the raw data for this statistic? Enter yes or no.\n')
    i = 0
    while see_data.lower() == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        see_data = input('\nWould you like to see more? Enter yes or no.\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in hours
    total_travel_time = int(df['Trip Duration'].sum() / 3600)
    # display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean() / 60)
    print('In total, users have rented out bikes for', total_travel_time, 'hours. That\'s', int(total_travel_time / 24), 'days of back-to-back biking! Impressive. However, on average, users have rented out for', mean_travel_time, 'minutes.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    see_data = input('\nWould you like to see the raw data for this statistic? Enter yes or no.\n')
    i = 0
    while see_data.lower() == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        see_data = input('\nWould you like to see more? Enter yes or no.\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Get the current year
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('We have different user types in our database. Here are the user type stats for the filter you set: ')
    print('Subscriber:', user_types[0], '\nCustomer:', user_types[1])

    # Display counts of gender
    gender = df['Gender'].value_counts()
    no_gender = df['Gender'].isnull().sum()
    print('\nThere are', gender[0], 'male users and', gender[1], 'female users in our database.', no_gender, 'users have no male or female gender assigned.')

    # Display earliest, most recent, and most common year of birth
    oldest_user = date.year - int(df['Birth Year'].min())
    youngest_user = date.year - int(df['Birth Year'].max())
    average_age = date.year - int(df['Birth Year'].mean())

    print('\nThe oldest user in the database is', oldest_user, 'years old, the youngest is', youngest_user, 'years old. On average, users are', average_age, 'years old.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    see_data = input('\nWould you like to see the raw data for this statistic? Enter yes or no.\n')
    i = 0
    while see_data.lower() == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        see_data = input('\nWould you like to see more? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()