import datetime

d = datetime.date(2022, 9, 4)
print(type(d))
print(d)
print(f'day: {d.day}')
print(f'month: {d.month}')
print(f'year: {d.year}')
print(f'weekday: {d.weekday()}')
# weekday: Monday 0, Sunday 6
print(f'isoweekday: {d.isoweekday()}')
# isoweekday: Monday 1, Sunday 7

today = datetime.date.today()
print(f'\ntoday: {today}')

# ======================================================================================================================
# timedelta()

tdelta = datetime.timedelta(weeks=7)
print(f'weeks: {tdelta.weeks}')
print(f'days: {tdelta.days}')
#print(f'hours: {tdelta.hours}')
#print(f'minutes: {tdelta.minutes}')
print(f'seconds: {tdelta.seconds}')
#print(f'milliseconds: {tdelta.milliseconds}')
print(f'microseconds: {tdelta.microseconds}')
