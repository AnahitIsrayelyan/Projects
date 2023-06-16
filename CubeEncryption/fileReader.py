class FileReader:
    def __init__(self, input_file):
        self._input_file = input_file

    def read(self):
        try:
            with open(self._input_file, 'r') as file:
                text = file.read()
            return text
        except FileNotFoundError:
            return ""

    def write(self, text, output_file):
        try:
            with open(output_file, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print(f"Output file '{output_file}' not found.")

