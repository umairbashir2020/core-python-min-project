import os
print("Current working directory:", os.getcwd()) # current dir
# create file 
def create_file(filename):
    try:
        with open(filename,'x') as f:  # 'x' mode creates a new file
            print(f"file name {filename}: created successfully! ")

    except FileExistsError:
        print(f"file name {filename} already exists!")

    except Exception as e:
        print("An error occured!")

#  show all files name 
def display_all_files():
    files =os.listdir()  # list all files in the current directory
    if not files:
        print('Files not found!')
    else:
        print("File in directory!")
        for file in files:
            print(file)

# delete a file 
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} has been deleted successfully!")

    except FileNotFoundError:
        print(f'File {filename} not found!')

    except Exception as e:
        print('An error occured!')

# read file 
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"content of file {filename} :\n{content}")

    except FileNotFoundError:
        print(f"file {filename} does't exist!")

    except Exception as e:
        print('An error occured!')

# edit file
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"content added to {filename} successfully!")
    
    except FileNotFoundError:
        print(f"file {filename} does't exist!")

    except Exception as e:
       print('An error occured!')

# call main function to execute a specific function 
def main():
    while True:
        print("\nFile Management App")
        print('1 - Create file')
        print('2 - Display file')
        print('3 - Delete file')
        print('4 - Read file')
        print('5 - Edit file')
        print('6 - Exit')

        choice = int(input("Please your choice (1-6) = "))
        if choice == 1:
            filename =input("Enter file name to create = ")
            create_file(filename)
        
        elif choice == 2:
            display_all_files()

        elif choice == 3:
            filename =input("Enter file name to delete it = ")
            delete_file(filename)
        
        elif choice == 4:
            filename = input('Enter file name to read = ')
            read_file(filename)

        elif choice == 5:
            filename = input('Enter file name to edit = ')
            edit_file(filename)

        elif choice == 6:
            print('Closing the App ...')
            break

        else:
            print('In-valid syntax!')


main()
        

