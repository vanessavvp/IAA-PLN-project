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


learning_b = {}
learning_c = {}
learning_e = {}
learning_h = {}
fav_cases_b = 0
fav_cases_c = 0
fav_cases_e = 0
fav_cases_h = 0
total_cases = 0
best_log = 0


def write_csv_file(file_name):
  with open(file_name, 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Descripcion', 'lPd en H', 'lPd en B', 'lPd en C', 'lPd en H', 'HBC o E'])


def find_log_word(lines):
  global total_cases, learning_b, learning_c, learning_e, learning_h
  string_log = 0.0
  for i in range(len(lines)):
    words = aprendizaje.preprocessing_words(lines[i][0])
    for word in words:
      if word in learning_b:
        string_log += learning_b[word]
      elif word in learning_c:
        string_log += learning_c[word]
      elif word in learning_e:
        string_log += learning_e[word]
      elif word in learning_h:
        string_log += learning_h[word]
    best_log = choose_best_log(string_log)
  print(best_log)


def choose_best_log(string_log):
  global learning_b, learning_c, learning_e, learning_h, best_log
  global total_cases, fav_cases_b, fav_cases_c, fav_cases_e, fav_cases_h
  bests_logs = []
  prob_b = fav_cases_b/total_cases
  prob_c = fav_cases_c/total_cases
  prob_e = fav_cases_e/total_cases
  prob_h = fav_cases_h/total_cases
  log_b = math.log(prob_b) + string_log
  log_c = math.log(prob_c) + string_log
  log_e = math.log(prob_e) + string_log
  log_h = math.log(prob_h) + string_log
  bests_logs.append(log_b)
  bests_logs.append(log_c)
  bests_logs.append(log_e)
  bests_logs.append(log_h)
  bests_logs.sort(reverse = True)
  return bests_logs[0]

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


def calculate_favorable_cases(file_name, fav_cases):
  file = open(file_name, 'r')
  first_line = (file.readline()).split()
  fav_cases = first_line[5]
  file.close()
  return int(fav_cases)


def main():
  global fav_cases_b, fav_cases_c, fav_cases_e, fav_cases_h, total_cases
  global learning_b, learning_c, learning_e, learning_h
  clasification_file = 'clasificacion_alu0101265704.csv'
  learning_b = cut_word_and_log('aprendizajeB.txt', learning_b)
  learning_c = cut_word_and_log('aprendizajeC.txt', learning_c)
  learning_e = cut_word_and_log('aprendizajeE.txt', learning_e)
  learning_h = cut_word_and_log('aprendizajeH.txt', learning_h)
  fav_cases_b = calculate_favorable_cases('aprendizajeB.txt', fav_cases_b)
  fav_cases_c = calculate_favorable_cases('aprendizajeC.txt', fav_cases_c)
  fav_cases_e = calculate_favorable_cases('aprendizajeE.txt', fav_cases_e)
  fav_cases_h = calculate_favorable_cases('aprendizajeH.txt', fav_cases_h)
  total_cases = fav_cases_b + fav_cases_c + fav_cases_e + fav_cases_h
  lines = aprendizaje.reading_file('copy.csv')
  find_log_word(lines)
  # vocabulario.delete_file_content(file_name)
  # write_csv_file(file_name)
  



main()