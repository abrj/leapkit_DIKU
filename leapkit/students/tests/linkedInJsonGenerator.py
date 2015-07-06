import json
import random
import testingLists as lists

generate = True 
dirty = True



if generate:
    skillsList = lists.generateRandomSkills(dirty)
else:
    skillsList = getSkills()

def create(typeFunction, percentage):
    retDic = {"skills" : {"_total": 0, "values" : []}}
    while(random.uniform(1,100) < percentage):
        typeFunction(retDic)
    return retDic

def skills(dic):
    isDuplicate = False
    (name, id) = getRand(skillsList)
    # Finds if the skill is a duplicate
    for element in dic.values()[0]["values"]:
        if id == element["id"]:
            isDuplicate = True
    # Adds the element if it is not a duplicate
    if(not isDuplicate):
        newIn = {"skill": {"name": name}, "id" : id}
        dic["skills"]["_total"] += 1
        dic["skills"]["values"].append(newIn)

def getRand(list):
    return(list[random.randint(0,len(list)-1)])

print json.dumps(create(skills, 85))
