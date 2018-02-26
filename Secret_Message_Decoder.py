import os


def decode_message():  # opening files in directory
    file_list=os.listdir(r"secretMessage")
    #print(file_list)
    saved_path = os.getcwd()
    # print("current working directory is" +saved_path)
    os.chdir(r"secretMessage")
    saved_path=("new working directory is" + saved_path)
    # print("new working directory is" + saved_path)

    #renaming file
    for file_name in file_list:
        old_name = file_name
        new_name = file_name.1strip("123456789")
        print("Old Name:"+ old_name)
        print("New Name:"+ new_name)

decode_message()
