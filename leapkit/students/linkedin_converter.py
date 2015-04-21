import json
from pprint import pprint
import ast
import logging

##############################
##      Data Structure      ##
##############################

class Person(object):
    pid = "" 
    firstName = ""
    maidenName = ""
    lastName = ""
    location = ""
    specialities = ""
    positions = ""
    pictureUrl = ""
    publicProfileUrl = ""

    #Lists
    skills = []
    educations = []
    courses = []
    languages = []

    def __str__(self):
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
        ret += "\nCourses:\n"
        for course in self.courses:
            ret += "    cid = " + str(course.cid) + ", name = " + course.name + "\n"
        return ret 

class Language(object):
    lid = ""
    name = ""
    level = ""

    # def __str__(self):
        # return "    lid = " + str(self.lid) + "\n    name = " + self.name + "\n level = " + self.level + "\n\n"

class Course(object):
    cid  = ""
    name   = ""

    # def __str__(self):
        # return "    cid = " + str(self.cid) + "\n    name = " + self.name + "\n"

class Skill(object):
    sid = ""
    name = ""

    # def __str__(self):
        # return "    cid = " + str(self.sid) + ", name = " + self.name + "\n"

class Education(object):
    eid = ""
    schoolName = ""
    fieldOfStudy = ""
    startDate = ""
    endDate = ""
    degree = ""

    # def __str__(self):
        # return "    eid = " + str(self.eid) + ": " + self.degree + " in " + self.fieldOfStudy + " from " + self.schoolName + "\n"

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
    # logging.error("\n\n")
    # logging.error(data)
    # logging.error("\n\n")
    # logging.error(variables)
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
            # logging.error("Checking for PID\n")
            # logging.error(data.keys())
            if(u'id' in data.keys()):
                # logging.error("Inserting pid:" + data[u"id"])
                person.pid = data[u"id"]
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
    # logging.error(variables)
    for var in variables:
        if(var == "startDate"):
            classInstance.startDate = formatDate(get(data, var))
        elif(var == "endDate"):
            classInstance.endDate = formatDate(get(data, var))
        elif(var == "name" and (name == "languages" or name == "skills" or name == "publishers")):
            classInstance.name = data[name[:-1]][var]
        elif(var == "name" and name == "courses"):
            classInstance.name = data[var]
        elif(var == "cid"): 
            classInstance.cid = data["id"]
        elif(var == "sid"): 
            classInstance.sid = data["id"]
        elif(var == "lid"): 
            classInstance.lid = data["id"]
        elif(var == "eid"): 
            classInstance.eid = data["id"]
        elif(var == "level" and name == "languages" and "proficiency" in data):
            classInstance.level = data["proficiency"][var]
        elif(var == "schoolName"): 
            classInstance.schoolName = data[var]
        elif(var == "degree"): 
            classInstance.degree= data[var]
        elif(var == "fieldOfStudy"): 
            classInstance.fieldOfStudy= data[var]
        else:
            logging.error("Did not find class variable for " + var)
            # exec("classInstance.%s = \"%s\"" % (var,get(data,var)))
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
