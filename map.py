MAP = []


class Map:

    def __init__(self):
        self.MAP = MAP

    def set_map(self, path):
        with open(path, mode="rt", encoding="utf-8") as txt_map:
            self.MAP = [list(line) for line in txt_map.read().split()]
