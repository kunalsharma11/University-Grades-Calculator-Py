'''
Created on May 18, 2018

@author: Kunal Sharma
'''
import copy

class DataCalculations(object): 
    
    def __init__(self, classlist, g):
        
        self.classlist = classlist
        self.g = g
        
    
    def AvailableOptions(self,option):
        spaces = '{:<6}{:<14}{:14}'
        newvar = ''
        if(option.lower() == "a1"):
            print("A1    grades    "+self.classlist.a1)
            for stud in self.classlist.clist:
                if stud.a1 =='0':
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, newvar))
                else:
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, stud.a1))                        
        elif(option.lower() == "a2"):
            print("A2    grades    "+self.classlist.a2)
            for stud in self.classlist.clist:
                if stud.a2 =='0':
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, newvar))
                else:
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, stud.a2))
        elif(option.lower() == "t1"):
            print("T1    grades    "+self.classlist.t1)
            for stud in self.classlist.clist:
                if stud.t1 =='0':
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, newvar))
                else:
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, stud.t1))                       
        elif(option.lower() == "t2"):
            print("T2    grades    "+self.classlist.t2)
            for stud in self.classlist.clist:
                if stud.t2 =='0':
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, newvar))
                else:
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, stud.t2))                       
        elif(option.lower() == "project"):
            print("Project    grades    "+self.classlist.proj)
            for stud in self.classlist.clist:
                if stud.proj =='0':
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, newvar))
                else:
                    print(spaces.format(stud.sid, stud.lname+","+stud.fname, stud.proj))                        
        else:
            print("Option not found. Please choose again")
            self.g.showData()

    def ComponentAverage(self,option):
        if(option.lower() == "a1"):
            total=0
            for stud in self.classlist.clist:
                total+=int(stud.a1)
            print("A1 Average: "+str(round(total/len(self.classlist.clist),2))+"/"+self.classlist.a1)
        elif(option.lower() == "a2"):
            total=0
            for stud in self.classlist.clist:
                total+=int(stud.a2)
            print("A2 Average: "+str(round(total/len(self.classlist.clist),2))+"/"+self.classlist.a2)
        elif(option.lower() == "t1"):
            total=0
            for stud in self.classlist.clist:
                total+=int(stud.t1)
            print("T1 Average: "+str(round(total/len(self.classlist.clist),2))+"/"+self.classlist.t1)
        elif(option.lower() == "t2"):
            total=0
            for stud in self.classlist.clist:
                total+=int(stud.t2)
            print("T2 Average: "+str(round(total/len(self.classlist.clist),2))+"/"+self.classlist.t2)
        elif(option.lower() == "project"):
            total=0
            for stud in self.classlist.clist:
                total+=int(stud.proj)
            print("Project Average:"+str(round(total/len(self.classlist.clist),2))+"/"+self.classlist.proj)
        else:
            print("Option not found. Please choose again")
            self.g.showData()
                   
    def StandardReport(self):
        newlist=sorted(self.classlist.clist, key=lambda Student:Student.sid)
        StudData='{:<9}{:<9}{:10}{:10}{:<9}{:<9} {:<9} {:<9} {:<15} {:<9}'
        print(StudData.format('ID','LN','FN','a1','a2','t1','t2','Project','total','GR'))
        newvar = ''
        newlistcopy =copy.deepcopy(newlist)
        for stud in newlistcopy:
            if stud.a1== '0':
                stud.a1= newvar
            if stud.a2== '0':
                stud.a2= newvar
            if stud.t1== '0':
                stud.t1= newvar
            if stud.t2== '0':
                stud.t2= newvar
            if stud.proj== '0':
                stud.proj= newvar
                
        
        for stud in newlistcopy:    
            
            print(StudData.format(stud.sid,stud.lname,stud.fname,stud.a1,stud.a2,stud.t1,stud.t2,stud.proj,stud.totalMarks,stud.grade))
            
    def  SortedReport(self,option):
        if(option.lower() == "lt"):
            newlist=sorted(self.classlist.clist, key=lambda Student:Student.lname)
            StudData='{:<9}{:<9}{:10}{:10}{:<9}{:<9} {:<9} {:<9} {:<15} {:<9}'
            print(StudData.format('ID','LN','FN','a1','a2','t1','t2','Project','total','GR'))
            newvar = ''
            newlistcopy =copy.deepcopy(newlist)
            for stud in newlistcopy:
                if stud.a1== '0':
                    stud.a1= newvar
                if stud.a2== '0':
                    stud.a2= newvar
                if stud.t1== '0':
                    stud.t1= newvar
                if stud.t2== '0':
                    stud.t2= newvar
                if stud.proj== '0':
                    stud.proj= newvar
                
        
            for stud in newlistcopy:    
            
                print(StudData.format(stud.sid,stud.lname,stud.fname,stud.a1,stud.a2,stud.t1,stud.t2,stud.proj,stud.totalMarks,stud.grade))
            
            self.g.showData()
        
        elif(option.lower() == "gr"):
            newlist=sorted(self.classlist.clist, key=lambda Student:Student.totalMarks)
            StudData='{:<9}{:<9}{:10}{:10}{:<9}{:<9} {:<9} {:<9} {:<15} {:<9}'
            print(StudData.format('ID','LN','FN','a1','a2','t1','t2','Project','total','GR'))
            newvar = ''
            newlistcopy =copy.deepcopy(newlist)
            for stud in newlistcopy:
                if stud.a1== '0':
                    stud.a1= newvar
                if stud.a2== '0':
                    stud.a2= newvar
                if stud.t1== '0':
                    stud.t1= newvar
                if stud.t2== '0':
                    stud.t2= newvar
                if stud.proj== '0':
                    stud.proj= newvar
                
        
            for stud in newlistcopy:    
            
                print(StudData.format(stud.sid,stud.lname,stud.fname,stud.a1,stud.a2,stud.t1,stud.t2,stud.proj,stud.totalMarks,stud.grade))
            
            self.g.showData()
            
            
            
            
