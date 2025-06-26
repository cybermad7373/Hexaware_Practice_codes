import random
import pyfiglet

class QuizApp:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is 2+2?": "4",
            "What is the color of the sky?": "Blue",
            "Which planet is known as the Red Planet?": "Mars",
            "What is the largest mammal?": "Blue whale"
        }
        self.score = 0

    def ask_question(self, question, answer):
        user_answer = input(question + " ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    def run_quiz(self):
        self.score = 0  # Explicitly reset score
        items = list(self.questions.items())
        random.shuffle(items)
        
        print("\n" + "="*50)
        ascii_text = pyfiglet.figlet_format("QUIZ APPLICATION")
        print(ascii_text.center(50))
        print("="*50)
        print(f"Total Questions: {len(self.questions)}")
        print("Answer the following questions:\n")
        
        for i, (question, answer) in enumerate(items, 1):
            print(f"Question {i}:")
            self.ask_question(question, answer)
            print()
        
        print("="*50)
        print(f"Your final score is {self.score}/{len(self.questions)}")
        print("="*50)

    def run(self):
        while True:
            print("\n" + "="*50)
            print("QUIZ APPLICATION".center(50))
            print("="*50)
            print("1. Start Quiz")
            print("2. View Total Questions")
            print("3. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                self.run_quiz()
            elif choice == '2':
                print(f"\nTotal questions available: {len(self.questions)}")
            elif choice == '3':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")