'''
Created on May 18, 2018

@author: Kunal Sharma
        
'''
from compute import*


class GraderClass(object):
    
    def StudentsInClassData(self):
    
        with open('C:/Users/pc/Desktop/python/compassignment/class.txt') as file:
    
            for line in file:
                elements = line.rstrip().split('|')
                s1=Student(elements[0],elements[1],elements[2])
                classlist.clist.append(s1);



    def Assignment1Data(self):
        firstloop = True
        with open('C:/Users/pc/Desktop/python/compassignment/a1.txt') as file:
    
            for line in file:
                if firstloop:
                    classlist.a1=line
                    firstloop=False
                else:
                    elements = line.rstrip().split('|')
                
                    for stud in classlist.clist:
                        if stud.sid ==  elements[0]:
                            if elements[1]:
                                stud.a1 = elements[1]
                            else:
                                stud.a1="0"
                        
    
    def Assignment2Data(self):
        firstloop = True
        with open('C:/Users/pc/Desktop/python/compassignment/a2.txt') as file:
    
            for line in file:
                if firstloop:
                    classlist.a2=line
                    firstloop=False
                else:
                    elements = line.rstrip().split('|')
                    for stud in classlist.clist:
                        if stud.sid ==  elements[0]:
                            if elements[1]:
                                stud.a2 = elements[1]
                            else:
                                stud.a2="0"
                            
    def test1Data(self):
        firstloop = True
        with open('C:/Users/pc/Desktop/python/compassignment/t1.txt') as file:
    
            for line in file:
                if firstloop:
                    classlist.t1=line
                    firstloop=False
                else:
                    elements = line.rstrip().split('|')
                    for stud in classlist.clist:
                        if stud.sid ==  elements[0]:
                            if elements[1]:
                                stud.t1 = elements[1]
                            else:
                                stud.t1="0"
    
    def test2Data(self):
        firstloop = True
        with open('C:/Users/pc/Desktop/python/compassignment/t2.txt') as file:
    
            for line in file:
                if firstloop:
                    classlist.t2=line
                    firstloop=False
                else:
                    elements = line.rstrip().split('|')
                    for stud in classlist.clist:
                        if stud.sid ==  elements[0]:
                            if elements[1]:
                                stud.t2 = elements[1]
                            else:
                                stud.t2="0"
    
    def ProjectData(self):
        firstloop = True
        with open('C:/Users/pc/Desktop/python/compassignment/proj.txt') as file:
    
            for line in file:
                if firstloop:
                    classlist.proj=line
                    firstloop=False
                else:
                    elements = line.rstrip().split('|')
                    for stud in classlist.clist:
                        if stud.sid ==  elements[0]:
                            if elements[1]:
                                stud.proj = elements[1]
                            else:
                                stud.proj="0"
                            
                            
    
    def calculateGrade(self):
        for stud in classlist.clist:
            totalMarks=0
            totalMarks+=round((float(stud.a1)/float(classlist.a1)*7.5),2)
            totalMarks+=round((float(stud.a2)/float(classlist.a2)*7.5),2)
            totalMarks+=round((float(stud.proj)/float(classlist.proj)*25),2)
            totalMarks+=round((float(stud.t1)/float(classlist.t1)*30),2)
            totalMarks+=round((float(stud.t2)/float(classlist.t2)*30),2)
           
            stud.totalMarks=round(totalMarks,2)
          
            
            if totalMarks<=50:
                stud.grade="F"
            elif totalMarks>50 and totalMarks <=57:
                stud.grade="C"
            elif totalMarks>57 and totalMarks <=64:
                stud.grade="B-"
            elif totalMarks>64 and totalMarks <=71:
                stud.grade="B"
            elif totalMarks>71 and totalMarks <=78:
                stud.grade="B+"
            elif totalMarks>78 and totalMarks <=85:
                stud.grade="A-"
            elif totalMarks>85 and totalMarks <=92:
                stud.grade="A"
            elif totalMarks>92 and totalMarks <=100:
                stud.grade="A+"
                
    def GradeWithNewPassFail(self,newpfgrade):
        import copy
        newlist =copy.deepcopy(classlist.clist)
        for stud in newlist:
            totalMarks=0
            totalMarks+=round((float(stud.a1)/float(classlist.a1)*7.5),2)
            totalMarks+=round((float(stud.a2)/float(classlist.a2)*7.5),2)
            totalMarks+=round((float(stud.proj)/float(classlist.proj)*25),2)
            totalMarks+=round((float(stud.t1)/float(classlist.t1)*30),2)
            totalMarks+=round((float(stud.t2)/float(classlist.t2)*30),2)
           
            stud.totalMarks=round(totalMarks,2)
            
            intnewpfgrade=float(newpfgrade)
            rangeMarks=(100-intnewpfgrade)/7
            
                    
            if stud.totalMarks<=int(intnewpfgrade):
                stud.grade="F"
            elif stud.totalMarks>intnewpfgrade and stud.totalMarks <=intnewpfgrade+rangeMarks:
                stud.grade="C"
            elif stud.totalMarks>intnewpfgrade+rangeMarks and stud.totalMarks <=intnewpfgrade+(2*rangeMarks):
                stud.grade="B-"
            elif stud.totalMarks>intnewpfgrade+(2*rangeMarks) and stud.totalMarks<=intnewpfgrade+(3*rangeMarks):
                stud.grade="B"
            elif stud.totalMarks>intnewpfgrade+(3*rangeMarks) and stud.totalMarks <=intnewpfgrade+(4*rangeMarks):
                stud.grade="B+"
            elif stud.totalMarks>intnewpfgrade+(4*rangeMarks) and stud.totalMarks <=intnewpfgrade+(5*rangeMarks):
                stud.grade="A-"
            elif stud.totalMarks>intnewpfgrade+(5*rangeMarks) and stud.totalMarks <=intnewpfgrade+(6*rangeMarks):
                stud.grade="A"
            elif stud.totalMarks>intnewpfgrade+(6*rangeMarks) and stud.totalMarks <=100:
                stud.grade="A+"
                
        StudData='{:<9}{:<9}{:10}{:10}{:<9}{:<9} {:<9} {:<9} {:<9} {:<9}'
        print(StudData.format('ID','LN','FN','a1','a2','t1','t2','Project','GR','FL'))
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
        
        g.showData()
        
    def showData(self):
        
        
        print("1> Display individual component")
        print("2> Display component average")
        print("3> Display Standard Report")
        print("4> Sort by alternate column")
        print("5> Change Pass/Fail point")
        print("6> Exit")
        
        option = input("Select the option")
        
       
        
        
        if option == "1":
            individualoption=input("Please select which component to display: A1, A2, T1,T2,Project")
            d.AvailableOptions(individualoption)
            
        elif option =="2":
            individualoption=input("Please select which component to display: A1, A2, T1,T2,Project")
            d.ComponentAverage(individualoption)
           
        elif option == "3":
            d.StandardReport()
        elif option =="4":
            individualoption=input("Please select Sort order : LT or GR")
            d.SortedReport(individualoption)
                     
        elif option == "5":
            newgrade=input("Please provide the new pass/fail grade")
            g.GradeWithNewPassFail(newgrade)
        elif option == "6":
            print("Good Bye")
            exit
        else:
            newgrade=input("Option not found. Please choose again")
            g.showData() 
            
class Student(object):
  

    def __init__(self, sid, fname, lname):
        
        self.sid = sid
        self.fname = fname
        self.lname = lname
        



class Class(object):
     

    def __init__(self, clist):
       
        self.clist = clist



classlist=Class([])



g=GraderClass
g=GraderClass()
d= DataCalculations(classlist, g)
g.StudentsInClassData()
g.Assignment1Data()
g.Assignment2Data()
g.test1Data()
g.test2Data()
g.ProjectData()
g.calculateGrade()

GraderClass.showData(g)
        
            
            