# -*- coding: utf-8 -*-
import unittest


from com_lib.reg_functions.patterns import pattern_between_two_char
from com_lib.file_functions import open_csv
from tqdm import tqdm

class Test(unittest.TestCase):
    def test_pattern_between_two_char(self):
        char_list = []
        char_list_csv = open_csv("ascii2.csv")

        for c in char_list_csv:
            char = c["Symbol"]
            if char.isprintable() == True:
                char_list.append(char)
        # print(len(char_list))
        err_list = []
        count = 0

        for l in tqdm(char_list, desc="left char", leave=False, ascii=True):
            for r in tqdm(char_list, desc="right char", leave=False, ascii=True):
                # for s in tqdm(char_list, desc="split char", leave=False, ascii=True):
                # time.sleep(.0005)
                # loop_char = [l, r]
                # print(f'l:{l}, r:{r}, s:{s}')
                # if s not in loop_char:
                text = f"{l}found one{r} {l}found two{r}"
                data = pattern_between_two_char(text, l, r)
                # data = call_pattern(l,r,s)
                # count += 1

                if "Error" in data:
                    err_list.append(data)


        assert len(err_list) == 0

 