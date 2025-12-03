class Election:
    def __init__(self):
        self.candidates = []
        self.votes = {}

    def add_candidate(self, name):
        if name not in self.candidates:
            self.candidates[name] = 0
            self.votes[name] = 0
            print(f"Candidate {name} added.")
        else:
            print(f"Candidate {name} already exists.")
    def cast_vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            self.votes[name] += 1
            print(f"Vote casted for {name}")
        else:
            print(f"Candidate {name} does not exist.")

    def show_results(self):
        if not self.candidates:
            print("No candidates available.")
            return
        print("\nElection Results")
        for candidate, vote_count in self.candidates.items():
            print(f"{candidate}: {vote_count} votes")
    #Determine the winner
        winner = max(self.candidates, key=self.candidates.get)
        print(f"\nWinner: {winner} with {self.candidates[winner]} votes")
def main():
    election = Election()
    while True:
        print("=======Election Votes System=======")
        print("\n1. Add Candidate\n2. Cast Vote\n3. Show Results\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter candidate name: ")
            election.add_candidate(name)
        elif choice == '2':
            name = input("Enter candidate name to vote for: ")
            election.cast_vote(name)
        elif choice == '3':
            election.show_results()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

