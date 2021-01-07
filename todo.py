#!/usr/bin/env python
import sys
import geti


#Data gathering from the shell
data = ' '.join(sys.argv[1:]).strip().split()

#Checking conditions for 'help' operation
if len(data)==0 or data[0]=='help':
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')
    
#Checking conditions for 'ls' operation
elif data[0]=='ls':
    try:
        with open('todo.txt') as todo:
            read_data=todo.readlines()
            if len(read_data) == 0:
                raise Exception('There are no pending todos!')
            for line in read_data:
                line=line.strip().split('~')
                print('[{}] {}'.format(line[0],line[1]))
    except:
        print('There are no pending todos!')

#Checking conditions for 'add' operation
elif data[0]=='add':
    todo= open("todo.txt", "a")
    try:
        if data[1]!='':
            print('Added todo: "{}"'.format(' '.join(data[1:])))
            res=int(geti.get())
            #todo.write('{}~{} \n'.format(res+1,' '.join(data[1:])))
        todo.close()
        geti.rev(('{}~{} \n'.format(res+1,' '.join(data[1:]))))
    except:
        print('Error: Missing todo string. Nothing added!')
        
        
   
#Checking conditions for 'del' operation
elif data[0]=='del':
    try:
        res=geti.delete(data[1])
        if res==0:
            print('1.Error: todo #{} does not exist. Nothing deleted.'.format(data[1]))
        else:
            print('Deleted todo #{}'.format(data[1]))
    except:
        print("Error: Missing NUMBER for deleting todo.")

#Checking conditions for 'done' operation
elif data[0]=='done':
    try:
        res=geti.done(data[1])
        if res==0:
            print('Error: todo #{} does not exist.'.format(data[1]))
        else:
            print('Marked todo #{} as done.'.format(data[1]))
    except:
        print('Error: Missing NUMBER for marking todo as done.')
    
#Checking conditions for 'report' operation
elif data[0]=='report':
    geti.report()

#Command error 
else:
    print('sorry...error in command')


