# reading
path = "relative/path/to/file.txt"
with open(path, 'r') as f:
    print(f.read())  # read the whole file
    print(f.readlines()) # read the whole file and return a list of lines
    print(f.read().splitlines()) # read the whole file and return a list of lines without the new line character
# ==================================================================================================== 
# writing
# overwrite the file and if the file doesn't exist, it will be created
with open(path, 'w') as f:
    f.write('Hello World')
# append to the file and if the file doesn't exist, it will be created
with open(path, 'a') as f:
    f.write('Hello World')
# if the file exists, then error will be raised
with open(path, 'x') as f:
    f.write('Hello World')
# ====================================================================================================
