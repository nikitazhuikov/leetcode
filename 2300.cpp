class Solution {
    public:
        vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
            int n = spells.size();
            int m = potions.size();
            vector<int> pairs(n);
            
            sort(potions.begin(), potions.end());
            
            for (int i = 0; i < n; i++) {
                long long minPotion = (success + spells[i] - 1) / spells[i];
                
                // Ручной бинарный поиск
                int left = 0, right = m;
                while (left < right) {
                    int mid = left + (right - left) / 2;
                    if (potions[mid] < minPotion) {
                        left = mid + 1;
                    } else {
                        right = mid;
                    }
                }
                
                pairs[i] = m - left;
            }
            
            return pairs;            
        }
    };