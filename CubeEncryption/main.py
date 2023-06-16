from encrypter import *
from decrypter import *
from fileReader import *


if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "output.txt"
    final_output_path = "FinalOutput.txt"

    fileReader = FileReader(input_path)
    raw_text = fileReader.read()
    
    encypter = Encrypter(raw_text)
    encypter.encrypt()

    keyy = encypter.get_key()
    encrypted_text = encypter.get_encrypted_text()

    fileReader.write(encrypted_text, output_path)

    decrypter = Decrypter(encrypted_text, keyy)
    decrypter.decrypt()
    decrypted_text = decrypter.get_decrypted_text()

    fileReader.write(decrypted_text, final_output_path)

