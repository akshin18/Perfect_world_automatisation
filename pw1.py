import pyautogui
from time import sleep
import keyboard
import mouse
# im = pyautogui.screenshot('ha.png',region=(1390,32,524,510))
import pytesseract
import os
from PIL import Image
import shutil
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

moyemu = 0
current_balance = 4500000

shutil.rmtree('pht/')
os.mkdir('pht')

for i in range(7):
    left = pyautogui.screenshot(f'pht\\left{str(i)}.png', region=(1490, 119+(i+1)*35, 68, 20))
    right = pyautogui.screenshot(f'pht\\right{str(i)}.png', region=(1741, 117+(i+1)*35, 69, 20))
c= []

left_count = len([x for x in os.listdir('pht\\') if 'left' in x])
right_count = len([x for x in os.listdir('pht\\') if 'right' in x])

for i in range(max([left_count,right_count])):
    c.append([])

print(c)

for i in range(len(c)):
    a = ''
    for zi in pytesseract.image_to_string(f'pht\\left{i}.png').split('\n')[0]:
        try:
            a = a+ str(int(zi))
        except:pass
    b = ''
    for zi in pytesseract.image_to_string(f'pht\\right{i}.png').split('\n')[0]:
        try:
            b = b + str(int(zi))

        except:
            pass


    c[i].append([str(a),str(b)])

b = [i for i in c if i[0][0] != '' and i[0][1] != '']
for i in b:
    print(i)


if b[-1][0][1] != '':
    if b[-1][0][1] != str(moyemu):
        pass
else:
    if b[-1][0][0] != str(moyemu):
        pass
