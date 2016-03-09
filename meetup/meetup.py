import datetime

ranks = {'1st':0, '2nd':1,'3rd':2,'4th':3, '5th':4, 'teenth':7}
days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
days_in_week = 7
days_in_four_weeks = 28
teenth_offset = 13

def meetup_day(year, month, day, nth):
    return find_nth(find_first_weekday(year, month, day), nth)
    
def find_first_weekday(year, month, weekday):
#     thanks @phihag http://stackoverflow.com/a/6558571
    d = datetime.date(year, month, 1)
    days_ahead = days.get(weekday) - d.weekday()
    if days_ahead < 0: 
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def find_nth(first_occurence_of_weekday, nth):
    nth_date = first_occurence_of_weekday
    if nth == 'teenth':
        while nth_date.day < teenth_offset:
            nth_date = nth_date + datetime.timedelta(days_in_week)
    else:
        if nth == 'last':
            nth_date = first_occurence_of_weekday + datetime.timedelta(days_in_four_weeks)
            if nth_date.month != first_occurence_of_weekday.month:
                nth_date -= datetime.timedelta(days_in_week)
        else:
            days_to_add = ranks.get(nth)
            nth_date = first_occurence_of_weekday + datetime.timedelta(days_to_add * days_in_week)
    
    if impossible_day(nth_date, first_occurence_of_weekday):
        raise Exception
    
    return nth_date

def impossible_day(d1, d2):
    return d1.month != d2.month