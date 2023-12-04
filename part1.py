# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:04:37 2023

@author: zheng
"""

import re

if __name__ == "__main__":
    # Input file
    input_file_path = 'input.txt'
    
    # Read the input file 
    string_array = []
    with open(input_file_path, 'r') as file:
            string_array = file.readlines()
    
    # 1. adding up all numbers first
    string_array_all_num =  [re.sub(r'[^\w\s]+', ' ', text) for text in string_array]
    all_sum = 0
    for i in range(len(string_array_all_num)):
        numbers = re.findall(r'\d+', string_array_all_num[i])
        numbers = [int(num) for num in numbers]
        # print(sum(numbers))
        all_sum += sum(numbers)
        
    # 2. add a 3x3 "&&&;&&&;&&&" mask centered at each symbol
    # creating a 1D mask within each line: *&* --> &&&
    string_array_1d_masked =  [re.sub(r'.[^\w\s.].', '&&&', text) for text in string_array]
    
    # with open('mask1.txt', 'w') as file:
    #     for line in string_array_1d_masked:
    #         file.write(line)
            
    # not proud of this part; there is probably some 2d regex library
    char_array_2d_masked = [list(string) for string in string_array_1d_masked]
    for i in range(len(string_array)):
        for j in range(len(string_array[i])):
            if string_array_1d_masked[i][j] == "&":
               char_array_2d_masked[i-1][j] = "&"
               char_array_2d_masked[i+1][j] = "&"
    # rejoin the char array back to a string array
    string_array_2d_masked = [''.join(row) for row in char_array_2d_masked]
    
    # with open('mask2.txt', 'w') as file:
    #     for line in string_array_2d_masked:
    #         file.write(line)
            
    masked_sum = 0
    for i in range(len(string_array_all_num)):
        numbers = re.findall(r'\d+', string_array_all_num[i])
        original_digits = [int(num) for num in numbers]
        numbers = re.findall(r'\d+', string_array_2d_masked[i])
        masked_digits = [int(num) for num in numbers]
        non_part_num_digits = list(set(original_digits) & set(masked_digits))
        
        masked_sum += sum(non_part_num_digits)
    
    
    print(all_sum - masked_sum)