#!/usr/bin/env python3
"""
Created on Wednesday May 5, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN 2º part
"""
import re
import csv
import nltk
import string

# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def reading_file(input_file):
  with open(input_file) as csv_file:
    punctuation_marks = string.punctuation + '…' + '”' + '“' + '-' + '‘'+ '’' + '´' + '—'
    csv_reader = csv.reader(csv_file, delimiter=',')
    list_of_rows = list(csv_reader)
    print(len(list_of_rows))
    text = 'Numero de documentos del corpus: ' + str(len(list_of_rows)) + '\n'
    writing_file('aprendizajeH.txt', text)
    writing_file('aprendizajeB.txt', text)
    writing_file('aprendizajeC.txt', text)
    writing_file('aprendizajeE.txt', text)


def writing_file(file_name, text):
  new_file = open(file_name,"wt")
  new_file.write(text)
  print("The file was successfully written! into \"" + file_name + "\" file\n")


def main():
  file = 'ecom-train.csv'
  reading_file(file)
  

main()