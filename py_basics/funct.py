#{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}
#return (list(zip(l1,l2)))   do using map
def cross():   
    l1 = [1,2,3]
    l2 = ["a","b","c"]
    cross = list(map(lambda x,y:(x,y),(l1,l2)))
    print (cross)
    
 
#to take a list of years and return a list of only leap years    
def leap_year():

    g = lambda x: (x%4 == 0 and x%100 != 0) or (x%4 == 0 and x%100 == 0 and x%400 ==0)
    years_list = [1977, 1982, 2000, 2400, 1992, 1996, 1967, 1900, 2200]
    leap_years = list(filter(g, years_list))        
    print (leap_years)
    
#convert soln to using list comprehensions
    leap_years = [ x for x in years_list if g(x)]   #can also just type the condition here

#os.listdir(path) Return a list containing the names of the entries in the directory given by path. 
#no order, does not include the special entries '.' and '..' even if they are present in the directory.
#files = filter(lambda x: x and x[0] != '.', os.listdir(folder))
# returns all files or folders that don't begin with "."
# ie. all files and folders


#
def fileclean(file_name):
    file = open(file_name)
    mode = int(input("enter 1 if you want to create new file, enter 2 if you want to overwrite existing file "))
    if  mode == 1:
        new_file = input("enter new file name ")    
        file2 = open(new_file,'w')
        for line in file:   
            line = line.strip()
            file2.write(line)
        file2.close()
    else:
        text = ""
        for line in file:   
            line = line.strip()
            text = text + line
        file = open(file_name,'w')
        file.write(text)
    file.close()
        
     #Then convert soln to using list comprehensions   ????
def fileclean2(file_name):
    
    mode = int(input("enter 1 if you want to create new file, enter 2 if you want to overwrite existing file "))
    if  mode == 1:
        file = open(file_name)
        new_file = input("enter new file name ")    
        file2 = open(new_file,'w')     
        [file2.write(line.strip()) for line in file]
        file2.close()
    else:
        file = open(file_name,'w')
        [file.write(line.strip()) for line in file]       #file not open for reading and writing same time
        text = [line.strip() for line in file]          #this returns a list, not str
        file.write(text)
    file.close()
    
# exercise for map function on functions instead of seq
