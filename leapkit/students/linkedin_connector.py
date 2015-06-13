# Python2.7

from linkedin import linkedin
from httplib import CannotSendRequest


import contextlib
import urlparse
import json

#TODO: Replace with Leapkits own creds.
__API_KEY = '75yv7bexwfjovt'
__API_SECRET = 'Jz3ElgF0hj1RAjb3'
__RETURN_URL = 'http://www.leapkit.com'

#FILE_NAME = 'linkedInResult.json'



def linkedin_get_url(return_url = __RETURN_URL):
    """
    Returns url to our linkedin application.
    Takes a return url to be redirected to after linkedin login.
    """
    authentication = linkedin.LinkedInAuthentication(__API_KEY, 
                                                     __API_SECRET, 
                                                     return_url, 
                                                     linkedin.PERMISSIONS
                                                        .enums.values())
    #print authentication.authorization_url  # open this url on your browser

    return authentication.authorization_url



def linkedin_extract(code, return_url):
    """
    Returns 1 if extraction was successful, otherwise 0.
    Takes the given code from the GET section of the redirect uri, i.e. the 
    LinkedIn url in browser after login.
    Takes the return_url used in the linkedin_get_url to establish connection 
    to LinkedIn. Can be omitted by converting these methods to objects.
    """
    authentication = linkedin.LinkedInAuthentication(__API_KEY, 
                                                     __API_SECRET, 
                                                     return_url, 
                                                     linkedin.PERMISSIONS
                                                        .enums.values())
    #Set auth_code, lib does not do this smartly..
    authentication.authorization_code = code
    authentication.get_access_token() #Needed to access linkedin account info.
    application = linkedin.LinkedInApplication(authentication) #Now get access

    # Extract user information
    # Only extract skills:
    #fields = 'skills'
    # Full extraction:
    fields = ("id," + "first-name," + "last-name," + "headline," + 
              "picture-url," + "industry," + "summary," + "specialties," + 
              "positions:(" + "id," + "title," + "summary," + "start-date," + 
              "end-date," + "is-current," + "company:(" + "id," + "name," + 
              "type," + "size," + "industry," + "ticker)" +")," + 
              "educations:(" + "id," + "school-name," + "field-of-study," + 
              "start-date," + "end-date," + "degree," + "activities," + 
              "notes)," + "associations," + "interests," + 
              "num-recommenders," + "date-of-birth," + "publications:(" + 
              "id," + "title," + "publisher:(name)," + "authors:(id,name)," + 
              "date," + "url," + "summary)," + "patents:(" + "id," + "title," + 
              "summary," + "number," + "status:(id,name)," + "office:(name)," + 
              "inventors:(id,name)," + "date," + "url)," + "languages:(" + 
              "id," + "language:(name)," + "proficiency:(level,name))," + 
              "skills:(" + "id," + "skill:(name))," + "certifications:(" + 
              "id," + "name," + "authority:(name)," + "number," + 
              "start-date," + "end-date)," + "courses:(" + "id," + "name," + 
              "number)," + "recommendations-received:(" + "id," + 
              "recommendation-type," + "recommendation-text," + 
              "recommender)," + "honors-awards," + "three-current-positions," + 
              "three-past-positions," + "volunteer")

    data = application.get_profile(None, None, fields)
    return data