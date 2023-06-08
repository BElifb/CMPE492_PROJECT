import json
from flatten_json import flatten
import collections
import Levenshtein

######################################################
import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
######################################################





def safeget(dct, keys):
    for index, key in enumerate(keys):
        #print("next key :: ", key)
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
    #print(path_list)
    return path_list

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


def string_similarity(A, B):

    #calculate the edit distance
    dist = Levenshtein.distance(A, B)
    if dist == 0:
        return 1
    else:
        return 1/dist

def partial_jaccard_similarity(A, B, schema=None, defaultmin=0, defaultmax=200):

    pay_off = 0.1
    length = len(A) + len(B)
    sim = 0.0
    range = defaultmax - defaultmin

    if len(A) == 0:
        if A == B:
            sim += 1
        else: 
            sim += pay_off
    else:
        for key, value in A.items():
            if key in B.keys():
                length -= 1
                b = B[key]
                if isinstance(value, bool):
                    print("1*")
                    print(value, b)
                    if value == b:
                        sim += 1
                    else: 
                        sim += pay_off
                elif isinstance(value, int):
                    print("2*")
                    if schema != None:
                        range = get_range(safeget(schema, parse_key(key)), defaultmin=defaultmin, defaultmax=defaultmax)
                        print("Calculated range --> ", range, "  for key ", key)

                    #more advanced similarity calculation possible, difference of values if schema has max min limits
                    #range value taken as an argument, default=200
                    value_diff = abs(value - b)
                    if value_diff > range:
                        value_diff = range
                        print("WARNING!!! Difference in integer values exceeds given range. Value diff: ", abs(value-b), " Range: ", range)
                    sim += (range - value_diff)/range
                    print("value_sim ", (range - value_diff)/range, " ::: ", value, b)
                elif isinstance(value, float):
                    print("3*")

                    if schema != None:
                        range = get_range(safeget(schema, parse_key(key)), defaultmin=defaultmin, defaultmax=defaultmax)
                        print("Calculated range --> ", range, "  for key ", key)
                    
                    #more advanced similarity calculation possible, difference of values if schema has max min limits
                    #range value taken as an argument, default=200
                    value_diff = abs(value - b)
                    if value_diff > range:
                        value_diff = range
                        print("WARNING!!! Difference in float values exceeds given range. Value diff: ", abs(value-b), " Range: ", range)
                    sim += (range - value_diff)/range
                    print("value_sim ", (range - value_diff)/range, " ::: ", value, b)
                elif isinstance(value, str):
                    print("4*")
                    #str comparison
                    if isinstance(b, str):
                        sim += string_similarity(value, b)
                        print("str_sim ", string_similarity(value, b), " = ", value, " | ", b )
                    else: 
                        sim += pay_off
                # elif isinstance(value, None):
                else:
                    print("51*")
                    print("attention", value, b)
                    if value == b:
                        sim += 1
                    else: 
                        sim += pay_off

    print("sim : ", sim)
    print("length : ", length)
    res = sim
    if length != 0:
        res /= length
    return res

  
# Opening JSON files
f1 = open('Flattened\myscenarios\data1.json')
f2 = open('Flattened\myscenarios\data2.json')
f3 = open('Flattened\myscenarios\data3.json')
f4 = open('Flattened\myscenarios\data4.json')
#Flattened\myscenarios\UC-001-0001-Kashiwa.json

# returns JSON object as 
# a dictionary
data1 = json.load(f1)
data2 = json.load(f4)

# Reading from file
#data = json.loads(f.read())

flat_json1 = flatten(data1)
flat_json2 = flatten(data2)

myschema1 = open('schemaresult.json')
myschemadata = json.load(myschema1)
 


print([item for item, count in collections.Counter(flat_json2.keys()).items() if count > 1])

#calculate partial jaccard similarity
similarity = partial_jaccard_similarity(flat_json1, flat_json2, myschemadata)

print("RESULT: ", similarity)

################################
sys.stdout = orig_stdout
f.close()
################################
