import datetime
import json

agents_dict = {}
agents_dict = dict(agents_dict)

n = 9
agents = []
for i in range(0, 9):
    agents_dict["Name"] = "jon"+str(i)
    agents_dict["ID"] = "agentID"+str(i)
    agents_dict["Domain"] = "Java"
    agents_dict["Skill"] = 3
    agents.append(agents_dict)

final  = json.dumps(agents, indent =4)

with open("Agents.json", "w") as outfile:
    outfile.write(final)


# doc1_dict = {
#     "Ticket ID": "2342d23442",
#     #"Date" : datetime.datetime(2020, 5, 7),
#     "Category" : "Management",
#     "Priority" : 2,
#     "Solution_Steps":"Step 1: .........\nStep 2:...........\n Step 3:.....",
#     "keywords" : ["12", "123", "123123"]
# }
# doc2_dict = {
#     "Ticket ID": "2342d234sd42",
#     #"Date" : datetime.datetime(2020, 5, 7),
#     "Category" : "Management",
#     "Priority" : 2,
#     "Solution_Steps":"Step 1: .........\nStep 2:...........\n Step 3:.....",
#     "keywords" : ["12", "123", "123123"]
# }
# ls = [doc1_dict, doc2_dict]
# final = json.dumps(ls, indent = 4)
# with open("Documents.json", "w") as outfile:
#     outfile.write(final)
#
# with open("Documents.json", "r") as infile:
#     json_object= json.load(infile)
#
# print(json_object[0]["Ticket ID"])