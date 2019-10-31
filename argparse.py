import os
import argparse


def search_folder(folder_name):
    search_results = []
    for path, dirs, files in os.walk('/home/spartan/Downloads/test/'):
        if folder_name in dirs:
            search_results.append(path)
    return search_results


if __name__ == '__main__':
    f_name = 'hidden'
    result = search_folder(f_name)

    if len(result) != 0:
        for path in result:
            print(f'Folder {f_name} found at {path}')
    else:
        print('Folder not found')
