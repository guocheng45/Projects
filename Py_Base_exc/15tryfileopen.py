try:
    with open("myfile.txt") as fh:          # 用了with就不用关闭文件，Python会帮忙关闭
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print("file is not exist")
