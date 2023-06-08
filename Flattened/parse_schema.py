import json


# Opening JSON files
#f1 = open('local_trial\my_first_schema.json')
#f1 = open('Flattened\myscenarios\data1.json')
f1 = open('schemaresult.json')


# returns JSON object as 
# a dictionary
data = json.load(f1)

#print(data["properties"]["age"]["minimum"])

def safeget(dct, keys):
    print(enumerate(keys))
    for index, key in enumerate(keys):
        print("next key :: ", key)

        if key.isdigit():
            key = int(key)
            try:
                dct = dct["items"]
            except KeyError:
                print("error1")
                return None
        else:
            try:
                dct = dct["properties"]
            except KeyError:
                print("error2")
                return None
            try:
                dct = dct[key]
            except KeyError:
                print("error3")
                return None
    return dct

def parse_key(keystring):
    path_list = keystring.split("_")
    print(path_list)
    return path_list

keys = parse_key("OpenSCENARIO_Storyboard_Story_0_Act_0_StartTrigger_ConditionGroup_0_Condition_0_delay")

node = safeget(data, keys)
print(node)

def get_range(leaf_node, defaultmin=0, defaultmax=33):
    mymax = defaultmax
    mymin = defaultmin
    try:
        mymax = leaf_node["maximum"]
    except KeyError:
        mymax = defaultmax
    try:
        mymin = leaf_node["minimum"]
    except KeyError:
        mymin = defaultmin
    return mymax - mymin
    



print("Range = ", get_range(node))

