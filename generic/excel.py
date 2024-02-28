import openpyxl

class Excel:

    @staticmethod
    def get_data(xlpath,sheet,row,column):

        try:
            wb=openpyxl.load_workbook(xlpath)
            value=wb[sheet].cell(row,column).value
            print('data from xl',value)
            wb.close()
            return value
        except Exception as e:
            print(e)
            print('Exception while reading the data')
            return ""