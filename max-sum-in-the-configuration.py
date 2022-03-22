#User function Template for python3

def max_sum(a,n):
    #code here
    maxi = -1
    s = 0
    gg = 0
    for i,j in enumerate(a):
        s+=j
        gg+=i*j
    maxi = gg
    for i in range(1,n):
        gg = gg-s+n*a[i-1]
        maxi= max(maxi,gg)
    return maxi
    
    
    # it will give tle although it is corrrect .
    # gg ={}
    # for i,j in enumerate(a):
    #     gg[i] = j
    # # print(gg)
    # for k in range(n):
    #     ans =0
    #     for key in gg:
    #         ans+=gg[key]*key
    #     maxi = max(maxi,ans)
    #     # print(maxi)
    #     l = gg[0]
    #     for key in gg:
    #         if key == n-1:
    #             gg[key] = l
    #         else:
    #             gg[key]= gg[key+1]
    #     # print(gg)
            
    # # print(maxi)
    # return maxi
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends
