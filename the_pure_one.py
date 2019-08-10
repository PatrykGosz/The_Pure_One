class Game:
    def __init__(self):
        pass

    def main(self, save_game_path):
        with open(save_game_path) as temp_file:
            save_name_line = temp_file.readlines()
            save_name = save_name_line[0].split(" ")[2]
            print(save_name)
