import json
import Levenshtein

def string_similarity(A, B):

    #calculate the edit distance
    dist = Levenshtein.distance(A, B)

    if dist == 0:
        return 1
    else:
        return 1/dist

def jaccard_similarity_for_list(A, B, order):
    print("here list sim")

    set1 = set()
    set2 = set()

    if len(A) == 0 and len(B) == 0:
        print("A1  : ", A)
        print("B  : ", B)
        return 1
    elif len(A) == 0 and len(B) != 0:
        print("A2  : ", A)
        print("B  : ", B)
        return 0
    elif len(A) != 0 and len(B) == 0:
        print("A3  : ", A)
        print("B  : ", B)
        return 0
    else:
        #assuming A and B lists have elements of the same type as per schema
        if isinstance(A[0], dict) and order == 1:
            length = len(A) + len(B)
            sim = 0.0
            Aden = A
            Bden = B
            for aDict in A:
                for bDict in B:
                    if list(aDict.keys()) == list(bDict.keys()):
                        print("aDict keys", list(aDict.keys()))
                        print("bDict keys", list(bDict.keys()))
                        #??
                        length -= 1
                        sim += recursive_json_similarity(aDict, bDict)
                        #remove bDict to avoid recomparing with other dicts in A
                        B.remove(bDict)
                        #break to avoid comparing with aDict again
                        break
            # for key, value in A.items():
            #     #print("A key ", key)
            #     if key in B.keys():
            #         #print("value " , value)
            #         length -= 1
            #         #b = B[key]
            #         sim += recursive_json_similarity(A, B)

            print(" A for ListComp", Aden )
            print(" B for ListComp", Bden )
            print("ListComp", sim if sim == 0.0 else sim/length )

            return sim if sim == 0.0 else sim/length

        else:
            print("A : ", A)
            set1 = set(x for x in A)

            print("B : ", B)
            set2 = set(x for x in B)

    # d1 = {'a':1, 'b':{'c':2}}
    # d2 = {'b':{'c':2}, 'a':1} # the same according to your definition
    # d3 = {'x': 42}

    # dset.add(json.dumps(d1, sort_keys=True))
    # dset.add(json.dumps(d2, sort_keys=True))
    # dset.add(json.dumps(d3, sort_keys=True))

    # for p in dset:
    #     print json.loads(p) 




    #Find intersection of two sets
    nominator = set1.intersection(set2)

    #Find union of two sets
    denominator = set1.union(set2)

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
#sort the keys ???

# Reading from file
#data = json.loads(f.read())

def recursive_json_similarity(A, B):

    pay_off = 0.1

    print("A => ", len(A))
    length = len(A) + len(B)
    sim = 0.0
    if len(A) == 0:
        if A == B:
            sim += 1
        else: 
            sim += pay_off
    else:
        print("A.items()", A)
        for key, value in A.items():
            print("A key ", key)
            if key in B.keys():
                print("value " , value)
                length -= 1
                b = B[key]
                if isinstance(value, bool):
                    print("2*")
                    if value == b:
                        sim += 1
                    else: 
                        sim += pay_off
                elif isinstance(value, int):
                    print("1*")
                    #more advanced similarity calculation possible, difference of values if schema has max min limits
                    if value == b:
                        sim += 1
                    else: 
                        sim += pay_off
                elif isinstance(value, float):
                    print("12*")
                    #more advanced similarity calculation possible, difference of values if schema has max min limits
                    if value == b:
                        sim += 1
                    else: 
                        sim += pay_off
                elif isinstance(value, str):
                    print("3*")
                    #str comparison
                    if isinstance(b, str):
                        sim += string_similarity(value, b)
                    else: 
                        sim += pay_off
                # elif isinstance(value, (list or tuple)):
                #     #list/set comparison
                #     if isinstance(b, (list or tuple)):
                #         sim += jaccard_similarity_for_list(value, b)
                #     else: 
                #         sim += pay_off
                elif isinstance(value,  dict):
                    print("41*")
                    if isinstance(b, dict):
                        sim += recursive_json_similarity(value, b)
                    else: 
                        sim += pay_off
                elif isinstance(value, list):
                    print("42*")
                    if isinstance(b, list):
                        #solve this tomorrow
                        #sim += recursive_json_similarity(value, b)

                        # sim += jaccard_similarity_for_list(value, b, 1)

                        if value == b:
                            sim += 1
                        else:
                            sim += 2*pay_off
                    else: 
                        sim += pay_off
                elif isinstance(value, tuple):
                    print("43*")
                    if isinstance(b, tuple):
                        sim += recursive_json_similarity(value, b)
                    else: 
                        sim += pay_off
                # elif isinstance(value, None):
                else:
                    print("51*")
                    print("attention")
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



def count_nested_len(d, k):
    length = len(d)
    print(length, d)
    # for key, value in d.items():
    #     if isinstance(value, (dict or list or tuple)):
    #         length += count_nested_len(value)
    return length

print(recursive_json_similarity(data1, data2))

#print(count_nested_len(data1, data2))

