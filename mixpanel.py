import pandas as pd

#read the excel file
file_name='mixpanel analysis dealers.xlsx'
def read_excel_file(filename=file_name):
    return pd.read_excel(io=filename, sheetname=None)

def analytics_function():
    mixpanel_data=read_excel_file()
    print mixpanel_data.keys()


if __name__ == '__main__':
    read_excel_file()
