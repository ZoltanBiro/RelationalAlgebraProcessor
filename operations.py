def selection(table,cond):
    result=[]
    table1=table
    condition=cond
    #find index of that column name
    columnIndex=table1[0].index(condition[0])
    result.append(table1[0])
    if condition[1]=="=":
        for i in range(1,len(table1)): # for each item
            if table1[i][columnIndex]==condition[2]:
                result.append(table1[i])
    elif condition[1]=="!=":
        for i in range(1,len(table1)): # for each item
            if table1[i][columnIndex]!=condition[2]:
                result.append(table1[i])
    elif condition[1]=="<":
        for i in range(1,len(table1)): # for each item
            if float(table1[i][columnIndex])<float(condition[2]):
                result.append(table1[i])
    elif condition[1]==">":
        for i in range(1,len(table1)): # for each item
            if float(table1[i][columnIndex])>float(condition[2]):
                result.append(table1[i])
    
    return result

        
def projection(table,columns):
    result=[]
    table1=table
    columnTitles=columns
    columnIndexes=[]
    for c in columnTitles:
        columnIndexes.append(table1[0].index(c))

    result.append(columnTitles)
    for i in range(1,len(table1)):
        temprow=[]
        for c in columnIndexes:
            temprow.append(table1[i][c])
        result.append(temprow)

    return result
    
def cartesianProduct(ltable,rtable):
    table1=ltable
    table2=rtable

    result=[]
    result.append(table1[0]+table2[0])
    for i in range(1,len(table1)):
        for j in range(1,len(table2)):
            result.append(table1[i]+table2[j])
    
    return result

def innerJoin(ltable,rtable,lcolumn,rcolumn):
    table1=ltable
    table2=rtable

    result=[]

    leftColumn=lcolumn
    rightColumn=rcolumn
    leftColumnIndex=table1[0].index(leftColumn)
    rightColumnIndex=table2[0].index(rightColumn) 

    result.append(table1[0]+table2[0])
    for i in range(1,len(table1)):
        for j in range(1,len(table2)):
            if table1[i][leftColumnIndex]==table2[j][rightColumnIndex]:
                result.append(table1[i]+table2[j])
    
    return result

def leftOuterJoin(ltable,rtable,lcolumn,rcolumn):
    table1=ltable
    table2=rtable

    result=[]

    leftColumn=lcolumn
    rightColumn=rcolumn
    leftColumnIndex=table1[0].index(leftColumn)
    rightColumnIndex=table2[0].index(rightColumn) 

    result.append(table1[0]+table2[0])
    for i in range(1,len(table1)):
        added=0
        for j in range(1,len(table2)):
            if table1[i][leftColumnIndex]==table2[j][rightColumnIndex]:
                result.append(table1[i]+table2[j])
                added=1
        if added==0:
            nullList=[]
            for k in table2[0]:
                nullList.append(None)
            result.append(table1[i]+nullList)
    
    return result

def rightOuterJoin(ltable,rtable,lcolumn,rcolumn):
    table1=ltable
    table2=rtable

    result=[]

    leftColumn=lcolumn
    rightColumn=rcolumn
    leftColumnIndex=table1[0].index(leftColumn)
    rightColumnIndex=table2[0].index(rightColumn) 

    result.append(table1[0]+table2[0])
    for i in range(1,len(table2)):
        added=0
        for j in range(1,len(table1)):
            if table1[j][leftColumnIndex]==table2[i][rightColumnIndex]:
                result.append(table1[j]+table2[i])
                added=1
        if added==0:
            nullList=[]
            for k in table1[0]:
                nullList.append(None)
            result.append(nullList+table2[i])
    
    return result

def fullOuterJoin(ltable,rtable,lcolumn,rcolumn):
    table1=ltable
    table2=rtable

    result=[]

    leftColumn=lcolumn
    rightColumn=rcolumn
    leftColumnIndex=table1[0].index(leftColumn)
    rightColumnIndex=table2[0].index(rightColumn) 

    result.append(table1[0]+table2[0])
    radded=[]
    for i in range(len(table2)):
        radded.append(0)
    for i in range(1,len(table1)):
        added=0
        for j in range(1,len(table2)):
            if table1[i][leftColumnIndex]==table2[j][rightColumnIndex]:
                result.append(table1[i]+table2[j])
                added=1
                radded[j]=1
        
        if added==0:
            nullList=[]
            for k in table2[0]:
                nullList.append(None)
            result.append(table1[i]+nullList)
    
    for i in range(1,len(table2)):
        nullList=[]
        for k in table1[0]:
            nullList.append(None)   
        if(radded[i])==0:
            result.append(nullList+table2[i])
 
    return result

def intersection(ltable,rtable):
    result=[]
    if(len(rtable[0])!=len(ltable[0])):
        print("Error, the number of columns must be the same")
        return result
    for i in range(len(ltable[0])):
        if ltable[0][i]!=rtable[0][i]:
            print("Error: column titles and datatypes must be the same")
            return[]
    result.append(ltable[0])

    for i in range(1,len(ltable)):
        if(ltable[i]in rtable):
            result.append(ltable[i])
    return result

def union(ltable,rtable):
    result=[]
    if(len(rtable[0])!=len(ltable[0])):
        print("Error, the number of columns must be the same")
        return result
    for i in range(len(ltable[0])):
        if ltable[0][i]!=rtable[0][i]:
            print("Error: column titles and datatypes must be the same")
            return[]
    result=result+ltable

    for i in range(1,len(ltable)):
        if(ltable[i] not in rtable):
            result.append(ltable[i])
    return result

def subtraction(ltable,rtable):
    result=[]
    if(len(rtable[0])!=len(ltable[0])):
        print("Error, the number of columns must be the same")
        return result
    for i in range(len(ltable[0])):
        if ltable[0][i]!=rtable[0][i]:
            print("Error: column titles and datatypes must be the same")
            return[]
    result.append(ltable[0])

    for i in range(1,len(ltable)):
        if(ltable[i] not in rtable):
            result.append(ltable[i])
    for i in range(1,len(rtable)):
        if (rtable[i] not in ltable):
            result.append(rtable[i])
    return result



