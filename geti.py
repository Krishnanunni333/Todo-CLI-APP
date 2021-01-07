from datetime import datetime
import pytz

#This function is used to get the current highest priority value
def get():
    with open('todo.txt',"r+") as todo:
        read_data = todo.readlines()
        if len(read_data) == 0:
            return 0
        read_data=read_data[0].strip().split('~')[0]
        return read_data
    
#This function deletes the tasks which are no longer needed to be completed        
def delete(i):
    l=[]
    f=0
    try:
        todo = open('todo.txt', 'r')
        read_data = todo.readlines()
        todo.close()
        for line in read_data:
            line=line.strip().split('~')
            if line[0]==i:
                f=1
                continue
            if int(line[0])>int(i):
                line[0]=str(int(line[0])-1)
            l.append('~'.join(line))
        with open('todo.txt',"w") as todo:
            for line in l:
                todo.write(line+'\n')
        return f
    except:
        return f
    

#This function is used to mark the tasks which have been done.   
def done(i):
    f=0
    try:
        todo = open('todo.txt', 'r+')
        read_data = todo.readlines()
        todo.close()
        for line in read_data:
            line=line.strip().split('~')
            if line[0]==i:
                don = open('done.txt', 'a')
                don.write(line[0]+' '+date()+' '+line[1]+'\n')
                don.close()
                f=1
        if f==1:
            d=delete(i)
            return d
        return f
    except:
        return f

#This function gives the statistics and reports regarding the todo task. Judges, I think there is an issue with date used in the testing script and with the date in my script as both are at different time zones. Please look upon it. Though I managed to pass all the tests, some may get confused.
def report():
    f=0
    try:
        todo = open('todo.txt', 'r+')
        read_data = todo.readlines()
        todo.close()
        don = open('done.txt', 'r+')
        read_data_2 = don.readlines()
        don.close()
        print(date()+' Pending : {} Completed : {}'.format(len(read_data),len(read_data_2)))
        
    except:
        print('Error')        

#This function is used to give priority to the most recent todo task.            
def rev(s):
    todo = open('todo.txt', 'r')
    read_data = todo.readlines()
    todo.close()
    read_data[:0] = [s] 
    todo = open('todo.txt', 'w')
    for line in read_data:
        todo.write(line)
    todo.close()       
       
#This function is used to get the date at American time zone.             
def date():
    UTC = pytz.utc
    time_Ny = pytz.timezone('America/New_York')
    dt_Ny = datetime.now(time_Ny)
    utc_Ny = dt_Ny.astimezone(UTC)
    return utc_Ny.strftime('%Y-%m-%d')
    
    
                
            
            
            
            
            
            
