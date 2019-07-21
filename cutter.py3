import os

#----------------------------------------------------------------------------------------------------        
class Contact:
    
    def __init__(self):
        self.innerlines=list()

    def __str__(self):
        str=''
        for line in self.innerlines:
            str=str+line+','
        return str
#----------------------------------------------------------------------------------------------------        
def main():        
    lines = [line.rstrip('\n') for line in open('input/20150331224915.vcf')]    
    
    contactList=list()
    for line in lines:
        if line.startswith('BEGIN:VCARD'):
            oneContact=Contact()
        oneContact.innerlines.append(line)
        if line.startswith('END:VCARD'):
            contactList.append(oneContact)
    print('Total number of contacts : '+str(len(contactList)))
    for oneContact in contactList:
        writeOneContactToFile(oneContact)

#----------------------------------------------------------------------------------------------------        
def writeOneContactToFile(oneContact):
    if not os.path.exists('output'):
        os.makedirs('output')
    
    for line in oneContact.innerlines:
        #print(line, end = '\n')
        if line.startswith('FN:'):
            fullName=line[3:]
    f = open('output/'+fullName+".vcf", 'w')
    for line in oneContact.innerlines:
        f.write(line+'\n')
    f.close()

#----------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------        
