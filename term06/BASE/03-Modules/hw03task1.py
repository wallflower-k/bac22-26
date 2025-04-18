import argparse
import os 
from docx import Document
import string

parser = argparse.ArgumentParser(description='Посчитаем количество слов в документе!')
parser.add_argument('file_path', help='Введите путь к файлу')
args = parser.parse_args()
doc = Document(os.path.abspath(args.file_path))
tx = ''
for i in doc.paragraphs:
    tx += i.text 
for x in string.punctuation:
    if x in tx:
        tx = tx.replace(x, '')
lst = tx.split()
print(len(lst))

# ввела в командную строку: python hw03task1.py files/Сухонина_Аннотация_3-й_курс.docx
# и сработало, напринтил 306