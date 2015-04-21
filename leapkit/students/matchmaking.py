#!/bin/env python2

#import operator

############### HELPER METHODS ###############

#Returns the degree of match between the given list of source and target 
#strings.
#Returns -1 if any list is empty.
#Takes a compare function compareFun, which takes a single string s and a target 
#list l of strings s_i. It must return 1 if s matches any target string s_i, 
#otherwise 0.
def matchListsOfStrings(sourceList, targetList, compareFun):
    #Clear for empty strings and test for empty lists.
    emptyString = ""
    while emptyString in sourceList:
        sourceList.remove(emptyString) 
    while emptyString in targetList:
        targetList.remove(emptyString)

    if not sourceList or not targetList:
        return -1

    #Match skills.
    matchSum = 0
    for skill in sourceList:
        matchSum += compareFun(skill, targetList)

    return float(matchSum) / len(sourceList)




#Returns 1 if string is equal to a string in stringList, otherwise 0.
def strictCompare(string, stringList):
    return any(string.lower() == s.lower() for s in stringList)

#Returns 1 if string is contained in a string in stringList, otherwise 0.
#Note: boolean values False and True are considered to be 0 and 1, respectively,
#except when converted to string.
def containsStringCompare(string, stringList):
    return any(string.lower() in s.lower()  for s in stringList)




#Returns list project names ordered by matching degree.
#Only take skills into account, not languages, etc.
def compareSkills(userSkills, projects):
    stringComparefunction = strictCompare

    sortedProjectList = [(projId, matchListsOfStrings(userSkills, projSkills, stringComparefunction) ) for projId, projSkills in projects]
    sortedProjectList.sort(key=lambda tup: tup[1], reverse=True)

    return sortedProjectList
    



############### SETUP METHODS ###############3
# Used for testing purposes

def parseSkills(line):
    return line.split("|")


def loadProjects(path):
    projects = []
    for line in open(path):
        fields = line.strip().split("::")
        skills = parseSkills(fields[1])
        project_id = int(fields[0])

        projects.append( (project_id, skills) )
    return projects

def loadUser(path):
    skills = []
    for line in open(path): #should only run once
        fields = line.strip().split("::")
        skills = parseSkills(fields[1])
    return skills

#Prints projects
def printProjects(projects):
    for projId, d in projects:
        print "Project:", projId, "with match degree:", d


if __name__ == "__main__":
    import sys
    n = len(sys.argv)

    if n <= 2:
        print("Path to user and project not provieded. Please give two args with paths to these.")
        sys.exit(0)
    elif n == 3:
        pathUser = sys.argv[1]
        userSkills = loadUser(pathUser)
        pathProj = sys.argv[2]
        projects = loadProjects(pathProj)

        projectsOrdered = compareSkills(userSkills, projects)
        printProjects(projectsOrdered)