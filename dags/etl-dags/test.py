import logging
import os
import socket
import urllib.request


def download_file(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded successfully to: {save_path}")
    except Exception as e:
        print(f"Failed to download file from {url}: {e}")


def read_file_and_log_content(file_path):

    url = "https://filesamples.com/samples/document/txt/sample3.txt"  # URL of the file to download
    save_path = "/home/executor/sample3.txt"  # Path to save the downloaded file
    download_file(url, save_path)

    cwd = os.getcwd()
    print(f"++++++++++++++++\n {socket.gethostname()} \n++++++++++++++")
    print(f"+++++++++++++\n {cwd} \n++++++++++++")
    logging.info("++++++++++++++++++++")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"File content:\n {content} \n+++++++++++++++++++++++++++++++++")
    except FileNotFoundError:
        logging.error("File not found at path: %s", file_path)


if __name__ == '__main__':
    file_path = '/home/executor/sample3.txt'
    read_file_and_log_content(file_path)
