import datetime
import selenium
from selenium import webdriver
import time
from icalendar import Calendar, Event
import fileinput
from getpass import getpass


def buildEvent(calendar, startTime, endTime, name, location, days):
    if ('M' in days):
        e = Event()
        e.add('summary', name)
        e.add('location', location)
        start_datetime = datetime.datetime.strptime(
            '2019-09-09 ' + str(startTime), "%Y-%m-%d %H:%M")
        end_datetime = datetime.datetime.strptime(
            '2019-09-09 ' + str(endTime), "%Y-%m-%d %H:%M")
        e.add('dtstart', start_datetime)
        e.add('dtend', end_datetime)
        e.add('dtstamp', datetime.datetime.now())
        e.add('rrule', {'freq': 'weekly', 'count': '14'})
        c.add_component(e)
    if ('T' in days):
        e = Event()
        e.add('summary', name)
        e.add('location', location)
        start_datetime = datetime.datetime.strptime(
            '2019-09-10 ' + str(startTime), "%Y-%m-%d %H:%M")
        end_datetime = datetime.datetime.strptime(
            '2019-09-10 ' + str(endTime), "%Y-%m-%d %H:%M")
        e.add('dtstart', start_datetime)
        e.add('dtend', end_datetime)
        e.add('dtstamp', datetime.datetime.now())
        e.add('rrule', {'freq': 'weekly', 'count': '14'})
        c.add_component(e)
    if ('W' in days):
        e = Event()
        e.add('summary', name)
        e.add('location', location)
        start_datetime = datetime.datetime.strptime(
            '2019-09-04 ' + str(startTime), "%Y-%m-%d %H:%M")
        end_datetime = datetime.datetime.strptime(
            '2019-09-04 ' + str(endTime), "%Y-%m-%d %H:%M")
        e.add('dtstart', start_datetime)
        e.add('dtend', end_datetime)
        e.add('dtstamp', datetime.datetime.now())
        e.add('rrule', {'freq': 'weekly', 'count': '15'})
        c.add_component(e)
    if ('R' in days):
        e = Event()
        e.add('summary', name)
        e.add('location', location)
        start_datetime = datetime.datetime.strptime(
            '2019-09-05 ' + str(startTime), "%Y-%m-%d %H:%M")
        end_datetime = datetime.datetime.strptime(
            '2019-09-05 ' + str(endTime), "%Y-%m-%d %H:%M")
        e.add('dtstart', start_datetime)
        e.add('dtend', end_datetime)
        e.add('dtstamp', datetime.datetime.now())
        e.add('rrule', {'freq': 'weekly', 'count': '14'})
        c.add_component(e)
    if ('F' in days):
        e = Event()
        e.add('summary', name)
        e.add('location', location)
        start_datetime = datetime.datetime.strptime(
            '2019-09-06 ' + str(startTime), "%Y-%m-%d %H:%M")
        end_datetime = datetime.datetime.strptime(
            '2019-09-06 ' + str(endTime), "%Y-%m-%d %H:%M")
        e.add('dtstart', start_datetime)
        e.add('dtend', end_datetime)
        e.add('dtstamp', datetime.datetime.now())
        e.add('rrule', {'freq': 'weekly', 'count': '14'})
        c.add_component(e)


def amto24(ampmTime):
    hourTime = ampmTime.split(':')
    if 'AM' in hourTime[1]:
        hour = int(hourTime[0])
        minute = hourTime[1][:2]
    elif 'PM' in hourTime[1]:
        hour = int(hourTime[0])
        if(hour == 12):
            hour = hour  # do nothing
        else:
            hour = hour+12
        minute = hourTime[1][:2]

    return str(hour)+':'+minute


print('Enter your NetID')
username = input()
print('Enter your password')
pw = getpass()

# open chrome and go to CSE schedule
browser = selenium.webdriver.Chrome()
url = "https://enroll.wisc.edu/scheduler"
browser.get(url)  # navigate to the page

# fine the NetID/Username elements
NetID = browser.find_element_by_id("j_username")
password = browser.find_element_by_id("j_password")

NetID.send_keys(username)
password.send_keys(pw)
pw = None  # get rid of password

