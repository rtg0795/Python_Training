import os

def search_folder(folder_search, where):
    for root, dirs, files in os.walk(where):
        if folder_search in dirs:
            yield root


if __name__ == '__main__':
    flag = False
    result = search_folder('hidden', '/home/spartan/Downloads/test/')
    for path in result:
        flag = True
        print(path)
    if not flag:
        print('Folder nor found!')


