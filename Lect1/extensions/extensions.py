##input from user
str = input("Enter your file name with its extension for us to get its type: ")
def main(str):
    extension_type(str)
def extension_type(str):
    ## Split the extension from the file name and make a list
    str = str.split(".")
    #remove file name
    str.pop(0)
    #Check the extensions type in lists
    if str[0] in ["jpg", "jpeg", "png", "gif", "bmp"]:
        print(f"image/" + str[0])
    elif str[0] in ["txt", "md", "rtf"]:
        print(f"text/" + str[0])
    elif str[0] in ["mp3", "wav", "flac"]:
        print(f"audio/" + str[0])
    elif str[0] in ["mp4", "avi", "mkv", "mov"]:
        print(f"video/" + str[0])
    elif str[0] in ["pdf", "docx", "xlsx", "pptx"]:
        print(f"application/" + str[0])
    else:
        print("application/octet-stream")

main(str)