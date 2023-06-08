from genson import SchemaBuilder
import json


# Opening JSON files
# f1 = open('Flattened\myscenarios\data1.json')
# data1 = json.load(f1)
#print("hi", data1)

builder = SchemaBuilder()

for i in range(1,41):
    f1 = open('Flattened\myscenarios\data' +  str(i) +'.json')
    data1 = json.load(f1)
    builder.add_object(data1)



print(builder.to_schema())

sourceFile = open('schemaresult.json', 'w')
print(builder.to_json(indent=2), file = sourceFile)
sourceFile.close()


