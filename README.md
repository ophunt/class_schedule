README:

Features:
- Auto generate an iCal file with your class schedule
- Events include class name, building, and room number
- Events also include a reminder 15 minutes before the class starts

Steps for use:

This assumes you have at least Python 3 and pip installed on your computer as well as Google Chrome. If you do not, please see here for python: https://www.python.org/downloads/

NOTE: this script will not work if you are waitlisted for any classes or if you have any classes in your cart. Please wait until you get off the waitlist to do this and/or remove all classes from your cart and only keep classes you are enrolled in.



Mac:
1) install chromedriver
	a) the easiest way to do so is by using homebrew. Install here: https://brew.sh/
	b) type ‘ brew cask install chromedriver ‘ in terminal to install chrome driver
2) install the following python packages:
	a) selenium. Type ‘ pip install selenium ‘ in terminal
	b) icalendar: Type ‘ pip install icalendar ‘ in terminal
3) run the script. The easiest way is to type ‘ python3 {path to script file}
	a) the easiest way to get the path to the script is to drag file onto command line window
	b) when running the script, Chrome will open and auto log-in. It should load your class schedule but if there is an error on the schedule, press refresh. See the error image in the repository for an example.
4) the script will place a file called [yourNetID]_class_schedule.ical in your /Users/[YourAccountName] directory
5) upload the ical file to your calendar tool of choice

Windows:
1) install chromedriver
	a) the easiest way to do so is by using Chocolatey. Install here: https://chocolatey.org/
	b) type ‘ choco install chromedriver ‘ in command prompt
2) install the following python packages:
	a) selenium. Type ‘ pip install selenium ‘ in terminal
	b) icalendar: Type ‘ pip install icalendar ‘ in terminal
3) run the script. The easiest way is to drag and drop the python script onto the command line terminal (if configured)
	a) when running the script, Chrome will open and auto log-in. It should load your class schedule but if there is an error on the schedule, press refresh. See the error image in the repository for an example.
4) the script will place a file called [yourNetID]_class_schedule.ical in your C:/Users/[YourAccountName] directory
5) upload the ical file to your calendar tool of choice
