class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        int i1 = -1, i2 = -1, // Index for median
            l1 = 0, l2 = 0, // Index for loop
            r1, r2,
            temp;
        vector<int> a;
            
        i1 = (m + n)/2 + 1;
        if ( (m + n)%2 == 0)
            i2 = i1 - 1;
        
        while(l1 < m || l2 < n){
            if( (l1 < m ? nums1[l1] : INT_MAX) <= (l2 < n ? nums2[l2] : INT_MAX) ){
                temp = nums1[l1];
                l1 ++;
            } else {
                temp = nums2[l2];
                l2 ++;
            }
            
            
            if (i2 != -1 && l1 + l2 == i2) {
                r2 = temp;
            }
            
            if (l1 + l2 == i1) {
                r1 = temp;
                break;
            }
        }
        
        return i2 != -1 ? (r1 + r2) / 2.0 : r1;
    }
};