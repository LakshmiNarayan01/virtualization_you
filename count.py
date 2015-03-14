import re
def count_string(name):
    string = name
    f=open("you.txt")
    
    contents=f.read()
    #lost = int(re.findall(r"Lost = (\d+)", contents)[0])
    #lostTotal = contents.split('time=')[1].split(' ')[0]
    #list=['0ms']

    #list.append(lostTotal)
    #time=contents.split('
    f.close()
    print "Number of " +string +" in file",contents.count(string)
    #print lostTotal
    #print list

#count_string("Stevens")

count_string("Entertainment")
count_string("Comedy")
count_string("Travel & Places")
count_string("Sports")
count_string("People & Blogs")
count_string("Education")
count_string("people")

#count_string("no")

