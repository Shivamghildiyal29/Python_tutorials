#datetime modules
import datetime

#install pytz package to include TimeZone information
import pytz

#naive datetimes dont have enough data for example Time zone information
#aware date time have data like time zone and day light savings

#datetime.date - working with year month days
d= datetime.date(2020, 11, 1) #no leading zeros before the single digit daye or month
print(d)

d_t= datetime.date.today() #gives the current date
print(d_t) #entire date
print(d_t.day) #gives day
print(d_t.month)#gives month
print(d_t.year) #gives year

#day of the week
print(d_t.weekday()) #monday =0; sunday =6
print(d_t.isoweekday()) #monday =1; sunday =7


#Time deltas-difference between times:
#Date +/-Tdelta = New date
t_del = datetime.timedelta(days=7)# makes a duration of 7 days
print(d_t + t_del) #gives date 1 week forward
print(d_t - t_del) #gives date one week ago

#Date +/- date = Tdelta
bday= datetime.date(2022, 9, 29)
T_date=bday-d_t
print(T_date)
print(T_date.days) #gives only days
print(T_date.total_seconds()) #gives seconds

#datetime.time-working with hours, minutes, seconds and microseconds
t= datetime.time(13,47,10,100215) #passing local time
#naive time without timezone information
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


#datetime.datetime: combination of bothe date and time funcitons of datetime module
dt= datetime.datetime(2020, 11, 1, 13,47,10,100215)
print(dt)
print(dt.date())#print only date
print(dt.year)#prints the year
print(dt.time())#printsonly time
print(dt.hour)

#Using time delta in the datetime
t_del1 = datetime.timedelta(days=10)
t_del2 = datetime.timedelta(hours = 20)

print(dt - t_del1)
print(dt +t_del2)
print(dt +t_del1 + t_del2)

#Constructors to add date time datatypes

d_today= datetime.datetime.today() #current local datetime of no timezone
d_now= datetime.datetime.now() #current local time with option to pass Time zone info
d_unow= datetime.datetime.utcnow() #current utc time but default TZ info is none

#Timezone aware datatime datetypes: Naive to UTC
dt= datetime.datetime(2020, 11, 1, 13,47,10,100215,tzinfo =pytz.UTC )
print(dt)
dnow= datetime.datetime.now(tz =pytz.UTC)
print(dnow)
dunow= datetime.datetime.utcnow().replace(tzinfo =pytz.UTC)
print(dnow)

#Converting to UTC time to desired timezone: UTC to desired date time
dt_Delhi =dnow.astimezone(pytz.timezone("Asia/Kolkata")) #Timezone can be determined from pytz.all_timezones

#Converting naive time to desired timezone
dt_now= datetime.datetime.now(tz =pytz.timezone("Asia/Kolkata"))
#To print all the timezones available
for t in pytz.all_timezones:
    print(t)

#Displaying the date: Formatting codes can be found on python documentation
dt_now= datetime.datetime.now(tz =pytz.timezone("Asia/Kolkata"))
print(dt_now.isoformat()) #interantional standard
print(dt_now.strftime('%B %d, %Y')) #format codes for desired formats

#String to date time
dt_string= '2020-12-01'
dt_str=datetime.datetime.strptime(dt_string, '%B %d, %Y')
print(dt_str)
dt_str=datetime.datetime.strptime(dt_string, "format of date string")
