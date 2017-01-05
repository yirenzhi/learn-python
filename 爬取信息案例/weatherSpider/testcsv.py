import csv
def test():
    with open('test.csv','w',newline='') as csvfile:
        #spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        spamwriter = csv.writer(csvfile,dialect='excel')
        spamwriter.writerow(['Spam']*5+['Baked Beans'])
        spamwriter.writerow(['Spam','Lovely Spam','Wonderful Spam'])
        spamwriter.writerow({'AA','BB','CC'})

def test2():
    with open('test2.csv','w',newline='') as csvfile:
        fieldnames = ['first','second']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first':'Baked','second':'Beans'})
        writer.writerow({'first':'Lovely','second':'Spam'})
        writer.writerow({'first':'Wonderful','second':'Spam'})
        
    
test()
