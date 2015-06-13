#!/bin/env python2

"""@matchmaking 

This package implements the needed functionaloty to match projects with a 
student.
"""


############### HELPER METHODS ###############

def matchListsOfStrings(sourceList, targetList, compareFun):
    """
    Matches a list of strings (sourceList) to another list of strings 
    (targetList) using a given comparison function (compareFun).

    The function returns the number of matches found as an integer.
    The function will return -1 if any of the lists are empty.
    """
    #Clear for empty strings and test for empty lists.
    emptyString = ""
    while emptyString in sourceList:
        sourceList.remove(emptyString) 
    #while emptyString in targetList:
    #    targetList.remove(emptyString)

    if not sourceList or not targetList:
        return -1

    #Match skills.
    matchSum = 0
    for skill in sourceList:
        matchSum += compareFun(skill, targetList)

    return matchSum


def strictCompare(string, stringList):
    """
    Returns 1 if string is equal to a string in stringList, otherwise 0.
    """
    return any(string.lower() == s.lower() for s in stringList)

def containsStringCompare(string, stringList):
    """
    Returns 1 if string is contained in a string in stringList, otherwise 0.
    Note: boolean values False and True are considered to be 0 and 1,
    respectively, except when converted to string.
    """
    return any(string.lower() in s.lower() for s in stringList)


def compareSkills(userSkills, projects, stringComparefunction=strictCompare):
    """
    Returns list project names ordered by matching degree.
    Only take skills into account, not languages, etc.

    Defaults to using strictCompare if no other function is given.
    """

    sortedProjectList = [(projId, matchListsOfStrings(userSkills, projSkills, 
                          stringComparefunction) ) 
                         for projId, projSkills in projects]
    sortedProjectList.sort(key=lambda tup: tup[1], reverse=True)

    return sortedProjectList
    

def compareSkillsFullString(userSkills, projects):
    """
    Returns list project names ordered by matching degree.
    Only take skills into account, not languages, etc.

    Used for comparing skills when there is a chance that some skills have a 
    space.
    """

    userSkillsWithSpaces = list(filter(lambda s : " " in s, userSkills))

    sortedProjectList = [(projId, 
                          matchListsOfStrings(userSkills, projSkills, 
                                              strictCompare) +  
                          matchListsOfStrings(userSkillsWithSpaces, 
                                              projDescription, 
                                              containsStringCompare)) 
                         for projId, projSkills, projDescription in projects]
    sortedProjectList.sort(key=lambda tup: tup[1], reverse=True)

    return sortedProjectList



############### SETUP METHODS ###############3
# Used for testing purposes

def parseSkills(line):
    """
    Returns the line split by "|".
    """
    return line.split("|")


def loadProjects(path):
    """
    Opens the file specified by path and returns it as a list of tubles on the
    form (project_id, [skills]).
    """
    projects = []
    for line in open(path):
        fields = line.strip().split("::")
        skills = parseSkills(fields[1])
        project_id = int(fields[0])

        projects.append( (project_id, skills) )
    return projects

def loadUser(path):
    """
    Opens the file specified by path and parses it and returns a list of
    strings.
    """
    skills = []
    for line in open(path): #should only run once
        fields = line.strip().split("::")
        skills = parseSkills(fields[1])
    return skills

#Prints projects
def printProjects(projects):
    """
    Pretty prints how a project matched with a student.
    """
    for projId, d in projects:
        print "Project:", projId, "with match degree:", d


# Used for showcase purposes. Ignore this.
if __name__ == "__main__":
    import sys
    n = len(sys.argv)

    if n <= 2:
        print("Path to user and project not provieded. \
              Please give two args with paths to these.")
        sys.exit(0)
    elif n == 3:
        pathUser = sys.argv[1]
        userSkills = loadUser(pathUser)
        pathProj = sys.argv[2]
        projects = loadProjects(pathProj)

        projectsOrdered = compareSkills(userSkills, projects)
        printProjects(projectsOrdered)