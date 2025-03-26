class Solution {
    public:
        int minOperations(vector<vector<int> >& grid, int x) {
    
            int result =0;
             
            vector<int>arr;
            for(int i=0;i<grid.size();i++){
                for( int j=0;j<grid[0].size();j++)
                    arr.push_back(grid[i][j]);
            }
    
            int len = arr.size();
            nth_element(arr.begin(),arr.begin() + len/2,arr.end());
            int median = arr[len/2];
            for (int num : arr){
                if(num % x != median % x) return - 1;
                result +=abs(median-num)/x;
            }
             
            return result;
        }
    };