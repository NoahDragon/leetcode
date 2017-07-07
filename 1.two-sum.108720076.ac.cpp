class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = nums.size(), i, j;
        vector<int> r(2);
        
        for(i = 0; i < l; i ++)
            for(j = i+1; j < l; j ++){
                if(nums[i] + nums[j] == target){
                    r = {i, j};
                    goto exit;
                }
            }
        
    exit:
        return r;
    }
};