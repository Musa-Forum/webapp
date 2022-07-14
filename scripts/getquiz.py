import openpyxl
import sys

args = sys.argv
# ブックを取得
book = openpyxl.load_workbook("../../../../../Musaforum/展示コレクション.xlsx")
# シートを取得 
sheet = book['ミラー_コレクション一 74008042a74b4fd487b']

number = int(args[1])

if __name__ == '__main__':
    # セルを取得
    japanese_name = sheet['A%d' % (number)].value
    quiz = sheet['C%d' % (number)].value
    choice1 = sheet['D%d' % (number)].value
    choice2 = sheet['E%d' % (number)].value
    choice3 = sheet['F%d' % (number)].value
    answer = sheet['G%d' % (number)].value
    code_name = sheet['AA%d' % (number)].value
    row = [quiz,choice1,choice2,choice3,answer,japanese_name,code_name]
    row = [str(i) for i in row]
    sys.stdout.write(",".join(row))

