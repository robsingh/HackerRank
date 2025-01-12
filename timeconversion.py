'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

def timeConversion(s):
    if s[-2] == 'A':
        if s[0] == '1' and s[1] == '2':
            s = '00' + s[2:-2]
        else:
            s = s[:-2]
    elif s[-2] == 'P':
        if s[0] == '1' and s[1] == '2':
            s = s[:-2]
        else:
            s = str(int(s[:2]) + 12) + s[2:-2]
    
    return s


s = '04:00:00PM'
print(timeConversion(s))