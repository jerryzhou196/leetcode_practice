#include <stdio.h>
#include <vector>

using namespace std;
// m = number of rows
// n = number of columns 

class Solution {
public:
    int numIslands(vector<vector<char> >& grid) {
        int count = 0;
        const int m = grid.size();
        const int n = grid[0].size();  

        vector<vector<bool> > seen(m, vector<bool> (n,0));
        for (int y = 0; y < m; y++){
            for (int x = 0; x < n; x++){
                if (!seen[y][x] && grid[y][x] == '1'){
                    count++;
                    mapIsland(x,y,seen,grid,m,n);
                }
            }
        }
        return count;
    }
    
    void mapIsland(int x, int y, vector<vector<bool>> &seen, vector<vector<char> >&grid, int m, int n){
        seen[y][x] = true; 
        if (isValid(x-1,y,seen,grid,m,n)){
            mapIsland(x-1,y,seen,grid,m,n);
        }        
        if (isValid(x+1,y,seen,grid,m,n)){//x+1, y
            mapIsland(x+1,y,seen,grid,m,n);
        }   
        if (isValid(x,y-1,seen,grid,m,n)){//x, y-1
            mapIsland(x,y-1,seen,grid,m,n);
        }
        if (isValid(x,y+1,seen,grid,m,n)){//x, y+1 
            mapIsland(x,y+1,seen,grid,m,n);
        }
    }

    bool isValid(int x, int y, vector<vector<bool>> &seen, vector<vector<char> >&grid, int m, int n){
        return (x >= 0 && x < n && y >= 0 && y < m && (grid[y][x] == '1') && !(seen[y][x]));
    }
};

int main(){
    Solution s;
    vector<vector<char> > vec{ {'1','1','1','1','0'}, 
                         { '1','1','0','1','0'}, 
                         {'1','1','0','0','0'},
                         {'0','0','0','0','1'} }; 
    printf("number of islands: %d", s.numIslands(vec));
    return 0;
}