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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york ciyty, washington). HINT: Use a while loop to handle invalid inputs
    
    while(True):
        city =input("enter valid city name: ")
        city = city.lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    monthss = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december','all']
    while(True):
        month =input("enter valid month name: ")
        month = month.lower()
        if month in monthss:
            break
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayss = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while(True):
        day =input("enter valid day name: ")
        day = day.lower()
        if day in dayss:
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime( df['Start Time'] )
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print("loading data is done ")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month: ',df['month'].mode()[0])
    print("#########################################\n")

    # TO DO: display the most common day of week

    print("the most common day: ",df['day_of_week'].mode()[0])
    print("#########################################\n")

    # TO DO: display the most common start hour

    print("the most common start hour: ",df['Start Time'].dt.hour.mode()[0])
    print("#########################################\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most common start station: ",df['Start Station'].mode()[0])
    print("#########################################\n")


    # TO DO: display most commonly used end station
    print("the most common end station: ",df['End Station'].mode()[0])
    print("#########################################\n")


    # TO DO: display most frequent combination of start station and end station trip
    df['combination of start station and end station'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    print(df['combination of start station and end station'].mode()[0])
    print("#########################################\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #print("total travel time: ",pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).head())
    
    start_index = 0
    end_index = 5
    while(True):
        total_travel_time = pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).iloc[start_index : end_index]

        print("total_travel_time: \n", total_travel_time)
        
        if end_index + 5 >  pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).size:
            print("this was the last elemens")
            break
        
        start_index = end_index
        end_index = start_index+5
        
        more_data = input('\nWould you like to display more data? Enter yes or no.\n')

        if more_data.lower() != 'yes':
            break
    
    
    # TO DO: display mean travel time
    print("mean travel time: ",pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
#     user_types = df['User Type'].value_counts().head()
#     print(user_types)
    start_index = 0
    end_index = 5
    while(True):
        user_types = df['User Type'].value_counts().iloc[start_index : end_index]

        print("count user_types: \n", user_types)
        
        if end_index + 5 >  df['User Type'].value_counts().size:
            print("this was the last elemens")
            break
        
        start_index = end_index
        end_index = start_index+5
        
        more_data = input('\nWould you like to display more data? Enter yes or no.\n')

        if more_data.lower() != 'yes':
            break
    # TO DO: Display counts of gender
#     gender = df['Gender'].value_counts().head()
#     print(gender)
    print("#########################################\n")

    start_index = 0
    end_index = 5
    while(True):
        gender = df['Gender'].value_counts().iloc[start_index : end_index]

        print("conut gender: \n", gender)
        
        if end_index + 5 >  df['Gender'].value_counts().size:
            print("this was the last 5 elemens")
            break
        
        start_index = end_index
        end_index = start_index+5
        
        more_data = input('\nWould you like to display more data? Enter yes or no.\n')

        if more_data.lower() != 'yes':
            break
     
        print("#########################################\n")

    
        # TO DO: Display earliest, most recent, and most common year of birth

    earliest = df['Birth Year'].min()
    print("earliest year of birth: ", earliest)    
    print("#########################################\n")

    recent = df['Birth Year'].max()
    print("most recent year of birth : ", recent)
    print("#########################################\n")

    common = df['Birth Year'].mode()[0]
    print("most common year of birth: \n", common)
    print("#########################################\n")

    
    
    start_index = 0
    end_index = 5    
#     while(True):
#         common = df['Birth Year'].value_counts().iloc[start_index : end_index]

#         print("most common year of birth: \n", common)
        
#         if end_index + 5 > df['Birth Year'].value_counts().size:
#             print("this was the last 5 elemens")
#             break
        
#         start_index = end_index
#         end_index = start_index+5
        
#         more_data = input('\nWould you like to display more data? Enter yes or no.\n')

#         if more_data.lower() != 'yes':
#             break
            
        
    print("\nThis took %s seconds." % (time.time() - start_time))
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
