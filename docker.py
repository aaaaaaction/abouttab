import os
import sys


def pull(image,times):
    count = 0
    while count < int(times):
        result = os.system(f"docker pull {image}")
        count += 1
        if result == 0:
            break


def push(image):
    while True:
        result = os.system(f"docker push {image}")
        if result == 0:
            break


def main():
    image = sys.argv[1]
    command = sys.argv[2]
    if command == "pull":
        pull(image,sys.argv[3])
    else:
        push(image)