class Lexemes_Scanner:
    def __init__(self, file_1, file_2, file_3):
        self.file_1 = file_1
        self.file_2 = file_2
        self.file_3 = file_3
        self.lexemes = []

    def make_tokens(self, code):
        lexemes = []
        a = ''
        in_multi_line_comment = False
        for char in code:
            if in_multi_line_comment:
                if char == '' and code[code.find('/')+2:code.find('*/')] == '/':
                    in_multi_line_comment = False
            elif char == '/' and code[code.find('/')+2:code.find('/')] == '*':
                in_multi_line_comment = True
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
        if a:
            lexemes.append(a)
        return lexemes

    def task_1(self, code):
        lines = code.split('\n')
        cl = []
        in_multi_line_comment = False
        for line in lines:
            line_one_by_one = line.strip()
            if 'input' in line:
                continue
            if 'import' in line:
                continue
            if '#' in line:
                continue
            if '"""' in line:
                continue
            if "'''" in line:
                continue
            if line_one_by_one and not line_one_by_one.startswith(('import ', '#', '"""', "'''")):
                cl.append(line)
            if '"""' in line or "'''" in line:
                in_multi_line_comment = not in_multi_line_comment
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
        print(done_1)
        done_2 = self.task_2(self.file_2, ' ; ', '$')
        self.dump(self.file_3, done_2)
        print(done_2)

class Main:
    def run(self):
        example = Lexemes_Scanner("C:\\Users\\Abdul Hannan\\Desktop\\Assignment\\Main Code.txt",
                           "C:\\Users\\Abdul Hannan\\Desktop\\Assignment\\File.1.txt",
                             "C:\\Users\\Abdul Hannan\\Desktop\\Assignment\\File.2.txt")
        example.initializer()
        print("lexemes:")
        print(example.lexemes)

Main().run()