import os
import the_pure_one


class main_menu:
    SAVED_FILES_PATH = "saved_games/"

    def __init__(self):
        pass

    def menu(self):
        print("\nThe Pure One \n")
        print("Please select from the below options:")
        print("1. Continue")
        print("2. New game")
        print("3. Saved games")
        users_selections = input("\nYour selections: ")

        if users_selections == "1":
            self._continue_game()
        elif users_selections == "2":
            self._new_game()
        elif users_selections == "3":
            self._choose_save_file()
        else:
            print("You must select a valid number!")
            self.menu()

    def _continue_game(self):
        the_pure_one.Game().main()  # TODO

    def _new_game(self):
        pass  # TODO

    def _choose_save_file(self):
        pass  # TODO

    def _print_saved_files(self):
        list_of_saved_files = self._saved_files()
        for file in list_of_saved_files:
            if file.split("_")[0] != "save":
                pass
            else:
                try:
                    with open(f"saved_games/{file}") as temp_file:
                        save_name_line = temp_file.readline()
                        save_name = save_name_line.split(" ")[2]
                        print(save_name)
                finally:
                    pass  # TODO

    def _saved_files(self):
        list_of_saved_files = os.listdir(self.SAVED_FILES_PATH)
        list_of_saved_files.sort()
        return list_of_saved_files


if __name__ == '__main__':
    main_menu().menu()
