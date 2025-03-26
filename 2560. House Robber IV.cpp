#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minCapability(vector<int>& A, int k) {
        int l = *min_element(A.begin(), A.end());
        int r = *max_element(A.begin(), A.end());

        while (l < r) {
            int m = (l + r) / 2;
            int last = 0, take = 0;

            for (int a : A) {
                if (last) {
                    last = 0;  // Skip adjacent house
                    continue;
                }
                if (a <= m) {
                    take++;
                    last = 1;  // Mark as robbed
                }
            }

            if (take >= k) {
                r = m;  // Try smaller max capability
            } else {
                l = m + 1;  // Increase capability
            }
        }

        return l;
    }
};