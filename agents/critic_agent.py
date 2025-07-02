class CriticAgent:
    def evaluate(self, responses):
        print("\n[CRITIC] Evaluating responses...")
        scores = {}
        for name, text in responses.items():
            score = len(text)
            scores[name] = score
            print(f"{name} scored {score}/100")
        return scores
