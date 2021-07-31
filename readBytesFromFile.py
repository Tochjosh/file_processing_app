
class ReadBytes:
    def __init__(self):
        self.filename = ''

    def read_all_content(self, filename):
        self.filename = filename
        with open(self.filename) as file:
            return file.read()

    def read_first_two_lines(self, filename):
        self.filename = filename
        with open(self.filename) as file:
            lis = file.readlines()
            return f'{lis[0].strip()}\n{lis[1].strip()}'

    def read_last_two_lines(self, filename):
        self.filename = filename
        with open(self.filename) as file:
            lis = file.readlines()
            return f'{lis[-2].strip()}\n{lis[-1].strip()}'


if __name__ == '__main__':
    filenm = input('Enter the file name or path: ')
    while True:
        prompt = input('>>>Enter\n1 to readall\n2 to read first two\n3 to read last two')
        if prompt in ['1', '2', '3']:
            break
        else:
            print('Wrong option input')
    files = ReadBytes()
    if prompt == '1':
        print(files.read_all_content(filenm))
    elif prompt == '2':
        print(files.read_first_two_lines(filenm))
    elif prompt == '3':
        print(files.read_last_two_lines(filenm))