# finish login
submitButton = browser.find_element_by_name("_eventId_proceed")
submitButton.click()
time.sleep(10)  # wait for page to load

innerHTML = browser.execute_script(
    "return document.body.innerHTML")  # get the HTML from the page

# Get class information with building/room location
classWithLocation = browser.find_elements_by_class_name("fc-content")

# Get class information with days/times
#classWithDays = browser.find_elements_by_xpath("//*[@id=\"scheduler-view\"]/md-card[1]/md-content[1]/section[1]/md-list[2]/md-list-item[1]/div[1]/div[2]/div[1]/div[1]")
classWithDays = []
i = 1
while len(browser.find_elements_by_xpath(f"//*[@id=\"scheduler-view\"]/md-card[1]/md-content[1]/section[1]/md-list[2]/md-list-item[{i}]/div[1]/div[2]/div[1]/div[1]")) is not 0:
    classWithDays.append(browser.find_elements_by_xpath(
        f"//*[@id=\"scheduler-view\"]/md-card[1]/md-content[1]/section[1]/md-list[2]/md-list-item[{i}]/div[1]/div[2]/div[1]/div[1]")[0])
    i += 1

# get only the text for classes with days
classWithDaysText = []
for cls in classWithDays:
    if('Online' not in cls.text):
        classWithDaysText.append(cls.text)  # check for online sections here
# get only the text for classes with locations
classWithLocationText = []
for cls in classWithLocation:
    classWithLocationText.append(cls.text.replace('check_circle', ''))


# get unique set of classes
classWithLocationText = list(set(classWithLocationText))
i = 0
# get 2D list of class attributes
classWithLoc2D = []
for classes in classWithLocationText:
    classWithLocationText[i] = classWithLocationText[i].replace('-', '\n')
    tempClass = classWithLocationText[i].split('\n')

    classWithLoc2D.append([])
    for cls in tempClass:
        classWithLoc2D[i].append(cls)
    i += 1

# get 2D list of class attributes
i = 0
classWithDay2D = []
for classes in classWithDaysText:
    if (not 'Online section' in classWithDaysText[i]):
        tempClass = classWithDaysText[i].split('\n')
        classWithDay2D.append([])
        for cls in tempClass:
            classWithDay2D[i].append(cls)
        i += 1

for classLoc in classWithLoc2D:

    className = classLoc[2][:len(classLoc[2])-10]  # get the class name
    # get the class type (ie dis, lab, lec)
    classType = classLoc[2][len(classLoc[2])-8:len(classLoc[2])-5]

    for classDay in classWithDay2D:
        # only lec
        if(len(classDay) == 3):
            if(className == classDay[0] and classType == classDay[2][:3]):
                classLoc.append(classDay[2].split()[1])
        #lec & dis/lab
        elif(len(classDay) == 4):
            if (className == classDay[0] and classType == classDay[2][:3]):
                classLoc.append(classDay[2].split()[1])
            elif(className == classDay[0] and classType == classDay[3][:3]):
                classLoc.append(classDay[3].split()[1])
        #lec & dis & lab
        elif(len(classDay) == 5):
            if (className == classDay[0] and classType == classDay[2][:3]):
                classLoc.append(classDay[2].split()[1])
            elif (className == classDay[0] and classType == classDay[3][:3]):
                classLoc.append(classDay[3].split()[1])
            elif (className == classDay[0] and classType == classDay[4][:3]):
                classLoc.append(classDay[4].split()[1])


c = Calendar()
for classes in classWithLoc2D:

    startTime = amto24(classes[0])
    endTime = amto24(classes[1])
    name = classes[2]
    location = classes[3]
    days = classes[4]
    buildEvent(c, startTime, endTime, name, location, days)

with open(f'{username}_schedule.ical', 'wb') as schedule:
    schedule.write(c.to_ical())


# add reminder for 15 minutes before the class starts
for line in fileinput.input(f'{username}_schedule.ical', inplace=True):
    print(line.rstrip().replace('END:VEVENT',
                                'BEGIN:VALARM\nACTION:DISPLAY\nDESCRIPTION:REMINDER\nTRIGGER:-PT15M\nEND:VALARM\nEND:VEVENT'))

browser.close()
