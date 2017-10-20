//_537_Complex_Number_Multiplication.cpp

//Created by bryantbyr on 20171020
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String complexNumberMultiply(String a, String b) {
        int a1 = 0, b1 = 0, sa1 = 1, sb1 = 1;
        boolean flag1 = true;
        for (char c : a.toCharArray() ) {
            if (flag1 && c == '-') {
                sa1 = -1;
            } else if (flag1 && c != '+') {
                a1 = a1 * 10 + (c - '0');
            } else if (c == '+') {
                a1 *= sa1;
                flag1 = false;
            } else if (c == '-') {
                sb1 = -1;
            } else if (c != 'i') {
                b1 = b1 * 10 + (c - '0');
            } else if (c == 'i') {
                b1 *= sb1;
            }
        }
        int a2 = 0, b2 = 0, sa2 = 1, sb2 = 1;
        boolean flag2 = true;
        for (char c : b.toCharArray()) {
            if (flag2 && c == '-') {
                sa2 = -1;
            } else if (flag2 && c != '+') {
                a2 = a2 * 10 + (c - '0');
            } else if (c == '+') {
                a2 *= sa2;
                flag2 = false;
            } else if (c == '-') {
                sb2 = -1;
            } else if (c != 'i') {
                b2 = b2 * 10 + (c - '0');
            } else if (c == 'i') {
                b2 *= sb2;
            }
        }
        String res;
        int A = a1 * a2 - b1 * b2, B = a1 * b2 + a2 * b1;
        res = A + "+" + B + "i";
        return res;
    }
}

//Created by bryantbyr on 20171020
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String complexNumberMultiply(String a, String b) {
        String a1 = "", b1 = "", a2 = "", b2 = "";
        for (int i = 0; i < a.length() ; ++i) {
            if (a.charAt(i) == '+') {
                a1 = a.substring(0, i);
                b1 = a.substring(i + 1, a.length() - 1);
                break;
            }
        }
        for (int i = 0; i < b.length() ; ++i) {
            if (b.charAt(i) == '+') {
                a2 = b.substring(0, i);
                b2 = b.substring(i + 1, b.length() - 1);
                break;
            }
        }
        int resA = Integer.parseInt(a1) * Integer.parseInt(a2) - Integer.parseInt(b1) * Integer.parseInt(b2),
            resB = Integer.parseInt(a1) * Integer.parseInt(b2) + Integer.parseInt(a2) * Integer.parseInt(b1);
        return resA + "+" + resB + "i";
    }
}

//Learn from discuss on 20171020
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String complexNumberMultiply(String a, String b) {
        String[] A = a.split("\\+");
        String[] B = b.split("\\+");
        int resA = Integer.parseInt(A[0]) * Integer.parseInt(B[0]) - Integer.parseInt(A[1].replace("i", "")) * Integer.parseInt(B[1].replace("i", "")),
            resB = Integer.parseInt(A[0]) * Integer.parseInt(B[1].replace("i", "")) + Integer.parseInt(B[0]) * Integer.parseInt(A[1].replace("i", ""));
        return resA + "+" + resB + "i";
    }
}

public class _537_Complex_Number_Multiplication {
    public static void main(String[] args) {
        Solution S = new Solution();
        String A = "1+-1i", B = "1+-1i";
        System.out.println(S.complexNumberMultiply(A, B));
    }
}
