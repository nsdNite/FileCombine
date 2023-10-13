# Python 3

import os


def create_list_of_txt_files() -> list:
    current_directory = os.getcwd()
    file_list = os.listdir(current_directory)
    txt_file_names = [file for file in file_list if os.path.isfile(file) and file.endswith(".txt")]

    return txt_file_names


def combine_files(input_file_list: list) -> None:
    output_file_name = "output.txt"
    try:
        with open(output_file_name, "w") as output_file:
            for input_file_name in input_file_list:
                with open(input_file_name, "r") as input_file:
                    output_file.write(input_file.read())
    except FileNotFoundError:
        print("One or more input files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Files have been successfully merged into output.txt")


if __name__ == "__main__":
    prompt = input("Please put txt files to merge into current folder \n"
                   "Please type start to start merging.")
    if prompt == "start":
        list_to_merge = create_list_of_txt_files()
        combine_files(list_to_merge)
        print("Success! Press enter to exit.")
        input()
    else:
        print("Program terminated")
