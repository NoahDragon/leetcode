/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * 
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        char t;
        
        for(char& c : s){
            if (c == '(' || c == '{' || c == '['){
                st.push(c);
            } else {
                if (st.size() != 0){
                    t = st.top();
                    st.pop(); 
                } else {
                    return false;
                }
                
                if((c == ')' && t == '(') || (c == '}' && t == '{') || (c == ']' && t == '[')){
                    continue;
                } else {
                    return false;
                }
            }
        }

        if (st.size() == 0)
            return true;
        else
            return false;
    }
};
