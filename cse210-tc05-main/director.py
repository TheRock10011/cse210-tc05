#I am going to create the Director class.
class director:

    #We needed a start game function.
    def start_game():
         
         #This function is supposed to call the get_word function from the word class.
         (get_word)

    (start_game)

    #We need the input from the user to continue game.
    def get_input_from_console():

        #Call the input function from console.
        (get_input)

    (get_input_from_console)

    #We need a function to take user input to the word class. 
    def send_check_letter():

        #Use the function above to send it to word class.
        (get_input_from_console)

    (send_check_letter)

    #We need a function to take the boolean to the jumper class.
    def continue_game():
        
        #Send the response from the function above to jumper.
        (send_check_letter)

    (continue_game)

    def end_game():

        if continue_game() == False:

            print('Game Over')

        else:

            (get_input_from_console)

    (end_game)