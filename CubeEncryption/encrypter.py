import random
from baseEncrypter import BaseEncrypter


RotationSides = ["R", "L", "U", "D"]


class Encrypter(BaseEncrypter):
    def __init__(self, text) -> None:
        super().__init__(text)
        self._key = ""
        self._encrypted_text = ""


    def encrypt(self) -> str:
        self.execute()
        self._encrypted_text = ""

        for i in range(len(self._splitted)):
            part = self._splitted[i]

            key_part = self._splitted_key[i]
            operations = key_part.split(",")

            for j in operations:
                operation = j
                for operation in operations:
                    rotate_op = operation[0]
                    rotate_count = int(operation[1])

                    if rotate_op == "R":
                        for _ in range(rotate_count):
                            part = self.rotate_right(part)
                    elif rotate_op == "L":
                        for _ in range(rotate_count):
                            part = self.rotate_left(part)
                    elif rotate_op == "U":
                        for _ in range(rotate_count):
                            part = self.rotate_up(part)
                    elif rotate_op == "D":
                        for _ in range(rotate_count):
                            part = self.rotate_down(part)

            self._encrypted_text += part

        return self._encrypted_text

    
    def execute(self):
        self.split8elems()
        self._key = self.generate_key()
        self.split_key()
        print(self._encrypted_text)

    def generate_key(self):
        keyy = ""
        prev_side = ""
        for _ in range(len(self._splitted)):
            part = ""
            parts = random.randint(1, 3)
            for _ in range(parts):
                side = random.choice(RotationSides)
                while side == prev_side: 
                    side = random.choice(RotationSides)
                rand_num = random.randint(1, 3)
                part += str(side) + str(rand_num) + ","
                prev_side = side
            part = part[:-1]
            keyy += part + ":"
        keyy = keyy[:-1]
        return keyy
    

    def get_key(self):
        return self._key
    

    def get_encrypted_text(self):
        return self._encrypted_text
    


if __name__ == "__main__":
    e = Encrypter("hello world")
    e.encrypt()