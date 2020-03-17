# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:35:55 2020

@author: gupta
"""

student_data = ["sunil", "vikrant", "charan"]

student_data_tup = ("sunil", "vikrant", "charan", ["anji", "rajesh"])

print(student_data)

print(student_data[0]) # to print first value

#hashable

# only hashable objects can be keys for a dictionary.

print(hash(student_data[1]  ))

print(hash(100), "hash of 100")

print(hash(-13404333543), "hash of -13404333543")

#print(hash(student_data_tup), "hash of student_data_tup")

stu_data = { 123 : "vikrant", 200 : "sunil", 223 : "charan", 44: "anji", 345: "hara"  }

print(stu_data)

print(stu_data[123])



nw_data = { "fields": {
                "networkfunction": {
                  "resourceType": "calixaxos.resourceTypes.Device",
                  "labelAttribute": "properties.name",
                  "label": "Network Function",
                  "type": "select",
                  "valueAttribute": "providerResourceId"
                },
                "commands": {
                  "resourceType": "calixaxos.resourceTypes.Template",
                  "labelAttribute": "properties.name",
                  "label": "CLI Template",
                  "type": "select",
                  "valueAttribute": "properties.commands"
                },
                "name": {
                  "description": "Name of the template executor",
                  "label": "Name:"
                },
                "node_locs" : [  "hyd", "blr", "pune", "mumbai", "delhi"  ],
                ("hyd", "blr", "pune", "mumbai", "delhi"): "some data"
              }
            }
print("*"*10)
print(nw_data["fields"])
print(nw_data["fields"]["networkfunction"]["resourceType"])
print("*"*20)
# to fetch data from top level in given dictionary.
#for e_k in nw_data:
#    print(e_k)

# to iterate inner data in dictionary, if inner data is another dict.. 
for e_k1 in nw_data:
    for inner_key in nw_data[e_k1]:
        #print(   nw_data[e_k1][inner_key] )
        for inn_k2 in nw_data[e_k1][inner_key]:

            if isinstance(nw_data[e_k1][inner_key], (list, tuple)):
                print(inn_k2)
            elif isinstance(nw_data[e_k1][inner_key], dict):
                print( inn_k2, "-->", nw_data[e_k1][inner_key][inn_k2] )




