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
        for (int y = 0; y < m; y++){
            for (int x = 0; x < n; x++){
                if (grid[y][x] == '1'){
                    count++;
                    mapIsland(x,y,grid,m,n);
                }
            }
        }
        return count;
    }
    
    void mapIsland(int x, int y, vector<vector<char> >&grid, int m, int n){
        if (!(x >= 0 && x < n && y >= 0 && y < m && (grid[y][x] == '1'))){
            return;
        };
        grid[y][x] = '0'; 
        mapIsland(x-1,y,grid,m,n); 
        mapIsland(x+1,y,grid,m,n);
        mapIsland(x,y-1,grid,m,n);
        mapIsland(x,y+1,grid,m,n);
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