/*
 * [158] Read N Characters Given Read4 II - Call multiple times
 *
 * https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times
 *
 * Hard (24.16%)
 * Total Accepted:    
 * Total Submissions: 
 * Testcase Example:  '""\n[read(0)]'
 *
 * 
 * The API: int read4(char *buf) reads 4 characters at a time from a file.
 * 
 * 
 * 
 * The return value is the actual number of characters read. For example, it
 * returns 3 if there is only 3 characters left in the file.
 * 
 * 
 * 
 * By using the read4 API, implement the function int read(char *buf, int n)
 * that reads n characters from the file.
 * 
 * 
 * 
 * Note:
 * The read function may be called multiple times.
 * 
 */
// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        
    }
};
