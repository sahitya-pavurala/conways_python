#!C:\Python27\python.exe
'''
Progammer : Sahitya Pavurala
ID : 0490373
HW 01

Program to demonstrate conway's game of life
This program takes input from a file named "life.txt"
and prints the output on the console window
'''
import os
import copy

def getFile():
    '''
    Returns a file object if the file name is valid
    or else it prints an error
    '''
    try:
        fileObj = open("life.txt",'r')
    except IOError:
        print "Check the file name it should be 'life.txt'!!!"
        exit(1)
    return fileObj 

def processFile():
    '''
    Gets the lines from the file as a list and
    processess them and finally returns a matrix
    with all the elements as characters from the lines
    '''
    fileObj = getFile()
    lines = fileObj.readlines()#lines is the list of all lines from the file
    firstLine = lines.pop(0)
    rows = firstLine.split()[0]#rows has the number of rows
    columns = firstLine.split()[1]#rows has the number of columns
    content =[]
    count = int(rows)
    for i in lines:
        words = ['-'] * int(columns)#this creates a temporary list with '-' character
        for j in range(len(words)):
            line = list(i)#converts the line as a list with all the characters as list elements
            try:
                if line[j] == '*':
                   words[j] = '*'
            except IndexError:
                pass
        content.append(words)
    while len(content)  < int(rows):
        content.append(['-'] * int(columns))
    return content


def originalData():
    '''
    Gets the matrix from processFile function
    and returns it
    '''
    matrix = processFile()
    return matrix


def createNextMatrix(nextmatrix):
    '''
    Takes the current generation matrix as parameter, 
    creates the next generation matrix and
    returns it 
    '''
    newmatrix = copy.deepcopy(nextmatrix)#creates a copy of the nextmatrix
    i = 0
    while i < len(nextmatrix):#here in the loops below we check for the number of neighbours
        j= 0
        while j < len(nextmatrix[0]):
            count = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if k < 0 or k >= len(nextmatrix) or l < 0 or l >= len(nextmatrix[0]):
                        pass
                    elif (k == i and l == j):
                        pass
                    elif nextmatrix[k][l] == '*':
                        count = count+1
            if nextmatrix[i][j] == '*' and (count == 2 or count == 3):#checks the cell lives in the next generation
                newmatrix[i][j] = '*'
            elif nextmatrix[i][j] == '-' and count == 3:#checks if it is a birth cell
                newmatrix[i][j] = '*'
            else :
                newmatrix[i][j] = '-'
            
            j = j+1
        i = i+1
    return newmatrix


def nextGenerations():
    '''
    Prints the original data and all the
    next generation sequences
    '''
    nextmatrix = originalData()
    for i in nextmatrix:
        print ''.join(i)
    print '=' * len(i) , 1    
    for i in range(10):
        nextmatrix = createNextMatrix(nextmatrix)
        for j in nextmatrix:
            print ''.join(j)
        print '=' * len(j) , i+2 #print a delimiting line to separate each generation sequence
    
        
def main():
    nextGenerations()
    os.system('pause')#pauses the output window 
    
if __name__ == '__main__':#this is used to make the program file double clickable
    main()
