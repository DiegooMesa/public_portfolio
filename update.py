import os
def get_file_names(directory):
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".html"):
                if filename not in blacklist:
                    files.append(filename)
    print("Files in " + directory + " : " + str(files))
    return files

def file_mod (directory, files, boilerplate):
    for file in files:
        #Open file to be modified in order to get current code
        old_file = open(directory + file, "r")
        old_file_read = old_file.read()
        old_file.close()
        
        #Replace boilerplate with new one
        new_file = open(directory + file, "w")
        new_file.write(boilerplate + old_file_read.split("<!--Boilerplate-->")[1])
        new_file.close()
        
        print("File: " + file + " modified.")

#Define blacklist
blacklist = ["index.html", "boilerplate.html"]

#Get main files and article files
main_files = get_file_names("./main/")
articles_projects = get_file_names("./projects/")

#Get boilerplate
boilerplate = open("boilerplate.html")
boilerplate = boilerplate.read()

file_mod("./main/", main_files, boilerplate)
file_mod("./projects/", articles_projects, boilerplate)