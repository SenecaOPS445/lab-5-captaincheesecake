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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f3 = open(file_name, 'a')
    f3.write(string_of_lines)
    f3.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f4 = open(file_name, 'w')
    for line in list_of_lines:
        f4.write(line + '\n')
    f4.close()
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    fr = open(file_name_read, 'r')
    fw = open(file_name_write, 'w')
    line_number = 1
    for line in fr:
        fw.write(str(line_number) + ':' + line)
        line_number += 1
    fr.close()
    fw.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))