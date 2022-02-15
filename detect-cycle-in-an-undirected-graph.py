def isCyclicUtil(v,visited,parent,adj):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            if isCyclicUtil(i,visited,v,adj):
                return True
        elif parent!=i:
            return True
    return False
    
class Solution:
    
    #Function to detect cycle in an undirected graph.

    def isCycle(self, V, adj):
        #Code here
        visited = [False]*V
        for i in range(V):
            if visited[i] == False:
                if isCyclicUtil(i,visited,-1,adj) :
                    return True
        return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
