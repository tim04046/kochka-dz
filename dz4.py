class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello from {self.name}!")


class Python(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Python")

    def greeting(self):
        print("print('Hello, World!')")


class JavaScript(ProgrammingLanguage):
    def __init__(self):
        super().__init__("JavaScript")

    def greeting(self):
        print("console.log('Hello, World!');")


class CSharp(ProgrammingLanguage):
    def __init__(self):
        super().__init__("C#")

    def greeting(self):
        print('Console.WriteLine("Hello, World!");')


langs = [Python(), JavaScript(), CSharp()]
for lang in langs:
    print(f"{lang.name}:")
    lang.greeting()
    print()
