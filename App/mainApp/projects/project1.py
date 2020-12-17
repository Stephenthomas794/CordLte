from flask import Blueprint, render_template 
def project1_blueprint_factory(send):
    #Libaries
    # Flask 
    #  - Flask is a lightweight WSGI web framework
    #  - Helps gets started quickly with building and scaling an application
    project1 = Blueprint("project1", __name__, static_folder="static",template_folder="templates")  
    # - For Updating the time when search is done
    from datetime import datetime

    # - To make HTTP Requests
    # - Automatically adds query strings, by adding parameters. But I did not do that
    # - Keep Alive and https connection pooling is done automatically 
    import requests 

    # - To prevent IP address blacklist from too many Requests
    import time
    from random import randint

    # Data Science Libaries to parse ZipCode Files
    # Numpy is not used in this application 
    # Numpys is used for multidiemntional arrays 
    # Pandas is great for in-memory 2d table objects called Dataframe
    import numpy as np
    import pandas as pd

    # - For parsing result 
    import re

    # - For Sending Email
    import smtplib, ssl


    #Blueprint
    #from run import send 
    # Routing to Main Page
    # This allows to route to different webpages
    # There is only one webpage for this application


    # Calls the "CheckZipCode" function
    # Converts it to a string
    # Returns to main page
    @project1.route('/project1run', methods = ['POST','GET']) 
    def hello():
        value = str(CheckZipCodes(send))
        return value

    # For every 1000 zipCode Searches Create a new File
    # Have this function here as backup to generate a file
    # This was to store information locally to prevent a rerun of the entire application
    def GenerateFile(timeToCreate):
        pass

    # Email File every 1000 zipCodes
    # Unused code
    # Copy and Paste from internet
    # Default
    def EmailFile():
        port = 465  # For SSL
        password = input()

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("my@gmail.com", password)
            # TODO: Send email here

    # Checking all the zip codes
    def CheckZipCodes(send):

        # Opens totals.txt file for storing data locally
        # The file reader has been given the aplication to create a new file is totals does not exist and write to file
        # Calls the cleanAndReturnZip function to get all the zipcodes
        # Sets the word we are looking for in MLS as "listingID:"
        # This means we know for everytime we find a listingID on that page, there is a foreclosure
        # Totals variable is used to keep track of total amount of forclosures
        # Counter variable is used to keep track of what zipCode we are on in the zipCode List
        # CountOfForeclosures keeps track of how many foreclosures at that specific zipCOde
        f = open("static/project1txt/Totals0.txt","w+")
        ftime = open("static/project1txt/date.txt","w+")
        zipCodes = list()
        zipCodes = cleanAndReturnZip()
        word = "listingId:"
        total = 0
        counter = 0
        countOfForclosures = 0

        # Make HHTP request for every zip code to the URL
        # For each zipCode in the zipCode list
        # First write the URl with its query string (so its MLS website + zipcode number"
        # Make the request using requests libaray
        # Turn the response into text
        # Split the request into a new line
        for item in zipCodes:
            url = "https://mls.foreclosure.com/listing/search?lc=foreclosure&loc=" + item
            requestUrl = requests.get(url)
            requestText = requestUrl.text
            requestTextSplit = requestText.split('\n')

            # Check every line to see if it equals "var marketdata"
            # For each line of the esponse we are looking for 'var markerdata" which is where listing IDs are stored
            for lines in requestTextSplit:
                if lines[0:15].lower() == 'var markersdata':

                    #F Count the number of times "listingID:" shows up to see the number of postings for that zip code
                    # We use the regex libaray (re), and sum function to find
                    # finditer from re libaray allows up to find all non overlapping matches in a string
                    # escape from re libary ignores all special characters
                    # Once we find total number of times "listing ID:" is found, we set that equal o countOFForclosures
                    # We then add this count to the total varible
                    # print to command line the count of foreclosures for this particular zipcode
                    # write to file the count of forclosures for this particluar zip code
                    countOfForclosures = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), lines))
                    total = total + countOfForclosures
                    print("Zip Code: {} Total Forclosures: {} \n".format(zipCodes[counter],countOfForclosures))
                    f.write("Zip Code: {} Total Forclosures: {} \n".format(zipCodes[counter],countOfForclosures))
                    send(zipCodes[counter], countOfForclosures)
            # Reset count Of Foreclosures
            # add one to counter to move to next zipcode
            # Set sleep timer to avoid the website knowing we are a bot
            # Sleep timer waits between 0 and 1 second
            countOfForclosures = 0
            counter = counter + 1
            time.sleep(randint(0,150)/100)

        # print to command line the total number of foreclosures
        # write to file total number of forclosures
        # close the file
        # return total number of foreclosures
        print("Total Overall Forclosures: {}".format(total))
        now = datetime.now()
        ftime.write("{}".format(now.strftime("%d/%m/%Y %H:%M:%S")))
        f.write("Total Overall Forclosures: {}".format(total))
        f.close()
        ftime.close()
        return total

    # Clean the csv File and return zip codes as strings
    # Columns Avaliable: Zip, City, State ID, Population, County Names
    # Clean up the file by dropping all un needed columns
    # First read the CSV file and turn into a data frame using pandas (zip varibale)
    # Dataframes allow you to handle the information easier
    # Nxt Drop all unneed columns
    # Used the pandas libaray and the drop property
    # Used the head property to make sure I only have what I needed
    # Created a new varibale zipCodes and turned it into a list
    # Used the map function to iterate over only the zip codes in the data frame
    # And turn all the values into strings
    # Returned the new list of all ZipCOdes as a list
    def cleanAndReturnZip():
        zip = pd.read_csv('static/project1txt/uszips.csv')
        zip.drop('timezone',axis=1,inplace=True)
        zip.drop('military',axis=1,inplace=True)
        zip.drop('imprecise',axis=1,inplace=True)
        zip.drop('county_fips_all',axis=1,inplace=True)
        zip.drop('county_name',axis=1,inplace=True)
        zip.drop('density',axis=1,inplace=True)
        zip.drop('parent_zcta',axis=1,inplace=True)
        zip.drop('lng',axis=1,inplace=True)
        zip.drop('lat',axis=1,inplace=True)
        zip.drop('zcta',axis=1,inplace=True)
        zip.drop('county_fips',axis=1,inplace=True)
        zip.drop('county_weights',axis=1,inplace=True)
        zip.head()
        zipCodes = list()

        # Convert the list of zip codes to string
        zipCodes = list(map(str, zip['zip']))
        return zipCodes
    return project1
