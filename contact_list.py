from collections import OrderedDict

class ContactList():
    friends=[]
    work_buddies=[]
    friendsIWorkWith=[]
    def __init__(self,relstat,name,phoneNum):
        self.name=name
        self.PNum=phoneNum
        self.wrk=relstat
        obj={'name': self.name, 'number': self.PNum}
        if self.wrk== 'work':
            ContactList.work_buddies.append(obj)
        elif self.wrk=='both':
            ContactList.work_buddies.append(obj)
            ContactList.friends.append(obj)
        else: 
            ContactList.friends.append(obj)
        def getKey(obj):
            return obj['name']
        ContactList.friends.sort(key=getKey)
        ContactList.work_buddies.sort(key=getKey)
        for i in ContactList.friends:
            for j in  ContactList.work_buddies:
                if i['name'] == j['name']:
                     ContactList.friendsIWorkWith.append(i)
        ContactList.friends.sort(key=getKey)
    
#ContactList.friends= ContactList.friends.sort(key=['name'])
#The class has ended            


Fran=ContactList('friend', 'Fran', '555-555-5555')
Ed=ContactList('work', 'Ed', '455-555-5555')
Bart=ContactList('work', 'Bart', '355-555-5555')
Carl=ContactList('friend', 'Carl', '255-555-5555')
Dave=ContactList('friend', 'Dave', '155-555-5555')
Zack=ContactList('work', 'Zack', '655-555-5555')
Wack=ContactList('both', 'Wack', '755-555-5555')
print(ContactList.friendsIWorkWith)
print(ContactList.friends)
print(ContactList.work_buddies)
