import json
from pprint import pprint
import ast
import logging

##############################
##      Data Structure      ##
##############################

class Person(object):
    """A person is used to structure a json string"""

    """Constructor that initiates all the basic person values"""
    pid = "" 
    firstName = ""
    maidenName = ""
    lastName = ""
    location = ""
    specialities = ""
    pictureUrl = ""
    publicProfileUrl = ""

    #Lists
    positions = []
    skills = []
    educations = []
    courses = []
    languages = []

    def __str__(self):
        """Returns a string with all information from that user"""
        ret = "pid = " + self.pid + "\nname = " + self.firstName + " " + self.maidenName + " " + self.lastName + ".\n"
        ret += "\nSkills:\n"
        for skill in self.skills:
            ret += "    cid = " + str(skill.sid) + ", name = " + skill.name + "\n"
        ret += "\nLanguages:\n"
        for language in self.languages:
            "    lid = " + str(language.lid) + ", name = " + language.name + "\n level = " + language.level + "\n"
        ret += "\nEducations:\n"
        for education in self.educations:
            ret += "    eid = " + str(education.eid) + ", degree = " + education.degree + " in " + education.fieldOfStudy +"\n"
        ret += "\nPositions:\n"
        for position in self.positions:
            ret += "    pid = " + str(position.pid) + ", isCurrent = " + str(position.isCurrent) + ", starter " + position.startDate + " and ended " + position.endDate + " worked for company " + position.company + "\n" + "        title was: " + position.title + "\n"
        ret += "\nCourses:\n"
        for course in self.courses:
            ret += "    cid = " + str(course.cid) + ", name = " + course.name + "\n"
        return ret 

class Language(object):
    """A Language is used to hold the languages and profifiency the person knows."""

    """Constructor that initiates all the basic language values"""
    lid = ""
    name = ""
    level = ""

class Position(object):
    """A Position is used to hold the company positions and employment dration a person knows."""

    """Constructor that initiates all the basic position values"""
    endDate = ""
    startDate = ""
    isCurrent = ""
    pid = ""
    company = ""
    title = ""
    summary = ""

class Course(object):
    """A Course is used to hold what courses a person has completed."""

    """Constructor that initiates all the basic course values"""
    cid  = ""
    name   = ""

class Skill(object):
    """Skill is used to hold what skills a person has."""

    """Constructor that initiates all the basic skill values"""
    sid = ""
    name = ""

class Education(object):
    """Education hold what educations a person has completed, what degree it
    gives and from where it was given."""

    """Constructor that initiates all the basic education values"""
    eid = ""
    schoolName = ""
    fieldOfStudy = ""
    startDate = ""
    endDate = ""
    degree = ""

################################
##      Helper Functions      ##
################################

def get(data, query):
    """returns a piece of data if it exists, otherwise returns an empy string"""
    if(query in data):
        return data[query]
    else:
        return ""

def getSub(data, query):
    """Get the values inside the data"""
    if("values" in get(data,query)):
        return get(data, query)["values"]
    else:
        return []

def createPerson():
    """Initiates the person class and fills lists"""
    person = Person()
    person.skills = []
    person.languages = []
    person.educations = []
    person.courses = []
    person.positions = []
    return person

def fillFullProfile(data):
    """Creates a person based on the data"""
    variables = [s for s in dir(Person) if s[0] != '_']
    person = createPerson()
    for var in variables:
        if(var == "languages"):
           for language in getSub(data,"languages"):
               classInstance = createSub(var, Language, language)
               person.languages.append(classInstance)
        elif(var == "educations"):
           for education in getSub(data,"educations"):
               classInstance = createSub(var, Education, education)
               person.educations.append(classInstance)
        elif(var == "positions"):
           for position in getSub(data,"positions"):
               classInstance = createSub(var, Position, position)
               person.positions.append(classInstance)
        elif(var == "skills"):
            for skill in getSub(data, "skills"):
               person.skills.append(createSub(var, Skill, skill))
        elif(var == "courses"):
            for course in getSub(data, "courses"):
               person.courses.append(createSub(var, Course, course))
        elif(var == "pid"):
            if(u'id' in data.keys()):
                person.pid = data[u"id"]
        elif(var == "firstName"):
            if(var in data.keys()):
                person.firstName = get(data,"firstName")
        elif(var == "maidenName"):
            if(var in data.keys()):
                person.maidenName = get(data,"maidenName")
        elif(var == "lastName"):
            if(var in data.keys()):
                person.lastName = get(data,"lastName")
        elif(var == "location"):
            if(var in data.keys()):
                person.location = get(data,"location")
        elif(var == "specialities"):
            if(var in data.keys()):
                person.specialities = get(data,"specialities")
        elif(var == "pictureUrl"):
            if(var in data.keys()):
                person.pictureUrl = get(data,"pictureUrl")
        elif(var == "publicProfileUrl"):
            if(var in data.keys()):
                person.publicProfileUrl = get(data,"publicProfileUrl")
        else:
            continue
    return person

def createSub(name, className, data):
    """Fills a sublist name with the information given in the data json string"""
    variables = [s for s in dir(className) if s[0] != '_']
    classInstance = className()
    for var in variables:
        if(var == "startDate"):
            classInstance.startDate = formatDate(get(data, var))
        elif(var == "endDate"):
            classInstance.endDate = formatDate(get(data, var))
        elif(var == "isCurrent" and name == "positions"):
            classInstance.isCurrent= get(data,var)
        elif(var == "name" and (name == "languages" or name == "skills" or name == "publishers")):
            classInstance.name = get(get(data,name[:-1]),var)
        elif(var == "name" and name == "courses"):
            classInstance.name = get(data,var)
        elif(var == "cid"): 
            classInstance.cid = get(data,"id")
        elif(var == "sid"): 
            classInstance.sid = get(data,"id")
        elif(var == "lid"): 
            classInstance.lid = get(data,"id")
        elif(var == "eid"): 
            classInstance.eid = get(data,"id")
        elif(var == "pid"): 
            classInstance.pid = get(data,"id")
        elif(var == "level" and name == "languages" and "proficiency" in data):
            classInstance.level = get(get(data,"proficiency"),var)
        elif(var == "schoolName"): 
            classInstance.schoolName = get(data,var)
        elif(var == "degree"): 
            classInstance.degree= get(data,var)
        elif(var == "fieldOfStudy"): 
            classInstance.fieldOfStudy= get(data,var)
        elif(var == "title"): 
            classInstance.title = get(data,var)
        elif(var == "summary"): 
            classInstance.summary = get(data,var)
        elif(var == "company"): 
            classInstance.company = get(get(data,var),"name")
        else:
            logging.error("Did not find class variable for " + var)
    return classInstance

def formatDate(data):
    """Formates a date from a json string into the format m/y"""
    if data is "":
        return data
    return str(get(data,"month")) + "/" + str(get(data, "year"))


####################
##      API       ##
####################

def run(rawdata):
    """Transform the data based on if it is in unicode or pure json"""
    if(rawdata[1] == "u"):
        json_data = ast.literal_eval(rawdata)
    else:
        json_data = json.loads(rawdata)
    return fillFullProfile(json_data)

def fromFile(path):
    """Takes a JSON file and creates a datastructure based on it"""
    file = open(path)
    data = ""
    for line in file:
        data += line
    return run(data)

def fromString(data):
    """Takes a JSON string and creates a datastructure based on it"""
    return run(data)
