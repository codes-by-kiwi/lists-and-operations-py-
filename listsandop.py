m = object() #returns an empty object.
n = object()

m_list = [m] * 10 #contains 10 instances of the variables m 
n_list = [n] * 10 #contains 10 instances of the variables n
final = m_list + n_list #combines both lists 

print("m_list contains %d objects" % len(m_list)) #len function tells the no of elements in a list 
print("n_list contains %d objects" % len(n_list)) 
print("final contains %d objects" % len(final))

if m_list.count(m) == 10 and n_list.count(n) == 10: #if m_list has 10 instances of m and n_list has 10 instances of n
    #then the following coded is executed  
    #count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.
    print("About to get to the finish line...")
if final.count(m) == 10 and final.count(n) == 10: #if final has 10 instances of m and 10 instances of n then 
    #the work is done 
    print("Great.You reached the end!")