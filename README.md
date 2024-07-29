    # PYTHON POMODORO TIMER
    #### Video Demo:  https://youtu.be/PzBng99ExEY
    #### Description:
        In this simple program, the user can enjoy and customize the traditional pomodoro timer. The user can set their desired work time and break time, as well as the number of rounds they wish to complete. The program is contained project.py, while test.project.py performs some unit tests to test the methods of pomo(), convert_to_seconds(time), and intro(n, t, w, b, r). The program greets and welcomes the user by prompting them for their name, the task that they will soon be left feeling so productive about, followed by their custom time intervals and number of rounds. The program processes all user input to ensure that value errors are caught, and the program prompts the user to re-enter their values when necessary. Using the python built-in packages 'time' and 'os', this program mimics the countdown of a real pomodoro timer by implementing a constantly updating CLI. The CLI also displays the users name, task, and custom values - just in case they are too lost in thought.

        PROJECT.PY
        In the main() method, default values are initialized and the pomorodo timer is set through set_pomo(). The process_input() method determines if the user's input is valid according to the specified prompt, invalid values, and recieved input. This configuration was chosen in order to perform seperate unit tests on how user input is processed.

        In the set_pomo() method, the variables are initialized through user input, with helper methods that process these inputs. The process_input() method does this by accepting parameters for a prompt, the variable to set, restraints, and an error message according to the type of input.The intro() method summarizes all of the user's customizations to then proceed to the timer.

        The pomo() method executes the timer. Using the os module, it clears the terminal before each timer round. The convert_to_seconds() method converts the user's inputted time to seconds to be used for the countdown.
        The countdown() method returns the value of the time, updating every second using the time module.

        TEST_PROJECT.PY
        test_pomo() ensures that there are no ValueErrors in the pomo() method, e.g. when a string is inputted as a user input instead of an integer.
        test_convert_to_seconds() ensures that the convert_to_seconds() method is mathematically correct
        test_intro() takes advantage of the intro() method which summarizes all user input to ensure that all the input in processed correctly.


