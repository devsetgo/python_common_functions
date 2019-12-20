from com_lib.reg_functions.patterns import pattern_between
from com_lib.file_functions import open_csv,save_json, save_csv
from tqdm import tqdm
import time
from unsync import unsync
import asyncio

def run_ascii():
    char_list = []
    char_list_csv =  open_csv('ascii2.csv')

    for c in char_list_csv:
        char = c["Symbol"]
        if char.isprintable() == True:
            char_list.append(char)

    err_list = []
    count = 0

    for l in tqdm(char_list, desc="left char", leave=False, ascii=True):
        for r in tqdm(char_list, desc="right char", leave=False, ascii=True):
            for s in tqdm(char_list, desc="split char", leave=False, ascii=True):
                # time.sleep(.001)
                loop_char = [l,r]                
                # print(f'l:{l}, r:{r}, s:{s}')
                if s not in loop_char:
                    text = f"{s}{l}found one{r}{s}{s}{l}found two{r}"
                    data = pattern_between(text,l,r,s)
                    # data = call_pattern(l,r,s)
                    count += 1
                    
                    if "Error" in data:
                        err_list.append(data)
    
    # tasks = [non_async_function(0.1) for _ in range(10)]
    # print([task.result() for task in tasks])
    
    return err_list, char_list, count




if __name__ == "__main__":
    t0 = time.time()
    err_list, char_list,count = run_ascii()
    t1 = time.time() - t0
    combinations = len(char_list) * len(char_list) * len(char_list)
    print(f'process took {t1:.2f} seconds with {combinations:,} combinations and a count cycle of {count:,}')
    if len(err_list) != 0:
        save_json('err.json', err_list)
    else:
        print('there were no errors')
