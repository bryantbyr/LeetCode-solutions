//PascalTriangle.java

import java.util.ArrayList;
import java.util.List;

//Created by bryantbyr on 20171005
//Time:O(n)
//Space:O(1)
//array
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < numRows ; ++i ) {
            List<Integer> temp = new ArrayList<Integer>();
            temp.add(1);
            for (int j = 1; j < i; j++)
                temp.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
            if (i != 0)
                temp.add(1);
            res.add(temp);
        }
        return res;
    }
}

//Created by bryantbyr on 20171005
//Time:O(n)
//Space:O(1)
//array (java: List.clear() VS new List())
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i < numRows ; ++i ) {
            // temp.clear();
            temp = new ArrayList<Integer>();
            temp.add(1);
            for (int j = 1; j < i; j++)
                temp.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
            if (i != 0)
                temp.add(1);
            res.add(temp);
        }
        return res;
    }
}

//Learn from discuss on 20171005
//Time:O(n)
//Space:O(1)
//array (java: new ArrayList<Integer>(list))
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> allrows = new ArrayList<List<Integer>>();
        ArrayList<Integer> row = new ArrayList<Integer>();
        for (int i = 0; i < numRows; i++) {
            row.add(0, 1);
            for (int j = 1; j < row.size() - 1; j++)
                row.set(j, row.get(j) + row.get(j + 1));
            allrows.add(new ArrayList<Integer>(row));// Note!
        }
        return allrows;
    }
}

//Created by bryantbyr on 20171005
//Time:O(n)
//Space:O(1)
//array (java: new ArrayList<Integer>(list) + List.clear())
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i < numRows ; ++i ) {
            temp.clear();
            // temp = new ArrayList<Integer>();
            temp.add(1);
            for (int j = 1; j < i; j++)
                temp.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
            if (i != 0)
                temp.add(1);
            res.add(new ArrayList<Integer>(temp));
        }
        return res;
    }
}

public class PascalTriangle {
    public static void main(String[] args) {
        Solution S = new Solution();
        List<List<Integer>> r = S.generate(4);
        for (int i = 0; i < r.size(); ++i) {
            for (int j = 0; j < r.get(i).size(); ++j)
                System.out.println(r.get(i).get(j));
        }
    }
}
