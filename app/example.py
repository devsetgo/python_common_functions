from com_lib.file_processing import (
    open_json,
    open_csv,
    create_sample_files,
    get_data_directory_list,
)


def get_data():
    filename: str = "test_1.json"
    try:
        result: dict = open_json(filename)
    except Exception as e:
        print(e)


def make_sample():
    filename: str = "sample"
    sample_size: int = 1000
    try:
        result = create_sample_files(filename, sample_size)
    except Exception as e:
        print(e)


def dir_list():
    directory: str = "json"
    try:
        directory_list: list = get_data_directory_list(directory)
    except Exception as e:
        print(e)

    try:
        for i in directory_list:
            result: dict = open_json(i)
            count = 0
            for n in result:
                x = n['name']
                count += 1
            print(count)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_data()
    make_sample()
    dir_list()
