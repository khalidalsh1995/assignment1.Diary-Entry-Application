"""function for diary entries."""


# This function save the user's text and date in the file. 
def add_entry(filename, entry_date):
    input_text = input ("write your entry: ")

    with open(filename, 'a') as f:
        f.write(f'{entry_date} | {input_text}\n')

    print('entry saved.')



# This function chock each line's date and print lines with same date.
def read_entries(filename, entry_date):
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Take only the first part of the line (the date).
                saved_date = line.split(' | ')[0]
                
                if saved_date == entry_date:
                    print(line, end='')
            
    except OSError:
        print('cannot open the diary file.')