"""my Diary Application"""

from diary import add_entry, read_entries


def main():
  print ('Diary Application')
  # The user chooses a file to save or read diary entries.
  filename = input('Enter diary filename: ')

  # The user chooses a date to write or read diary entries.
  entry_date = input('Enter date (MM-DD-YYYY): ')

  while True:
    print('1- add entey')
    print('2- read entries')
    print('3- exit')

    choice = input('enter your choice: ')

    if choice == "1":
      add_entry(filename, entry_date)      
    elif choice =='2':
      read_entries(filename, entry_date)
    elif choice =='3':
      break
    else:
      print('Invalid chouce. try again.')
       

if __name__ == '__main__':
  main()