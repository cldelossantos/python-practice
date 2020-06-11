months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def translate_to_month(number):
    if number > 12 or number < 0:
        print("Please provide a number 1-12")
    else:
        print(months[number])


translate_to_month(5)