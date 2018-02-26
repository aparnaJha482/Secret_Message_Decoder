import os


def decode_message():  # opening files in directory
    file_list=os.listdir(r"secretMessage")
    #print(file_list)
    saved_path = os.getcwd()
    print("current working directory is"+saved_path)
    os.chdir(r"secretMessage")
    saved_path=("new working directory is"+ saved_path)
    print("new working directory is" + saved_path)


decode_message()
