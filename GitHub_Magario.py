#! /usr/bin/python3

import re
import os
import sys
import operator 
import collections
import itertools
 
###########################################################################################################################    

#Add path object
path=os.getcwd()
Stop=os.listdir(path)   
p=re.compile('(\d+-[a-z]+-\d+)') 
fileList=p.findall(str(Stop))   #use regex to identify only needed files in directory for processing
Stop=p.findall(str(Stop))       #create start/stop/count global var based on number of files to be processed
Stop=len(Stop)
Start=int(0)
fileCount=Stop

#Parsing each file name in directory, and create nested list. 
def fnNewNestedList():
    
    # Parse Year, Month, Day, elimiate dash, format YY-MON-DD
    # findall() years
    q=re.compile('(\d+)-')  
    Year=q.findall(str(fileList))
    #print ('\nPrinting Year:\n',Year)

    # findall() months
    r=re.compile('-([a-zA-Z][a-zA-Z][a-zA-Z])') 
    Month=r.findall(str(fileList))
    #print ('\nPrinting Month:\n',Month)

    # findall() days
    s=re.compile('-(\d+)')
    Day=s.findall(str(fileList))
    #print ('\nPrinting Day:\n',Day)
    
    #create a nested list for each file in directory and nest parsed filename
    fileParsed=[[] for i in range(fileCount)]
    for i in range (Start,Stop,1):
        fileParsed[i]=[fileList[i],Year[i],Month[i],Day[i]]
        
    return fileParsed                               #return nested lists w/4 elements, 3 more to be added

