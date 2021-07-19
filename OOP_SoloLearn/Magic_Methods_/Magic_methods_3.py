import random


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        """
        We have overridden the len() function for the class VagueList to return a random number.
        :return: a random number
        """
        return random.randint(0, len(self.cont) * 2)


vague_list = VagueList(["A", "B", "C", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
