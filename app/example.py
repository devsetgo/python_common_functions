from com_lib.file_processing import open_json, create_sample_files


def get_data():
    
    filename = f'bob'
    try:
        x = open_json(filename)
        print(len(x))
    except Exception as e:
        print(e)

def make_sample():
    filename = 'sample'
    sample_size = 1000
    result = create_sample_files(filename, sample_size)
    
if __name__ == '__main__':
    get_data()
    make_sample()