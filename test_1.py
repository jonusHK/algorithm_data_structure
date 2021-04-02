from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self):
        super().__init__('not found agent who meets the conditions')


class Agent(object):
    def __init__(self, name, skills, load):
        self._name = name
        self._skills = skills
        self._load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self._id = id
        self._restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]): #  -> List[Agent]
        return sorted(agents, key=lambda agent: agent._skills)

    def find(self, ticket: Ticket, agents: List[Agent]): #  -> Agent
        return


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]): # -> Agent
        if len(agents) > 0:
            rst_li = sorted(agents, key=lambda agent: agent._load)
            for agent in rst_li:
                if agent._load < 3:
                    return agent
        raise NoAgentFoundException


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]): # -> Agent
        rst_li = []
        for agent in agents:
            restrictions = set(ticket._restrictions)
            intersection = restrictions & set(agent._skills)
            if len(restrictions) == len(intersection):
                rst_li.append(agent)

        if len(rst_li) > 0:
            rst_li = self._filter_loaded_agents(rst_li)
            for agent in rst_li:
                if agent._load < 3:
                    return agent
        raise NoAgentFoundException

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2]))

least_flexible_policy = LeastFlexibleAgent()
print(least_flexible_policy.find(ticket, [agent1, agent2]))