import pandas as pd


class SpreadSheet:
    def __init__(self):
        self.filename = ''
        self.delimiter = ','

    def __verify_file_type(self):
        try:
            df = pd.read_csv(self.filename, sep=self.delimiter)
        except FileNotFoundError as err:
            raise err

        self.filetype = self.filename[-4:]
        if self.filetype == '.tsv':
            self.delimiter = '\t'
        if self.filetype not in ['.csv', '.tsv']:
            print('Takes only CSV and TSV files')
            exit()

    def read_all_content(self, filename):
        self.filename = filename
        self.__verify_file_type()
        df = pd.read_csv(filename, sep=self.delimiter)
        return df

    def read_first_two_lines(self, filename):
        self.filename = filename
        self.__verify_file_type()
        df = pd.read_csv(filename, sep=self.delimiter)
        return df.head(2)

    def read_last_two_lines(self, filename):
        self.filename = filename
        self.__verify_file_type()
        df = pd.read_csv(filename, sep=self.delimiter)
        return df.tail(2)


if __name__ == '__main__':
    file = input('Enter the file name or path: ')
    while True:
        prompt = input('>>>Enter\n1 to readall\n2 to read first two\n3 to read last two')
        if prompt in ['1', '2', '3']:
            break
        else:
            print('Wrong option input')

    file_read = SpreadSheet()
    if prompt == '1':
        print(file_read.read_all_content(file))
    elif prompt == '2':
        print(file_read.read_first_two_lines(file))
    elif prompt == '3':
        print(file_read.read_last_two_lines(file))
