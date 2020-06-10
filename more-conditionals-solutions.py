def season_teller(month_number):
    if month_number > 0 and month_number < 3:
        print("It's Winter")
    elif month_number == 3:
        print("March marks the end of Winter and the beginning of Spring with the Vernal Equinox, Thursday, March 19, 2020, 11:50 p.m.")
    elif month_number > 3 and month_number < 6:
        print("It's Spring")
    elif month_number == 6:
        print("Summer begins with the Summer Solstice, Saturday, June 20, 2020, 5:44 p.m.")
    elif month_number > 6 and month_number < 9:
        print("It's Summer")
    elif month_number == 9:
        print("Autumn begins with the Autumnal Equinox, Tuesday, September 22, 2020, 9:31 a.m.")
    elif month_number > 9 and month_number < 12:
        print("It's Winter") 
    elif month_number == 12:
        print("Winter begins with the Winter Solstice, Monday, December 21, 2020, 5:02 a.m.")
    else:
        to_string = str(month_number)
        if to_string[:-2] == str(13):
            suffix = "th"
        elif to_string[-1] == str(1):
            suffix = "st"
        elif to_string[-1] == str(2):
            suffix = "nd"
        elif to_string [-1] == str(3):
            suffix = "rd"
        else:
            suffix = "th"
        print ('Theres no {month_number}{suffix} month, please enter a number 1-12'.format(month_number = month_number, suffix = suffix))


season_teller(-5)