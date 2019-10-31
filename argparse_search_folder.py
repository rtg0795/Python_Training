import os
import argparse 
import psutil

parser = argparse.ArgumentParser(description='Search for a folder')
parser.add_argument('-f', '--folder', required=True, type=str, help='Folder name')
args = parser.parse_args()

def search_folder(folder_name):
    search_results = []
    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        mount_point = partition.mountpoint
        for path, dirs, files in os.walk(mount_point):
            print(path)
            if folder_name in dirs:
                search_results.append(path)
    return search_results


if __name__ == '__main__':
    result = search_folder(args.folder)
    if args.folder:
        if len(result) != 0:
            for path in result:
                print(f'Folder {args.folder} found at {path}')
        else: 
            print('Folder not found')
