import importlib

class MasterAgent:
    def __init__(self):
        self.agents = {}

    def spawn_agent(self, agent_name, module_path):
        module = importlib.import_module(module_path)
        agent_class = getattr(module, agent_name)
        agent_instance = agent_class()
        self.agents[agent_name] = agent_instance
        print(f"[MASTER] Spawned agent: {agent_name}")
        return agent_instance

    def run_session(self, user_input):
        print(f"[MASTER] User said: '{user_input}'")
        responses = {}
        for name, agent in self.agents.items():
            response = agent.generate_response(user_input)
            print(f"[{name}] → {response}")
            responses[name] = response
        return responses
