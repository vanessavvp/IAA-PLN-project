#!/usr/bin/env python3
"""
Created on Friday May 7, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN final part
"""
import re
import csv
import math
import nltk
import string
import vocabulario
import aprendizaje


clasification_file = 'clasificacion_alu0101265704.csv'
summary_file = 'resumen_alu0101265704.csv'
solution_summary = []
logs_value = {}
learning_b = {}
learning_c = {}
learning_e = {}
learning_h = {}
fav_cases_b = 0
fav_cases_c = 0
fav_cases_e = 0
fav_cases_h = 0
total_cases = 0
input_code = 0
test_file = ''
solution = []


def write_csv_file(file_name, info_list):
  with open(file_name, 'at', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(info_list)


def log(lines):
  global learning_h, learning_b, learning_c, learning_e
  global fav_cases_h, fav_cases_b, fav_cases_c, fav_cases_e
  global solution, solution_summary
  for i in range(len(lines)):
    # Adding description to the clasification file
    aux = []
    words = aprendizaje.preprocessing_words(lines[i][0])
    description = ' '.join(words)
    aux.append(description)
    solution.append(aux)

    # Calculating log probs for each learning dictionary 
    log_h = calculate_log_sentences(words, learning_h, fav_cases_h)
    logs_value['H'] = log_h
    log_b = calculate_log_sentences(words, learning_b, fav_cases_b)
    logs_value['B'] = log_b
    log_c = calculate_log_sentences(words, learning_c, fav_cases_c)
    logs_value['C'] = log_c
    log_e = calculate_log_sentences(words, learning_e, fav_cases_e)
    logs_value['E'] = log_e
    solution[i].append(log_h)
    solution[i].append(log_b)
    solution[i].append(log_c)
    solution[i].append(log_e)

    # Choosing the best log prob
    best_value_key = max(logs_value.keys(), key=(lambda k: logs_value[k]))
    solution[i].append(str(best_value_key))
    solution_summary.append(str(best_value_key))
  write_csv_file(clasification_file, solution)
  write_csv_file(summary_file, solution_summary)


def request_file_code():
  global test_file, input_code, summary_file
  global solution_summary
  test_file = input('Introduce test file: ')
  input_code = input('Introduce code: ')
  text = 'codigo: ' + input_code
  f = open(summary_file, 'w')
  f.write(text)
  f.close()
  

def calculate_log_sentences(words, learning, fav_cases):
  # Adds the logarithm of the probability for each of the words in a specific class
  global total_cases
  sentence_log = 0.0
  for word in words:
    if word in learning:
      sentence_log += learning[word]
    else:
      sentence_log += learning["<UNK>"]
  class_log_prob = math.log(fav_cases / total_cases)
  total_log_sentence = sentence_log + class_log_prob
  return round(total_log_sentence, 2)


def cut_word_and_log(file_name, learning):
  file = open(file_name, 'r')
  file.readline()
  file.readline()
  for line in file:
    words = line.split()
    if words[1] not in learning:
      learning[words[1]] = float(words[5])
  file.close()
  return learning


def cut_favorable_cases(file_name, fav_cases):
  file = open(file_name, 'r')
  first_line = (file.readline()).split()
  fav_cases = first_line[5]
  file.close()
  return int(fav_cases)


def main():
  global fav_cases_b, fav_cases_c, fav_cases_e, fav_cases_h, total_cases
  global learning_b, learning_c, learning_e, learning_h
  global test_file, clasification_file, summary_file
  vocabulario.delete_file_content(clasification_file)
  vocabulario.delete_file_content(summary_file)
  learning_b = cut_word_and_log('aprendizajeB.txt', learning_b)
  learning_c = cut_word_and_log('aprendizajeC.txt', learning_c)
  learning_e = cut_word_and_log('aprendizajeE.txt', learning_e)
  learning_h = cut_word_and_log('aprendizajeH.txt', learning_h)
  fav_cases_b = cut_favorable_cases('aprendizajeB.txt', fav_cases_b)
  fav_cases_c = cut_favorable_cases('aprendizajeC.txt', fav_cases_c)
  fav_cases_e = cut_favorable_cases('aprendizajeE.txt', fav_cases_e)
  fav_cases_h = cut_favorable_cases('aprendizajeH.txt', fav_cases_h)
  total_cases = fav_cases_b + fav_cases_c + fav_cases_e + fav_cases_h
  request_file_code()
  lines = aprendizaje.reading_file(test_file)
  log(lines)

  
main()