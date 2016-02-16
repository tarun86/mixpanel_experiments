import pandas as pd

#read the excel file
file_name='mixpanel analysis dealers.xlsx'
def read_excel_file(filename=file_name):
    print filename
    return pd.read_excel(io=filename, sheetname=None)

if __name__ == '__main__':
    read_excel_file()
