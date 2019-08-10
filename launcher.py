from saved_games import *
import os


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
            self._print_saved_files()
        else:
            print("You must select a valid number!")
            self.menu()

    def _continue_game(self):
        pass  # TODO

    def _new_game(self):
        pass  # TODO

    def _print_saved_files(self):
        list_of_saved_files = self._saved_files()
        file_id = 0
        for file in list_of_saved_files:
            file_id += 1
            if file.split("_")[0] != "save":
                pass
            else:  # TODO
                try:
                    pass
                except:
                    pass
                else:
                    pass
                finally:
                    pass

    def _saved_files(self):
        list_of_saved_files = os.listdir(self.SAVED_FILES_PATH)
        list_of_saved_files.sort()
        return list_of_saved_files


if __name__ == '__main__':

    print(main_menu()._saved_files())