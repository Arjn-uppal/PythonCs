def main():

    x = triangle(int(input("Give me an N:")))
    print(x)

def triangle(N):
    
  #Base Case
    if N == 1:
        return 1

    #Recursive Call
    else:
        myResult = N + triangle(N-1)
        #print(myResult)

        return myResult
    
main()