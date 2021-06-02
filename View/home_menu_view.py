from Controler.tournament_controler import tournamentControler

class HomeMenu:
    def print_home_menu(self):
        print("1: start new tournament")
        print("2: Reload a tournament")
        print("3: see reports and results")
        print("4: Quit")
    
    def is_answer_ok(self, user_input, max_input):
        user_input = int(user_input)
        return user_input > 0 and user_input <= max_input


    def home_menu(self):
        print("--------- HOME MENU ---------")
        self.print_home_menu()
        answer = input("Enter your choice : ")
        max_input = 4
        while not answer.isnumeric() and not self.is_answer_ok(answer, max_input):
            answer = input("Please, enter your choice : : ")
        
        if(answer == "1"):
            print("Hello, you're going to start a new tournament")
            tournament = tournamentControler()
            tournament.new_tournament()
            self.home_menu()
        elif(answer == '2'):
            print("Hello, you're going to reload a tournament")
            tournament = tournamentControler()
            tournament.reload_tournament()
            self.home_menu()
        elif(answer == "3"): 
            print("Hello, you're going to watch reports and results")
            tournament = tournamentControler()
            tournament.report_tournament()  
            self.home_menu()
        elif(answer=="4"):
            print("Bye bye")
            self.home_menu()
            