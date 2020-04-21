'''
work_hours = int, total hours in week
day_hours = int, max hours work in a day
pattern = string, partially completed schedule
return ARRAY OF STRINGS
'''

def findSchedules(work_hours, day_hours, week):
    all = []
    temp = []
    
    remaining = work_hours
    blanks = 0
    blank_dictionary = {}
    for i, day in enumerate(week):
        if day != '?':
            remaining -= int(day)
        else:
            blanks += 1
            blank_dictionary[i] = -1

    

    
    print(remaining)
    print(blanks)
    print(blank_dictionary)
    return all


if __name__ == '__main__':
    work_hours = 24
    day_hours = 8
    week = '08??840'

    findSchedules(work_hours, day_hours, week)