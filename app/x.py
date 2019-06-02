from com_lib.file_functions import (
    open_json,
    open_csv,
    create_sample_files,
    get_data_directory_list,
)


y = 0
for i in range(0,10):
    file_name = 'sample.json'
    x = open_json(file_name)
    y += len(x)

print(y)