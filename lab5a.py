#!/usr/bin/env python3
# Author ID: srivera8

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f1 = open(file_name, 'r')
    readf1 = f1.read()
    f1.close
    return readf1

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f2 = open(file_name, 'r')
    readf2 = f2.readlines()
    f2.close
    return [line.strip() for line in readf2 ]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))