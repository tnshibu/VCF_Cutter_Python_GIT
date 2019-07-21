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
    fileNames = next(os.walk('input'))[2]
    for fileName in fileNames:
        process_one_file(fileName)
    
def process_one_file(fileName):
    lines = [line.rstrip('\n') for line in open('input/'+fileName)]    
    folderName='output/'+fileName
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    contactList=list()
    for line in lines:
        if line.startswith('BEGIN:VCARD'):
            oneContact=Contact()
        oneContact.innerlines.append(line)
        if line.startswith('END:VCARD'):
            contactList.append(oneContact)
    print('Total number of contacts ('+fileName+'): '+str(len(contactList)))
    for oneContact in contactList:
        writeOneContactToFile(folderName, oneContact)

#----------------------------------------------------------------------------------------------------        
def writeOneContactToFile(folderName, oneContact):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    
    fullName=''
    for line in oneContact.innerlines:
        #print(line, end = '\n')
        if line.startswith('FN:'):
            fullName=line[3:]
            fullName=fullName.replace('/','_')
    f = open(folderName+'/'+fullName+".vcf", 'w')
    for line in oneContact.innerlines:
        f.write(line+'\n')
    f.close()

#----------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------        
