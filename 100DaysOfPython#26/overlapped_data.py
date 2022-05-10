with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#26/file1.txt") as file1:
    file1_list = []
    for num in file1:
        num = int(num.rstrip())
        file1_list.append(num)
with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#26/file2.txt") as file2:
    file2_list = []
    for num in file2:
        num = int(num.rstrip())
        file2_list.append(num)

overlapped_data_list = [num for num in file1_list if num in file2_list]
print (overlapped_data_list)