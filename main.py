from Ticket import Ticket
from Ticket import Solution
import Agent
from Agent import AgentSwarm
import json

def ticket_load():
    with open("Cases.json", "r") as infile:
        json_object = json.load(infile)
    return json_object

def main():
    aswarm_list = []
    tickets = []
    no_of_swarm = int(input("Enter the no of Swarms : "))
    for i in range(0, no_of_swarm):
        print("Swarm ", i, "id : AS_", i)
        no_of_agents = int(input("Enter the no of Agents in the swarm : "))
        domain = input("Enter the domain of the Swarm : ")
        print("\n-----------------------------------------\n")
        aswarm_list.append(AgentSwarm(no_of_agents, domain, "AS_"+str(i)))
    ticket_dict = ticket_load()
    for i in ticket_dict:
        ticket_id = i["Ticket ID"]
        category = i["Category"]
        prioirity  = i["Priority"]
        description = i["description"]
        duration = i["duration"]
        tickets.append(Ticket(ticket_id, description, category, prioirity, duration))

    for i in aswarm_list:
        for j in tickets:
            i.assignCase(j)


    #Solution
    while True:
        for i in aswarm_list:
            count =0
            for j in i.assigned:
                print(count, end=" ")
                j.display()
                count += 1
            choice = int(input("Enter the preferred case to solve "))
            t = i.assigned[choice]
            i.solutionDesign(t)
            for j in aswarm_list:
                if j.swarmID!=i.swarmID:
                    print("\n--------------------\n")
                    print("Agent Swarm ", i.swarmID, " adopted the step : ")
                    i.solving[t.ticketID].display()
                    print("Would you adopt the same step or otherwise? : ")
                    choice2 = int(input("1 for yes 0 for no : "))
                    if choice2:
                        s = Solution()
                        s.stepInsert(j.swarmID, i.solving[t.ticketID])


    # as1.assignCase(t1)
    # as1.solutionDesign()
    # as1.displaySolution(t1)

if __name__ == "__main__":
    main()