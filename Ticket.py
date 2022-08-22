import Document

pheromone_pow = 1.2


class Step:
    def __init__(self, agentID):
        self.agentID = agentID
        self.stepCount = 0
        self.stepID = agentID+"_"+str(self.stepCount)
        self.description = ""
        self.pheromoneStrength = 10

    def setStep(self):
        self.stepID = self.agentID+"_"+str(self.stepCount)
        self.stepCount += 1
        self.description = input("Enter the description of the step taken")

    def setStep(self, Step):
        self.stepID = self.agentID+"_"+str(self.stepCount)
        self.stepCount+=1
        self.description = Step.description

    def getStepDescription(self):
        return self.description

    def display(self):
        print('\n---------------------------------------\n')
        print("Step ID : ", self.stepID)
        print("Agent Swarm : ", self.agentID)
        print("Step Description : ", self.description)
        print("Pheromone Strength : ", self.pheromoneStrength)


    def updatePheromone(self):
        self.pheromoneStrength = pheromone_pow*self.pheromoneStrength


class Solution:
    def __init__(self):
        self.steps = []

    def stepInsert(self, agentID, Step=None):
        step  = Step(agentID)
        step.setStep(Step)
        self.steps.append(step)

    def display(self):
        for i in self.steps:
            i.display()


class Ticket:
    def __init__(self, ticketID, description, category, priority, duration):
        self.ticketID = ticketID
        self.description = description
        self.category = category
        self.priority = priority
        self.duration = duration
        self.solved = False

    def display(self):
        print("TICKET ID : " , self.ticketID)
        print("TICKET DESCRIPTION : ", self.description)

