class Contact:
    begin='BEGIN:VCARD'
    version=''
    name=''
    fullname=''
    telephone=''
    end=''

    def __str__(self):
        return "{} {} {} {} {} {}\n".format(self.begin, self.version, self.name, self.fullname, self.telephone, self.end)
        
        
#with open('20150331224915.vcf') as f:
#    lines = f.readlines()
lines = [line.rstrip('\n') for line in open('20150331224915.vcf')]    

contactList=list()
for line in lines:
    #print(line, end = '')
    if line.startswith('BEGIN:VCARD'):
        oneContact=Contact()
        oneContact.begin=line
    if line.startswith('VERSION:'):
        oneContact.version=line
    if line.startswith('N:'):
        oneContact.name=line
    if line.startswith('FN:'):
        oneContact.fullname=line
    if line.startswith('TEL;CELL:'):
        oneContact.telephone=line
    if line.startswith('END:VCARD'):
        oneContact.end=line
        #print(oneContact, end='')
        contactList.append(oneContact)

for oneContact in contactList:
    print(oneContact, end='')
