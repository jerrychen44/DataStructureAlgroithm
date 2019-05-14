import os





'''

Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h



Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Here is some code for the function to get you started:

'''
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    rst = []
    if suffix == None or path == None:
        return []
    if len(suffix) == 0 or len(path) == 0:
        return []

    helper(suffix, path,rst)
    #print('rst:',rst)
    return rst



def helper(suffix,path,rst):
    #print(suffix,path)
    #print (os.listdir(path))

    for item in os.listdir(path):
        #print('item:',item)
        nextpath = path +'/' +item
        is_folder = os.path.isdir(nextpath)
        #print(is_folder)
        if is_folder == True:
            #print(nextpath)
            helper(suffix,nextpath,rst)
        else:#is file
            if suffix in item:
                if (path + '/' + item).endswith(".c"):
                    rst.append(path + '/' + item)



def local_test():
    # Let us print the files in the directory in which you are running this script
    print (os.listdir("."))

    # Let us check if this file is indeed a file!
    print (os.path.isfile("./ex.py"))

    # Does the file end with .py?
    print ("./ex.py".endswith(".py"))


#local_test()

print(find_files('b', '.'))
#output: ['./testdir/subdir3/subsubdir1/b.c']


print(find_files('b', ''))
#output:[]

print(find_files('b', './testdir/subdir5'))
#output:[]
