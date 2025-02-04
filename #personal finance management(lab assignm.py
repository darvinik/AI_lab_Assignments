#personal finance management(lab assignment 1 (11))

class FinMgr:
    def __init__(self, inc, bud, sav_goal):
        self.inc = inc 
        self.bud = bud  
        self.sav_goal = sav_goal 
        self.exp = {}  
        self.sav = 0 

    def add_exp(self, cat, amt):
        if cat not in self.exp:
            self.exp[cat] = 0
        self.exp[cat] += amt
        print(f"Added expense: ${amt} in {cat}")

    def track_exp(self):
        print("\nExpense Report:")
        for cat, amt in self.exp.items():
            print(f"{cat}: ${amt} (Budget: ${self.bud.get(cat, 0)})")
            if amt > self.bud.get(cat, 0):
                print(f" Overspending detected in {cat}!")

    def calc_sav(self):
        tot_exp = sum(self.exp.values())
        self.sav = self.inc - tot_exp
        print(f"\nTotal Savings: ${self.sav}")

    def rec_sav_strat(self):
        if self.sav < self.sav_goal:
            print(" Recommendation: Reduce unnecessary expenses to meet your savings goal!")
        else:
            print("You are on track to meet your savings goal!")

# Example Usage
inc = 5000  # Monthly income
bud = {"Rent": 1500, "Food": 600, "Entertainment": 300, "Utilities": 400}
sav_goal = 1000

fin_agent = FinMgr(inc, bud, sav_goal)

# Adding expenses
fin_agent.add_exp("Food", 700)
fin_agent.add_exp("Entertainment", 400)

# Tracking expenses and savings
fin_agent.track_exp()
fin_agent.calc_sav()
fin_agent.rec_sav_strat()
