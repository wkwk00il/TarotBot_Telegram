from random import choices
import openpyxl


wb = openpyxl.reader.excel.load_workbook(filename='love.xlsx')
wb.active = 0

sheet = wb.active


def pick_love_card():
    numb = choices([int(i) for i in range(2, 81)], k=4)
    c1 = '\u2660'+' '+f'<b>Текущее положение дел:</b>\n' + 'выпала карта '+'"'+sheet[f'A{numb[0]}'].value+'"'+'\n'+ '\U0001F4AC'+' '+f'<b>Она означает:</b>\n'+sheet[f'B{numb[0]}'].value+'\n\n'
    c2 = '\u2660'+' '+f'<b>Причины вашего беспокойства:</b>\n' + 'выпала карта ' + '"'+sheet[f'A{numb[1]}'].value+'"' + '\n' + '\U0001F4AC'+' '+f'<b>Она означает:</b>\n' + sheet[f'C{numb[1]}'].value+'\n\n'
    c3 = '\u2660'+' '+f'<b>Отношение любимого человека:</b>\n' + 'выпала карта ' + '"'+sheet[f'A{numb[2]}'].value+'"' + '\n' +'\U0001F4AC'+' '+ f'<b>Она означает:</b>\n' + sheet[f'D{numb[2]}'].value+'\n\n'
    c4 = '\u2660'+' '+f'<b>Совет Оракула:</b>\n' + 'выпала карта ' + '"'+sheet[f'A{numb[3]}'].value+'"' + '\n' +'\U0001F4AC'+' '+ f'<b>Она означает:</b>\n' + sheet[f'E{numb[3]}'].value+'\n\n'
    return f'{c1}{c2}{c3}{c4}'

