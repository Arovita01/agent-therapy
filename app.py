from agent_core.master_agent import MasterAgent
from agents.critic_agent import CriticAgent
from dotenv import load_dotenv

load_dotenv()

user_input = "I’ve been feeling anxious and can’t sleep properly."

master = MasterAgent()

# Spawn therapy agents
master.spawn_agent("CognitiveTherapist", "agents.cognitive_therapist")
master.spawn_agent("BehavioralCoach", "agents.behavioral_coach")

# Run session
responses = master.run_session(user_input)

# Evaluate
critic = CriticAgent()
critic.evaluate(responses)