#############################################################################################################
# A fn to sort, groupby, year, month, day (using parsedFile index 1,2,3). 
def fnMultiLevelSort(a):
    y=sorted(a, key=lambda x: x[1])  
    yy=[]
    #Create dictionary and sort y month order. Without this sorted will alpha sort months.
    dictMonth=collections.OrderedDict()
    dictMonth={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
    itertools.groupby(map(y.sort(key=lambda val: dictMonth[val[2]]),y)) ##sort month
    for i, y in itertools.groupby(y,key=lambda yy: yy[1]):
        for i, y in itertools.groupby(sorted(y, key=lambda dd: int(dd[3]))): 
            for rec in y:
                yy.append(rec)
                yy=list(yy)
    yy.sort(key=operator.itemgetter(1))
    return yy               #Careful,watch level return sits at here, will return single group if indent

###################################################################################################################

#Create new list of date spread values from ordered list of files.
#Append to z-list 4-digit yr, 3-alpha mo, full alpha mo, and spread values
def pause():
    programPause=input("Press <Enter> key to continue...")
    
#calculate the date range between files using the sorted list from MultiLevelSort
def fnDateSpread(a):
    z=a   

################################### REFACTOR DIFF FOR NINE(9)DATE SPREAD CONDITIONS#####################

    #12/06/17 maintain neg diff value as id marker for beg/end of month - refactor fn create label
    #create the date spread value
    for idx, elem in enumerate(z):  
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        diff=[]
        val=[]
        val.extend(int(e[3]) for e in z)
        diff = [val[i+1]-val[i] for i in range(len(val)-1)]
        #do I need to add back position zero here????
        #Yes, otherwise list is wrong length, and label processing needed
        diff.insert(0,val[0])

################################### REFACTOR DIFF FOR TEN(10)DATE SPREAD(see SpreadTest)CONDITIONS#####################
    
    #create YYYY list
    z2=(["19"+e[1] for e in z[0:]])
        
    #Append nested list element[4] with 4 digit year from z2 for label formating
    for e in z:
        ei=z.index(e)
        f=operator.__getitem__(z2,ei)
        e.append(f)
    #print ("\nPrinting appended z with YYYY: ".join(map(str,z)))

    #Append nested list element[5] with month name for label formating
    MonthName={"jan":"January","feb":"February","mar":"March","apr":"April","may":"May","jun":"June","jul":"July","aug":"August","sep":"September","oct":"October",
               "nov":"November","dec":"December"}
    for e in z:
        f=MonthName.get(e[2])
        e.append(f)
    #print ("\nPrinting appended z with YYYY,MO: ".join(map(str,z)))

    #Append nested list element [6] with date spread value for label formatting
    for e in z:
        ei=z.index(e)
        f=operator.__getitem__(diff,ei)
        e.append(f)
        #print(e)  #12/06/17 11/15/17 DATE SPREAD TESTING

    #REFACTOR and move after diff value calc append to nested list element [6]
    #Looking for ten(10) different end of month values per SpreadTest results, and zip file inconsistencies
    #nested list element [6] diff val to find beg/end of mo.
    CountElem=0
    for idx, elem in enumerate(z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        #print (ThisElem,NextElem)
        
        if (ThisElem[6] == -25 ):        #included for zip file inconsistencies
            #diff.append(ThisElem)
            #print("\nDIFF -25 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == -26 ):        
            #diff.append(ThisElem)
            #print("\nDIFF -25 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == -27): 
            #diff.append(ThisElem)
            #print("\nDIFF -27 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == -28): 
            #diff.append(ThisElem)
            #print("\nDIFF -28 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == -29): 
            #diff.append(ThisElem)
            #print("\nDIFF -29 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == -30):
            #diff.append(ThisElem)
            #print("\nDIFF -30 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == 1):
            #diff.append(ThisElem)
            #print("\nDIFF 1 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == 2):
            #diff.append(ThisElem)
            #print("\nDIFF 2 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == 3):
            #diff.append(ThisElem)
            #print("\nDIFF 3 ",ThisElem)
            CountElem=CountElem+1
        if (ThisElem[6] == 4):
            #diff.append(ThisElem)
            #print("\nDIFF 4 ",ThisElem)
            CountElem=CountElem+1
    #print("\nTotal neg element count ", CountElem)
    return z

#################### SPREAD TEST CODEBLOCK ####################
#Capture group and count all diff values for date spread and label/title logic
#11/15/17 Must review all 8000 files to create logic for range determination
#11/15/17 Use regex to find neg values, count and print

def fnSpreadTest(a):
    SpreadTest=[]
    
    #01/30/18 add path object
    path2=os.getcwd()
    Stop=os.listdir(path2)   
    p=re.compile('(\A-[0-9][0-9])')                     #regex to find only neg diff vals
    q=re.compile('(\d+-[a-z]+-\d+)')                    #regex to find Magario files
    r=re.compile('(\A-?\d{1,2}$)')                      #return diffs from flattened file
    SpreadTest=[(e[0],p.findall(str(e[6]))) for e in a] #use regex to identify neg date spread vals   
    SpreadTest2=[(e[0],str(e[6])) for e in a]
    NegCount=0
    Stop=q.findall(str(Stop))                           #create start/stop/count global var based on number of files to be processed
    Stop=len(Stop)                                      #num files in dir
    Start=int(0)
    FileCount=len(SpreadTest)                           #num files processed
    print ("\nSpreadTest Results ")
    print("Stop ",Stop)
    print ("p ",p)
    print ("r ",r)
    print ("Start ", Start)
    print ("FileCount ", FileCount)
    print ("SpreadTest2 Type: ", type(SpreadTest2))
    
    #define a lambda expression to flatten the SpreadTest list as it has a nested list
    flatten = lambda *n: (e for a in n
        for e in (flatten(*a) if isinstance(a,(tuple, list)) else (a,)))
    #for development, look at the list here
    #for i in SpreadTest2:
        #print ("SpreadTest2 ",i)
    
    #flatten the list for processing
    TempList=list(flatten(SpreadTest))
    TempList2=list(flatten(SpreadTest2))

    #grouping values
    TempList3=[m.group(0) for l in TempList for m in [p.search(l)] if m]
    SpreadTest3=[m.group(0) for l in TempList2 for m in [r.search(l)] if m]
    
#################### COUNTING/GROUPING NUMBER UNIQUE NEGATIVE VALUES###
    from collections import Counter
    print("\nCounter TempList3 p ",Counter(TempList3))
    NegCount=len([m.group(0) for l in TempList for m in [p.search(l)] if m])
    print("Count of Negative Values p ", NegCount)
    print("\nCounter SpreadTest3 r ",Counter(SpreadTest3))
    NegCount2=len([m.group(0) for l in TempList2 for m in [r.search(l)] if m])
    print("Count of Unique Values r ", NegCount2, "\n")
#################### COUNTING/GROUPING NUMBER UNIQUE NEGATIVE VALUES###
    
######################################## fnCreateLabel #############################################
# refactor fnCreateLabel for nine(9) diff cases for files 1920-1941
# create a label/title for each file in directory
def fnCreateLabel(a):
    z=a    
    #DoubleEntry
    #fixes fnDateSpread error for most DAYS 2 calc DIFF 1 in error. Chg to double entry and DIFF 2
    #Caution: date spread values vary. See SpreadTest codeblock regex for counting/grouping of unique value
    for idx, elem in enumerate(z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]
        if ThisElem[3] =="02" and ThisElem[6]==1:  #test for str(day) value and int(diff) value #01/10/18 update from"2"
            #print ("\nTesting day 2 and diff 1")
            #print ("PREVELEM:",PrevElem,"\nTHISELEM:",ThisElem,"\nNEXTELEM:",NextElem)
            ThisElem[6]=2
            #12/06/17 print ("THISELEM:",ThisElem,"ENDELEM:",EndElem,"NEXTELEM:",NextElem)
            #print("DoubleEntry day 2 diff 1 ",DoubleEntry,"\n")
            
    ############################## Test and treat end of month 10 edge cases ################
    #REFACTOR
    #z is a nested list
    #create elements to work on
    for idx, elem in enumerate(z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]

        #Test for and treat 31 and 30 day months
        if ThisElem[6] in(-25, -26, -27, -28, -29, -30):     
            #SingleEntry
            #Test and treat 31 day months for single entry
            #replace diff value to 1 
            if ThisElem[6] == -30 and PrevElem[2] in ('jan','mar', 'may', 'jul', 'aug', 'oct', 'dec'):
                #print ("This is a single entry item: ", ThisElem[2]," ",ThisElem[6])
                SingleEntry=("{} {},{}".format(PrevElem[5],PrevElem[3],PrevElem[4]))
                PrevElem[6]=1
                elem=PrevElem
                elem.append(SingleEntry)
                
            #SingleEntry
            #Test and treat 30 day months for single entry, replace diff val to 1
            if ThisElem[6] == -29 and PrevElem[2] in ('apr','jun', 'sep', 'nov'):
                #print ("This is a single entry 30 day month item : ", ThisElem[2]," ",ThisElem[6])
                SingleEntry=("{} {},{}".format(PrevElem[5],PrevElem[3],PrevElem[4]))
                PrevElem[6]=1
                elem=PrevElem
                elem.append(SingleEntry)
                
            #DoubleEntry
            #Test and treat 31 day months double entry by finding 1st of mo and backtrack
            if ThisElem[6] == -29 and PrevElem[2] in ('jan','mar', 'may', 'jul', 'aug', 'oct', 'dec'):
                #print ("This is a double entry 31 day month item: ", ThisElem[2]," ",ThisElem[6])
                #print("Print e[6] ReplaceElem6 ",PrevElem[6])
                DayElem=int(PrevElem[3])+1
                EndElem=("{} {},{}".format(PrevElem[5],DayElem,PrevElem[4]))
                ThisElem=("{} {},{}-".format(PrevElem[5],PrevElem[3],PrevElem[4]))
                NextElem=("{} {},{}".format(elem[5],elem[3],elem[4]))
                DoubleEntry=ThisElem+EndElem
                elem=PrevElem
                elem.append(DoubleEntry)
    #'''
    #DoubleEntry
    #this will get most DIFF 2s accross month types
    for idx, elem in enumerate (z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]
        if ThisElem[6] == 2 and NextElem[6] ==2:     
            DayElem=int(ThisElem[3])+1
            EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
            ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
            DoubleEntry=ThisElem+EndElem
            elem.append(DoubleEntry)
            #print ("THISELEM:",ThisElem,"ENDELEM:",EndElem,"NEXTELEM:",NextElem)
            #print ("\nDoubleEntry all DIFF 2 vals ",DoubleEntry,"\n")
    #'''
    #'''
        #DoubleEntry 30 day months outlier
        elif ThisElem[3] in ('28','29') and ThisElem[2] in ('apr','jun', 'sep', 'nov') and ThisElem[6]==2:
            DayElem=int(ThisElem[3])+1
            EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
            ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
            DoubleEntry=ThisElem+EndElem
            elem.append(DoubleEntry)
            #elem.append("TESTING ELIF")
            #print ("THISELEM:",ThisElem,"ENDELEM:",EndElem,"NEXTELEM:",NextElem)
            #print ("\nDoubleEntry 28,29 and 30 day mo DIFF 2 vals ",DoubleEntry,"\n")
    #'''
    #'''
        #DoubleEntry 31 day months outlier
        elif ThisElem[3] in ('29') and ThisElem[2] in ('jan','mar', 'may', 'jul', 'aug', 'oct', 'dec') and ThisElem[6]==2:
            DayElem=int(ThisElem[3])+1
            EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
            ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
            DoubleEntry=ThisElem+EndElem
            elem.append(DoubleEntry)
            #elem.append("TESTING ELIF")
            #print ("THISELEM:",ThisElem,"ENDELEM:",EndElem,"NEXTELEM:",NextElem)
            #print ("\nDoubleEntry 29 and 31 day mo DIFF 2 vals ",DoubleEntry,"\n")
    #'''

    #February incl leap year
    #'''
    for idx, elem in enumerate (z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]

        #DoubleEntry February leap year
        if ThisElem[3] ==('28') and ThisElem[2] == "feb" and ThisElem[1] in ('20','24','28','32','36','40','44','48','52','56','60'):
            DayElem=int(ThisElem[3])+1
            EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
            ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
            DoubleEntry=ThisElem+EndElem
            elem.append(DoubleEntry)
    #'''
    #'''
        #SingleEntry February
        elif ThisElem[3] == ('28') and ThisElem[2] == "feb":
            SingleEntry=("{} {},{}".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            ThisElem[6]=1
            #elem=PrevElem
            elem.append(SingleEntry)  
    #'''

    #1st of month
    #'''
    for idx, elem in enumerate (z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]
        #DoubleEntry 1st of month
        if ThisElem[3] ==('1') and NextElem[3] == ('3') and ThisElem[6] in (-25, -26, -27, -28, -29, -30) :
            DayElem=int(ThisElem[3])+1
            EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
            ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
            DoubleEntry=ThisElem+EndElem
            elem.append(DoubleEntry)
    #'''
    #'''
        #SingleEntry 1st of month
        elif ThisElem[3] == ('1') and NextElem[3] == ('2') and ThisElem[6] in (-25, -26, -27, -28, -29, -30):
            SingleEntry=("{} {},{}".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            elem.append(SingleEntry)  
    #'''
    #Treat first/last record(idx), non-sequential DIFFS and correct diff vals
    #'''
    for idx, elem in enumerate (z):
        ThisElem=elem
        NextElem=z[(idx+1)% len(z)]
        PrevElem=z[(idx-1)% len(z)]
        FirstRec=0
        LastRec=len(z)-1
 
        #Update DIFF value first and last record of collection SingleEntry, look for 7 item elements
        if len(ThisElem) == 7 and idx in (FirstRec,LastRec):
            #print ("FIRST LAST ", ThisElem)
            #print ("FirstRec ",FirstRec)
            #print ("LastRec ",LastRec)
            SingleEntry=("{} {},{}".format(ThisElem[5],ThisElem[3],ThisElem[4]))
            ThisElem[6]=1
            elem.append(SingleEntry)  
            #print ("FIRST LAST ",ThisElem)
            
        #CreateLabel and UpdateDiffs of non-sequential outliers, look for 7 item elements
        if len(ThisElem) == 7 :
            Diff=int(NextElem[3])-int(ThisElem[3])
            if Diff ==1:
                SingleEntry=("{} {},{}".format(ThisElem[5],ThisElem[3],ThisElem[4]))
                ThisElem[6]=1
                elem.append(SingleEntry)
            else:
                DayElem=int(ThisElem[3])+int(Diff)-1
                EndElem=("{} {},{}".format(ThisElem[5],DayElem,ThisElem[4]))
                ThisElem=("{} {},{}-".format(ThisElem[5],ThisElem[3],ThisElem[4]))
                NextElem=("{} {},{}".format(NextElem[5],NextElem[3],NextElem[4]))   #for testing
                DoubleEntry=ThisElem+EndElem
                elem[6]=Diff
                elem.append(DoubleEntry)
                #print ("UPDATE DIFF ",Diff, ThisElem, "EndElem ",EndElem, "INDEX ",idx)

    ########################### REFORMAT LABEL #########################

    #create month ordered dictionary
    dictMonth=collections.OrderedDict()
    dictMonth={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":10,"November":11,"December":12}
    TempList=[]
    TempList.extend([e[7]] for e in z)
    start=re.compile('(\w*\s)''(\d{1,2})'',(\d{1,4})')
    print("Start regex: ",start)
    RegexFindall=[start.findall(str(e)) for e in TempList]

    #change tuples to list
    TempList=[]
    TempList2=[]
    for idx, ei in enumerate(RegexFindall):
        ThisElem=ei
        NextElem=RegexFindall[(idx+1)% len(RegexFindall)]
        for i in ThisElem:
            TempList=[list(map(list,e)) for e in RegexFindall]

    #convert nested list month names to int
    for idx,ei in enumerate(TempList):
        ThisElem=ei
        NextElem=TempList[(idx+1)% len(TempList)]
        
        for i in ThisElem:
            
            for ii in NextElem:
                
                for k,v in dictMonth.items():
                    if k in i[0]:
                        month=v
            i[0]=month                              #be careful with indentation, will break code
        TempList2.append(ThisElem)    
        #print("\nThis",ThisElem,"\nNext",NextElem) #testing
        #print ("\nTempList2".join(map(str,TempList2))) 
    
    ################# TESTING REFORMAT LABEL FOR SID ############################## 
    #Append a list with the newley formtted dates
    TempList3=[]
    for idx,ei in enumerate(TempList2):
        ThisElem=ei
        TempList3.append(["{}-{}-{}".format(i[2],i[0],i[1]) for i in ThisElem])
    #print ("\nTempList3Reformat".join(map(str,TempList3))) 

    #use python datetime module to convert single to double digit days
    from datetime import datetime
    TempFix=TempList3
    for x in TempFix:
        for idx,i in enumerate(x):
            ei=x.index(i)
            f=operator.__getitem__(x,ei)       
            g=datetime.strptime(i,'%Y-%m-%d').strftime('%Y-%m-%d')      #reformating to dd days
            x[idx]=i.replace(i,g)                                       #update each element item with two digit day
    print ("\nFixing single digit to double digit date values")         #for processing clarity/feedback
    
    #appending z nested lists with new values for final return
    for idx, ei in enumerate(z):
        ei.append(TempList3[idx])
        #print ("\nZAppend ".join(map(str,z)))       #01/12/18 z list is updating due to SHALLOW COPY and binding reference
    ################# TESTING REFORMAT LABEL FOR SID ##############################

    return z

####################################################################################################################

def pause():
    programPause=input("Press <Enter> key to continue...")
    
#Create the CollectionID before appending to SID (source id)
def fnCollectID():
    CID = []
    #Get Inputs
    Domain = input(("Please enter the Domain: ")).lower()
    Library = input(("Please enter the Library: ")).lower()
    CollectID = input(("Please enter the CollectionID: "))
    FLSeries = input(("Please enter the first level series: ")).upper()

    #Store the variable values in CID for later formatting and processing
    CID.append(Domain)
    CID.append(Library)
    CID.append(CollectID)
    CID.append(FLSeries)

    #Echo Input for user validation
    print("Domain is: ", Domain)
    print("Library is: ", Library)
    print("CollectionID is: ", CollectID)
    print("First level series is: ", FLSeries)
    print ("The Collection ID will contain these items in this order: ", '\n',CID)
        
    #Validate Input, Return to main function if corrections needed
    repeat = (input("\nWould you like to correct this input? Y or N? "))
    repeat.lower
    if repeat == "y" :
        #main()
        print("\nOk. Lets re-enter the info.\n")
        #Domain=''
        #Library=''
        #CollectID=''
        #FLSeries=''
        sys.stdout.flush()
        fnCollectID()
    else :
        #Assign and Format CollectID
        CollectID="{0:3}:{1:3}{2}_{3}_".format(CID[0],CID[1],CID[2], CID[3])
        print("\nOk. This is the collection ID to be used.")
        
        #CollectID variable is now in CID list
        CID.append(CollectID)
        print (CollectID)
        print ("\nSample Output CID list ",CID)
        #print("\nOk. Next we will create the Source ID.")
        #pause()
    return CID

#############################################################################################################

#Create SourceID from CollectionID(CID) and reformatted date spread
def fnSourceID(arg1,arg2):
    print("\nWe are now creating the SourceID....",)
    def pause():
        programPause=input("Press <Enter> key to continue...")
    pause()
    
    #define a lambda expression to flatten a nested list
    flatten = lambda *n: (e for a in n
        for e in (flatten(*a) if isinstance(a,(tuple, list)) else (a,)))
    
    #Assign CID and zList to local var
    var1, var2 = arg1,arg2     
    f=[]

    #Assign the prefix to be used for series
    for idx, x in enumerate(var2):
        CollectID=var1[4]

        #get reformatted date spread vals x[8] for single or double entry
        f=operator.__getitem__(x,8)
        x+=f
        x.pop(8)

    CID=var1
    DoubleEntry=10
    SingleEntry=9
    SID=[]
    
    #Create the SourceID for single and double entry x elements 
    for idx, x in enumerate(var2):
        size=len(x)
        
        if size == SingleEntry:                     #testing for single entry nested element size
            #then change to single entry format
            #add CID prefix = SID
            tempSID="{}{}".format(CID[4],x[8])
            #append SID to z list
            x.append(tempSID)
            
        elif size  == DoubleEntry:                  #testing for double entry nested element size
            #change to double entry format
            #add CID prefix = SID
            tempSID= "{}{}_{}".format(CID[4],x[8],x[9])
            #append SID to z list
            x.append(tempSID)
    print("END fnSourceID\n")
    z=var2
    return z

################################## output tab delim file, and QC file for zNestedList #################################

def fnTSV(arg1):
    import csv
    DoubleEntry=11                  #number of nested elements for Double Entry, see index summary below
    SingleEntry=10                  #number of nested elements for Single Entry, see index summary below
    var1=arg1                       #SHALLOW COPY
    countSingle=0
    countDouble=0
    headers=['METADATA','SID','DRUID','LABEL']
    headersQC=['PARSE_FN','YY','3ALPHA_MMM','DD','YYYY','FULLALPHA_MO','DIFFVAL','LABEL','REFORMAT1','REFORMAT2','SID']
    print("\nWe are now getting ready to process the final output....",)
    def pause():
        programPause=input("Press <Enter> key to continue...")
    pause()
    
    #User Input series end date for filteredList and qc output
    SeriesEnd=input("\nPlease input the final date in this series, format (INT-INT-INT) YYYY-MM-DD \n").lower()
    print("\nWe will now create the final output manifest and quality control files....",)
    pause()
    
    #Create stop filter for series range in var1/zlist
    stopIndex=[int(var1.index(i)) for i in var1 if SeriesEnd in i[9:11]]  
    stop=stopIndex[0]+1
    print("Range stop Index: ",stop)                                                 
    print(type(stop))

    #Create series list for output
    filteredList= [var1[i] for i in range(0,stop)]      
    count=len(filteredList)
    print('\nCount of list items: ',count)
    #print('\nFiltered List '.join(map(str,filteredList)))

    
    #insert output headers
    filteredList.insert(0,headers)
    print('\nFiltered List '.join(map(str,filteredList)))

    #Create series manifest w/SID and Label/Title
    with open('MagarioManifest.tsv', 'w', newline='', encoding='utf-8') as file:
        a=csv.writer(file, dialect='excel-tab',delimiter='\t')
        a.writerow(filteredList[0])
        META=""
        DRUID=""
        for idx, x in enumerate(filteredList): 
            if len(x) == SingleEntry:
                SID=x[9]
                Label=x[7]  
                a.writerow((META,SID,DRUID,Label))      
            if len(x) == DoubleEntry:
                SID=x[10]
                Label=x[7]                                                     
                a.writerow((META,SID,DRUID,Label))      
    
    ############################# CREATE QUALITY CONTROL OUTPUT FILE (QC)############################
    #NOTE: for QC and readability-SingleEntry SID moved to x[10] 
    #Index summary of z nested list see below main()

    #Delete output headers, insert QC headers
    del filteredList[0]
    filteredList.insert(0,headersQC)
    #print('\nFiltered List headersQC '.join(map(str,filteredList[0:6])))  #testing

    #Create QC file from series filtered list, tab delim
    with open('MMQC.tsv', 'w', newline='', encoding='utf-8') as file:
        a=csv.writer(file, dialect='excel-tab',delimiter='\t')
        for idx, x in enumerate(filteredList):
            if len(x)== SingleEntry:
                x.append(x[9])
                x[9]='     '
                a.writerow((x))
            else:
                a.writerow((x))  
        
    ############################# CREATE QUALITY CONTROL OUTPUT FILE (QC)############################

    print("\nEND fnTSV")

#################################################################################################################

def main():
    a=fnNewNestedList()
    b=fnMultiLevelSort(a)
    c=fnDateSpread(b)       
    fnSpreadTest(c)         
    d=fnCreateLabel(c)                
    e=fnCollectID()
    f=fnSourceID(e,d)        
    fnTSV(f)
    exit()
main()

############# FnReturns, ZLIST AND CID INDEX SUMMARY #############
'''
#Function Returns summary
fnCollectID             return CID
fnNewNestedList         return fileParsed
fnMultiLevelSort        return yy
fnDateSpread            return z
fnCreateLabel           return z
fnSourceID              return z
'''

'''
#CID  list index summary:
[0] Domain
[1] Library
[2] CollectionID
[3] First Level Series
[4] full CollectID
'''
'''
#z nested list index summary:
[0] Parsed file name, excluding extension
[1] 2-digit year
[2] 3-alpha month name
[3] 2-digit day (or single digit)              #01/10/18 fix to two digit day
[4] 4-digit year
[5] Full alpha spelling month name
[6] Date spread integer value
[7] Label/title date spread format  
[8] Reformat date spread value 1 for single or double entry
[9] Reformat date spread value 2 for double entry
[10] SID double entry or [9] SID single entry
#[9] SID=CID[4] + label reformat(Z/e[8])  #01/03/18 REM single or double entry due to...
#[10] filename = [0] + .jpg               #01/03/18 REM ...change length of x element in z list
'''
############# FnReturns, ZLIST AND CID INDEX SUMMARY #############  







    


    





    



