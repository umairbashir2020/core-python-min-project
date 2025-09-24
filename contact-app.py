contacts ={} 

def main():
    while True:
        print('\nContact Book App')
        print('1. Create contact')
        print('2. View contact')
        print('3. Update contact')
        print('4. Delete contact')
        print('5. Search contact')
        print('6. Count contact')
        print('7. View contact list')
        print('8. Exit')

        choice = int(input('Enter your choice = '))
        # choose 1 to create new contact
        if choice == 1: 
            name = input('Enter your contact name .. ')

            if name in contacts:
                print(f"Contact name {name} already exists!")
            else:
                age = input("Enter age = ")
                mobile = input("Enter mobile number = ")
                email = input('Enter email  = ')
                contacts[name] ={ 'age' :int(age) , 'mobile': mobile, "email": email}

        # choose 2 to view specific contact
        if choice == 2:
            name = input("Enter you contact name = ")
            if name in contacts:
                contact =contacts[name]
                print(f"Name: {name} , Age:{age} , mobile:{mobile} ")
            else:
                print('Contact not found!')
        
        # choose 3 to update the contact
        if choice == 3:
            name= input("Enter contact name you want to update = ")
            if name in contacts:
                new_name =input('Enter New Name = ')
                age = input("Enter updated age = ")
                mobile = input("Enter updated mobile number = ")
                email = input('Enter updated email  = ')
                
                contacts[new_name] ={
                    'age' :int(age),
                    'mobile': mobile,
                    "email": email
                }
                # remove old entry if name was changed
                if name != new_name:
                    del contacts[name]
                
                print('Contact has been updated successflly!')
            else:
                print('Contact not found!')

        # choose 4 to delete the contact
        if choice == 4:
            name = input("Enter contact name you want to delete = ")
            if name in contacts:
                del contacts[name]
                print(f'Contact {name} has been deleted successsfully!')
            else:
                print("Contact not found!")

        # choose 5 to search a contact
        if choice == 5:
            search_name =input("Enter name you want to search ...")
            found = False
            for name, contact in contacts.items():
                if search_name.lower() in name.lower():
                    print(
                        f"Found - Name: {name}, "
                        f"Age: {contact['age']}, "
                        f"Mobile: {contact['mobile']}, "
                        f"Email: {contact['email']}"
                    )
                    found = True
            if not found:
                print('No contact fount with that name')

        # choose 6 to count contacts in the book contact
        if choice == 6:
            print(f"Total contacts in your book : {len(contacts)}")

        # choose 7 to display contact list
        if choice == 7:
            print(f'List of contacts .. {contacts}')
            break
        
        # choose 8 to terminate the program
        if choice == 8:
            print('Closing the executions ..')
            break


main()

