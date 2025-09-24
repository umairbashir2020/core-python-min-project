file = open('file management/sample.txt','r')
content = file.read()
file.close()

print(f"content of sample.txt file : {content}")