f = open('/path/to/file/test.txt', 'r') # absolute path
print(f.read())
f.close()

f = open('testnewline.txt', 'w+') # read-only mode
f.write("This is a new line.")
f.close()

f = open('test3.txt', 'a+' ) # read & append mode
f.write("\nThis is a sixth line.") #<-- appending the new line
f.seek(0) # <-- resetting the cursor
print(f.read()) # <-- reading the file and printing it
f.close()

with open('test3.txt', 'a+' ) as f:
    f.write("\nThis is a seventh line.") #<-- appending the new line
    f.seek(0) # <-- resetting the cursor
    print(f.read()) # <-- reading the file and printing it

f = open('/path/to/file/test.txt', 'r') # absolute path
print(f.readlines())
f.close()

with open('/path/to/file', 'r' ) as f:
    for line in f.readlines():
        print(line.strip())

#For csv files "import csv" "import pandas as alternative"

with open('/path/to/file/', 'r') as f:
    for line in f.readlines():
        if 'ERROR' in line:
            message = line.strip().split(' - ')
            print(message)  # Print or process the extracted message

#outputing eror messages to a new file
error_messages = []
with open('/path/to/file', 'r' ) as f:
    for line in f.readlines():
        if 'ERROR' in line:
            date = line.strip().split(' - ')[0]
            error_type = line.strip().split(' - ')[1]
            message = line.strip().split(' - ')[2]
            error_messages.append(message)

with open('/path/to/new/file', 'w+') as f:
    for error in error_messages:
        f.write(error + '\n')

# Function to process log file and extract error messages
def process_log_file(log_filename, dest_filename):

    error_messages = []
    
    with open(log_filename, 'r' ) as f:
        for line in f.readlines():
            if 'ERROR' in line:
                date = line.strip().split(' - ')[0]
                error_type = line.strip().split(' - ')[1]
                message = line.strip().split(' - ')[2]
                error_messages.append(message)
    
    with open(dest_filename, 'w+') as f:
        for message in error_messages:
            f.write(message + '\n')
process_log_file('logs.txt', 'errors2.txt')