import json
from flatten_json import flatten

def jaccard_similarity(A, B):
    #Find intersection of two sets
    nominator = A.intersection(B)

    #Find union of two sets
    denominator = A.union(B)

    #Take the ratio of sizes
    similarity = len(nominator)/len(denominator)
    print("len intersection:", len(nominator) )
    print("len union:", len(denominator) )
    
    return similarity
  
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
 
#print(flat_json)

# Storing key and value as list of tuples using list comprehension
set1 = set([str(key) + "=" + str(value) for key, value in flat_json1.items()])
set2 = set([str(key) + "=" + str(value) for key, value in flat_json2.items()])
set11 = set([str(key) for key, value in flat_json1.items()])
set22 = set([str(key) for key, value in flat_json2.items()])
# resultList1 = [(key, value) for key, value in flat_json1.items()]
# resultList2 = [(key, value) for key, value in flat_json2.items()]
# printing the resultant list of a dictionary key-values
#print(set1)
# for item in resultList1:
#     print(item)

# set1 = set(x for x in resultList1)

# set2 = set(x for x in resultList2)

# x1 = list(dict.fromkeys(resultList1))
# se1 = set(x1)
# x2 = list(dict.fromkeys(resultList2))
# se2 = set(x2)

set1.update(set11)
set2.update(set22)

#calculate jaccard similarity
similarity = jaccard_similarity(set1, set2)

print(similarity)
