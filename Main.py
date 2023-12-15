class Lexemes_Scanner:
    def __init__(self, file_1, file_2, file_3):
        self.file_1 = file_1
        self.file_2 = file_2
        self.file_3 = file_3
        self.lexemes = []

    def make_tokens(self, code):
        lexemes = []
        a = ''
        multi_line_comment = False
        for char in code:
            if multi_line_comment:
                if '*/' in code:
                    multi_line_comment = False
            elif char == '/' and code.startswith('/*', code.find('/') + 1):
                multi_line_comment = True
            elif char.isalnum() or char == '_':
                a += char
            else:
                if a:
                    lexemes.append(a)
                    a = ''
                if char.isspace():
                    continue
                elif char == '#':
                    while char != '\n':
                        char = next(code)
                else:
                    lexemes.append(char)
        return lexemes

    def task_1(self, code):
        lines = code.split('\n')
        cl = []
        multi_line_comment = False
        for line in lines:
            one_line = line.strip()
            if 'import' in line:
                continue
            if '#' in line:
                continue
            if '"""' in line:
                continue
            if "'''" in line:
                continue
            if one_line and not one_line.startswith(('import ', '#', '"""', "'''")):
                cl.append(line)
            if '"""' in line or "'''" in line:
                multi_line_comment = not multi_line_comment
        return '\n'.join(cl)

    def load(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def dump(self, file_path, code):
        with open(file_path, 'w') as file:
            file.write(code)

    def task_2(self, file_path, separator, sentinel):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        joined_lines = separator.join(lines) + sentinel
        return joined_lines

    def initializer(self):
        input_code = self.load(self.file_1)
        done_1 = self.task_1(input_code)
        self.lexemes = self.make_tokens(iter(done_1))
        self.dump(self.file_2, done_1)
        print("\nTask#01\n")
        print(done_1)
        done_2 = self.task_2(self.file_2, ' ; ', '$')
        print()
        print("Task#02\n")
        print(done_2)
        print("\nTask#03\n")
        self.dump(self.file_3, done_2)

class Main:
    def run(self):
        scan = Lexemes_Scanner("Main Code.txt",
                           "File.1.txt",
                             "File.2.txt")
        scan.initializer()
        print("lexemes:")
        num=0
        for lex in scan.lexemes:
            num=num+1
            print(f"{num} {lex}")

Main().run()
