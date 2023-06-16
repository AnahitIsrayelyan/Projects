from baseEncrypter import BaseEncrypter

class Decrypter(BaseEncrypter):
    def __init__(self, text, key):
        super().__init__(text)
        self._key = key
        self._decrypted_text = ""


    def decrypt(self) -> str:
        self.execute()
        self._decrypted_text = ""

        for i in range(len(self._splitted)):
            part = self._splitted[i]

            key_part = self._splitted_key[i]
            operations = key_part.split(",")
            operations = operations[::-1]

            for j in operations:
                operation = j
                for operation in operations:
                    rotate_op = operation[0]
                    rotate_count = int(operation[1])

                    if rotate_op == "L":
                        for _ in range(rotate_count):
                            part = self.rotate_right(part)
                    elif rotate_op == "R":
                        for _ in range(rotate_count):
                            part = self.rotate_left(part)
                    elif rotate_op == "D":
                        for _ in range(rotate_count):
                            part = self.rotate_up(part)
                    elif rotate_op == "U":
                        for _ in range(rotate_count):
                            part = self.rotate_down(part)

            self._decrypted_text += part

        self._decrypted_text = self._decrypted_text.replace('$', ' ')  


    def execute(self):
        self.split8elems()
        self.split_key()

    
    def get_decrypted_text(self):
        return self._decrypted_text
