def fileReader():
    '''reads from a text file'''
    with open("gdp.txt", "r") as fileObj:
        contents = fileObj.read().splitlines()
        print(contents)
        total =0
        for each in contents:
            total=total+int(each)
        print(total/len(contents))
        



        