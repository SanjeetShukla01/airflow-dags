import logging
import os
import socket


def read_file_and_log_content(file_path):

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
    # https: // filesamples.com / samples / document / txt / sample3.txt
