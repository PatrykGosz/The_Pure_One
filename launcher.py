import os
import the_pure_one


class MainMenu:
    SAVED_FILES_PATH = "saved_games/"

    def __init__(self):
        self.sorted_list_of_saved_games = self._get_sorted_list_of_saved_files()

    def _get_sorted_list_of_saved_files(self):
        sorted_list_of_saved_games = []

        for file in sorted(os.listdir(self.SAVED_FILES_PATH)):
            if file.split("_")[0] == "save":
                sorted_list_of_saved_games.append(file)
        return sorted_list_of_saved_games

    def menu(self):
        print("\nThe Pure One \n")
        print("1. Continue")
        print("2. New game")
        print("3. Saved games")

        users_selections = int(input("\nYour selection: "))

        if users_selections == 1:
            self._continue_game()
        elif users_selections == 2:
            self.generate_new_save_file()
        elif users_selections == 3:
            self._saved_games()
        else:
            print("You must select a valid number!")
            self.menu()

    def _continue_game(self):
        the_pure_one.Game().main(
            f"{self.SAVED_FILES_PATH}{(sorted(self.sorted_list_of_saved_games, reverse=True))[0]}"
        )

    def generate_new_save_file(self):
        counter = 1
        flag_new_save_file_generated = False

        for file in self.sorted_list_of_saved_games:
            if counter != int((file.split(".")[0]).split("_")[1]):
                with open(f"{self.SAVED_FILES_PATH}save_{counter + 1}.txt", "w") as new_game_temp:
                    new_game_temp.write(f"{self._generate_new_save_file_content()}")
                    flag_new_save_file_generated = True
                    break
            else:
                counter += 1

        if not flag_new_save_file_generated:
            with open(f"{self.SAVED_FILES_PATH}save_{counter}.txt", "w") as new_game_temp:
                new_game_temp.write(f"{self._generate_new_save_file_content()}")
                flag_new_save_file_generated = True

        print(f"\nStarting new game in save file \"save_{counter}.txt\"\n")
        the_pure_one.Game().main(f"{self.SAVED_FILES_PATH}save_{counter}.txt")

    def _generate_new_save_file_content(self):  # TODO
        save_file_content = "NAME = C1E27"
        return save_file_content

    def _saved_games(self):
        print("\nSaves:\n")

        counter = 0

        for file in self.sorted_list_of_saved_games:
            with open(f"{self.SAVED_FILES_PATH}{file}") as temp_file:
                save_name_line = temp_file.readlines()
                try:
                    save_name = save_name_line[0].split(" ")[2]
                except IndexError:
                    save_name = (f"Save {file} corrupted!")
                counter += 1
                print(f"{counter}. {save_name}")
        print(f"\n{counter + 1}. Return")

        users_selections = int(input("\nYour selection: "))

        if users_selections == (counter + 1):
            self.menu()
        elif users_selections > (counter + 1) or users_selections < 1:
            print("\nYou must select a valid number!")
            self._saved_games()
        else:
            the_pure_one.Game().main(f"{self.SAVED_FILES_PATH}{self.sorted_list_of_saved_games[users_selections - 1]}")


if __name__ == '__main__':
    MainMenu().menu()
