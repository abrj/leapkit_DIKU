import json
from pprint import pprint
import ast
import logging

##############################
##      Data Structure      ##
##############################

class Person(object):
    pid = None
    firstName = None
    maidenName = None
    lastName = None
    location = None
    specialities = None
    positions = None
    pictureUrl = None
    publicProfileUrl = None

    #Lists
    skills = None
    educations = None
    courses = None
    languages = None

    def __str__(self):
        ret = "pid = " + self.pid + "\nname = " + self.firstName + " " + self.maidenName + " " + self.lastName + ".\n"
        ret += "\nSkills:"
        for skill in self.skills:
            ret += str(skill)
        ret += "\nLanguages:"
        for language in self.languages:
            ret += str(language)
        ret += "\nEducations:"
        for education in self.educations:
            ret += str(education)
        ret += "\nCourses:"
        for course in self.courses:
            ret += str(course)
        return ret 
        # return ""

class Language(object):
    lid = None
    name = None
    level = None

    def __str__(self):
        return "    lid = " + self.lid + "\n    name = " + self.name + "\n    proficiency = " + self.level + "\n\n"

class Course(object):
    cid  = None
    name   = None
    number  = None

    def __str__(self):
        return "    cid = " + self.cid + "\n    name = " + self.name + "\n    number = " + self.number

class Skill(object):
    cid = None
    name = None

    def __str__(self):
        return "    cid = " + self.cid + ", name = " + self.name + "\n"

class Education(object):
    eid = None
    schoolName = None
    fieldOfStudy = None
    startDate = None
    endDate = None
    degree = None
    activities = None
    notes = None

    def __str__(self):
        return "    eid = " + self.eid + ": " + self.degree + " in " + self.fieldOfStudy + " from " + self.schoolName + "\n"

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
    return person

def fillFullProfile(data):
    """Creates a person based on the data"""
    variables = [s for s in dir(Person) if s[0] != '_']
    person = createPerson()
    logging.error("\n\n")
    logging.error(data)
    logging.error("\n\n")
    logging.error(variables)
    for var in variables:
        if(var == "languages"):
           for language in getSub(data,"languages"):
               classInstance = createSub(var, Language, language)
               person.languages.append(classInstance)
        elif(var == "educations"):
           for education in getSub(data,"educations"):
               classInstance = createSub(var, Education, education)
               person.educations.append(classInstance)
        elif(var == "skills"):
            for skill in getSub(data, "skills"):
               person.skills.append(createSub(var, Skill, skill))
        elif(var == "courses"):
            for course in getSub(data, "courses"):
               person.courses.append(createSub(var, Course, course))
        elif(var == "pid"):
            if(var in data.keys()):
                person.pid = data["id"]
        elif(var == "firstName"):
            if(var in data.keys()):
                person.firstName = data["firstName"]
        elif(var == "maidenName"):
            if(var in data.keys()):
                person.maidenName = data["maidenName"]
        elif(var == "lastName"):
            if(var in data.keys()):
                person.lastName = data["lastName"]
        elif(var == "location"):
            if(var in data.keys()):
                person.location = data["location"]
        elif(var == "specialities"):
            if(var in data.keys()):
                person.specialities = data["specialities"]
        elif(var == "positions"):
            if(var in data.keys()):
                person.positions = data["positions"]
        elif(var == "pictureUrl"):
            if(var in data.keys()):
                person.pictureUrl = data["pictureUrl"]
        elif(var == "publicProfileUrl"):
            if(var in data.keys()):
                person.publicProfileUrl = data["publicProfileUrl"]
        else:
            continue
    return person

def createSub(name, className, data):
    """Fills a sublist"""
    variables = [s for s in dir(className) if s[0] != '_']
    classInstance = className()
    for var in variables:
        if(var[-4:] == "Date"):
            # TODO: More exec, it's not okay.
            exec("classInstance.%s = \"%s\"" % (var, formatDate(get(data,var))))
        elif(var == "name" and (name == "languages" or name == "skills" or name == "publishers")):
            classInstance.name = data[name[:-1]][var]
        elif(var == "level" and name == "languages" and "proficiency" in data):
            classInstance.level = data["proficiency"][var]
        else:
            # TODO: More exec.
            exec("classInstance.%s = \"%s\"" % (var,get(data,var)))
    return classInstance

def formatDate(data):
    """Formates a date"""
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
