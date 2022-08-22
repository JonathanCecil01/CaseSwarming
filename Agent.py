from Ticket import Solution
from Ticket import Step
from Ticket import Ticket
import json

class AgentSwarm:
    def __init__(self, n, domain, swarmID):
        self.swarmID = swarmID
        self.agents = []
        for i in range(0, n):
            a = Agent()
            a.setAgent()
            self.agents.append(a)
        self.solved = []
        self.assigned = []
        self.solving = {}
        self.domain = domain

    def assignCase(self, Ticket):
        self.assigned.append(Ticket)

    def caseSolved(self, Ticket):
        Ticket.solved = True
        self.assigned.pop(Ticket)
        self.solved.append(Ticket)

    def solutionDesign(self, Ticket):
        count =0
        for i in self.assigned:
            print(count, end=" ")
            i.display()
            count+=1

        choice = int(input("Enter the preferred case to solve "))
        t = self.assigned[choice]
        s = Solution()
        while True:
            s.stepInsert(self.swarmID)
            self.solving[t.ticketID] = s
            br_in = input("Enter 0 to break ")
            if br_in=='0':
                break
            else:
                continue
        self.displaySolution(t)


    def displaySolution(self, Ticket):
        self.solving[Ticket.ticketID].display()

class Agent:
    def __init__(self):
        self.name = ""
        self.id = ''
        self.domain = ""
        self.skill = 0

    def setAgent(self):
        # with open("Agents.json", "r") as infile:
        #     json_object = json.load(infile)
        # print(json_object)
        self.name = "jonatan "
        self.id = "jc123"
        self.domain = "Java"
        self.skill = 3
        #
        # self.name = input("Enter Name : ")
        # self.id = input("Enter Agent ID : ")
        # self.domain = input("Enter Domain : ")
        # self.skill = int(input("Enter the skill level : "))



