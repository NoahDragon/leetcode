/**
 * https://leetcode.com/problems/powx-n  
 * Medium (26.45%) 
 * Testcase Example:  '8.88023\n3' 
 * Implement pow(x, n).
 */
class Solution {
public:
    double myPow(double x, int n) {
	double y = x;
	
	if ( n == 0)
		return 1;

	if ( x == 1.0)
		return 1.0;

	if ( x == -1.0){
		if(n%2 == 0)
			return 1;
		else
			return -1.0;
	}

	if ( n > 0 ){
    		for(int i = 0; i < n-1; i++){
			y *= x;
			if ( y == 0.0)
				break;
		}
	}

	if ( n < 0 ) {
		n = -n;
		for (int i = 0; i < n-1; i++){
			y *= x;
			if ( 1.0/y == 0.0)
				break;
		}
		y = 1.0/y;
	}

	return y;
    }
};
