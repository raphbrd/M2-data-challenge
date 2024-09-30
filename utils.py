""" Utility functions """
import numpy as np
import pandas as pd


def get_trip_duration(taxi_data):
    """ Return the duration in minutes for each trip in taxi data

    Parameters
    ----------
    taxi_data : pd.DataFrame

    Returns
    -------
    a numpy array of the durations in minutes
    """
    do = taxi_data["tpep_dropoff_datetime"]
    pu = taxi_data["tpep_pickup_datetime"]
    return pd.to_timedelta(do - pu).values.astype(float) * 1e-6


def get_rush_hours(hs, days):
    """ return a boolean indicating whether a given trip is during rush hours.

    Rush hours are between 7am and 10am or 4pm and 7pm during a work day
    (from Monday to Friday included).

    Parameters
    ----------
    hs: pd.Series | np.array
        the hour of each trip
    days: pd.Series | np.array
        list of the full string indicating the day of the trip

    Returns
    -------
    a numpy array of the rush hours (boolean)
    """
    workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    is_rush_hour = (hs.between(7, 10, inclusive='left')) | (hs.between(16, 19, inclusive='left'))

    # Return boolean indicating both conditions are met
    return days.isin(workdays) & is_rush_hour
