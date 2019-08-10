import os
import the_pure_one


class main_menu:
    SAVED_FILES_PATH = "saved_games/"

    def __init__(self):
        pass

    def menu(self):
        print("\nThe Pure One \n")
        print("1. Continue")
        print("2. New game")
        print("3. Saved games")
        users_selections = input("\nYour selection: ")

        if users_selections == "1":
            self._continue_game()
        elif users_selections == "2":
            self._new_game()
        elif users_selections == "3":
            self._saved_games()
        else:
            print("You must select a valid number!")
            self.menu()

    def _continue_game(self):
        the_pure_one.Game().main()  # TODO

    def _new_game(self):
        the_pure_one.Game().main()  # TODO

    def _saved_games(self):
        print("\nSaves:\n")

        counter = 0

        list_of_saved_files = os.listdir(self.SAVED_FILES_PATH)
        list_of_saved_files.sort()

        for file in list_of_saved_files:
            if file.split("_")[0] != "save":
                pass
            else:
                with open(f"{self.SAVED_FILES_PATH}{file}") as temp_file:
                    save_name_line = temp_file.readlines()
                    try:
                        save_name = save_name_line[0].split(" ")[2]
                    except IndexError:
                        save_name = (f"Save {file} corrupted!")
                    counter += 1
                    print(f"{counter}. {save_name}")

        print(f"\n{counter + 1}. Return")
        print("\nYour selection: ")

        # TODO

if __name__ == '__main__':
    main_menu().menu()
