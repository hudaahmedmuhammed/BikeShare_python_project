import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities= ['chicago', 'new york city', 'washington']
months = ['january' ,'february' , 'march', 'april', 'may' ,'june', 'all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Name the city you wanna analyze, kindly enter one of these cities {} : '.format(cities).lower())
        if city not in CITY_DATA:
            print('Oops!, The city you\'ve entered seems an invalid input! Try again.')
            continue
        else: 
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Name the month you wanna filter by {} , or enter "all" to apply no month filter: '.format(months).lower())
        if month not in months:
            print('Oops!, The month you\'ve entered seems an invalid input! Try again.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Name the day of week you wanna filter by {} , or enter "all" to apply no day filter: '.format(days))
        if day not in days:
            print('Oops!, The day you\'ve entered seems an invalid input! Try again.')
            continue
        else:
            break

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
    # Loads the data into pandas data frame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))
#     print('The most common month is: ', df['month'].mode()[0], '\n')

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {} '.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: {} '.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is : {}'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is : {}'.format(common_end))


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is : {}'.format(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is : {}'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average travel time is : {}'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types are: {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Counts of gender are: {}'.format(gender))
    else:
        print('There is not any gender information for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest year of birth is : {}'.format(earliest))
        print('The most recent year of birth is : {}'.format(most_recent))
        print('The most common year of birth is : {}'.format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? please enter (yes) or (no).\n')
        if raw.lower() == 'yes':
            print(df[x:x + 5])
            x = x + 5
        else:
            break
    print('-'*40)
            
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
