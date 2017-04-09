//79--Word Search(BackTracking).cpp

#include <iostream>
#include <vector>
using namespace std;

//2017/03/26
//Time:O(M*N*4^K)
//Space:O(M*N)
//经典回溯案例(此题遇到了一定障碍，中间几个提交版本详见LeetCode上的submission)
class Solution{
public:
     bool exist(vector<vector<char>>& board, string word)
     {
        if(board.size()==0||board[0].size()==0)
            return false;

        int m=board.size();
        int n=board[0].size();
        int** b=new int*[m];
        for(int i=0;i<m;i++)
            b[i]=new int[n];
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                b[i][j]=false;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(BackTracking(board,b,i,j,word,0)){
                	for(int k=0;k<m;k++)
                		delete[] b[k];
                	delete[] b;
                    return true;
				}
            }
        }
        return false;
     }

     bool BackTracking(vector<vector<char>>& board,int** b,int m,int n,string s,int pos)
     {
        if(m>=board.size()||m<0||n<0||n>=board[0].size()||pos>=s.size()||board[m][n]!=s[pos]||b[m][n])
            return false;

		b[m][n] = true;
		if (pos == s.size()-1 )
			return true;

		if (BackTracking(board, b, m + 1, n, s, pos + 1) || BackTracking(board, b, m - 1, n, s, pos + 1)
		|| BackTracking(board, b, m, n + 1, s, pos + 1) || BackTracking(board, b, m, n - 1, s, pos + 1))
			return true;

		b[m][n] = false;
		return false;
     }
};

int main()
{
    Solution s;
    vector<vector<char>> v;
	v = { { 'S', 'A','C','A' }, { 'F', 'E', 'D','A' }, { 'A','Y', 'A','A'} };

    cout<<s.exist(v,"SAEYAS")<<endl;

    return 0;
}
