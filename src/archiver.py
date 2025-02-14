import os
import sys
import time
import tarfile

TMP_FOLDER = "tmp"
ARCHIVE_NAME = "files.tar.gz"
MAX_ARCHIVE_FILES = 10


def check_folder():
    if not os.path.exists(TMP_FOLDER):
        os.makedirs(TMP_FOLDER)


def count_files():
    return len(
        [
            name
            for name in os.listdir(TMP_FOLDER)
            if os.path.isfile(os.path.join(TMP_FOLDER, name))
        ]
    )


def archive_files():
    files = sorted(os.listdir(TMP_FOLDER))[
        :MAX_ARCHIVE_FILES
    ]  # Select only the first 10 files

    with tarfile.open(ARCHIVE_NAME, "w:gz") as tar:
        for filename in files:
            file_path = os.path.join(TMP_FOLDER, filename)
            if os.path.isfile(file_path):
                tar.add(file_path, arcname=filename)
                os.remove(file_path)
    print("files collected")


def create_files():
    check_folder()
    for i in range(10):
        file_path = os.path.join(TMP_FOLDER, f"file{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"This is file {i}\n")


def delete_files():
    for filename in os.listdir(TMP_FOLDER):
        file_path = os.path.join(TMP_FOLDER, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def monitor_folder(create_files_flag):
    check_folder()
    print(create_files_flag)
    if create_files_flag:
        create_files()

    if count_files() < 10:
        print("waiting for 10 files in {0} folder".format(TMP_FOLDER))

    while True:
        if count_files() >= 10:
            archive_files()
            delete_files()
            break
        time.sleep(1)


if __name__ == "__main__":
    create_files_flag = len(sys.argv) > 1 and sys.argv[1].lower() == "true"
    monitor_folder(create_files_flag)
