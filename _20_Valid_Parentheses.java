//_20_Valid_Parentheses.java
import java.util.Stack;

//Created by bryantbyr on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '{' || c == '[' || c == '(')
                stack.push(c);
            else if (c == ')' && (stack.isEmpty() || stack.pop() != '('))
                return false;
            else if (c == ']' && (stack.isEmpty() || stack.pop() != '['))
                return false;
            else if (c == '}' && (stack.isEmpty() || stack.pop() != '{'))
                return false;
        }
        return stack.isEmpty();
    }
}

//Learn from discuss on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '[')
                stack.push(']');
            else if (c == '{')
                stack.push('}');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }
}

public class _20_Valid_Parentheses {
    public static void main(String[] args) {
        Solution S = new Solution();
        String s = "()[]{}";
        System.out.println(S.isValid(s));
    }
}
