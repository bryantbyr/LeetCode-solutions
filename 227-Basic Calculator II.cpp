//227-Basic Calculator II.cpp
#include<iostream>
#include<string>
using namespace std;

class Solution
{
    public:
        long calculate(string s)
        {
			//replace(s);
			unsigned int i = 0;
			int count = 0;
			int key = 0;
			while (i < s.size() && s[i])
			{
				while (s[i] == ' ')
				{
					count++;
					key = 1;
					i++;
				}
				if (key==1)
					s.erase(i-count, count);
				i = i - count;
				i++;
				count = 0;
				key = 0;
			}
			
			//long cur = s[0]-'0';//当前结果
			long cur = getNum(0,s);
			//char prev = s[0];
			long prev = cur;
			long n=cur;
			char prec=NULL;
			int k=length(cur);
			long precur;
			while (k < s.size())
			{
				char c = s[k];
				if (c == '+')
				{
					//n = s[k + 1];
					n = getNum(k + 1, s);
					cur += n;
					prev = n;
					prec = c;
				}
				else if (c == '-')
				{
					//n = s[k + 1];
					n = getNum(k + 1, s);
					cur -= n;
					prev = n;
					prec = c;
				}
				else if (c == '*')
				{
					//n = s[k + 1];
					n = getNum(k + 1, s);
					
					if (prec == '+' || prec == NULL)
					{
						precur = cur-prev;
						cur = cur - prev  + prev*n;
					}	
					else if (prec == '-' || prec == NULL)
					{
						precur = cur + prev;
						cur = cur + prev - prev*n;
					}
					else if (prec == '*')
						cur = (cur - precur)*n + precur;
					else if (prec == '/')
						cur = (cur - precur) * n + precur;
					prev = n;
					prec = c;
				}
				else if (c == '/')
				{
					//n = s[k + 1];
					n = getNum(k + 1, s);
					if (prec == '+' || prec == NULL)
					{
						precur = cur - prev;
						cur = cur - prev + prev / n;
					}
					else if (prec == '-')
					{
						precur = cur + prev;
						cur = cur + prev - prev / n;
					}
					else if (prec == '*')
						cur = (cur - precur)/n+precur;
					else if (prec == '/')
						cur = (cur - precur) / n + precur;
					prev = n;
					prec = c;
				}
				if (k == 0)
					k = 1;
				else
				    k+=(length(n)+1);
			}

			return cur;
		}
		long getNum(int n,string s)
		{
			long t = s[n]-'0';
			n++;
			while (n < s.size() && '0' <= s[n] &&s[0]<= '9')//..............
			{
				t = t * 10 + (s[n] - '0');
				n++;
			}
			return t;
		}
		int length(int n)
		{
			int i = 1;
			while (n / 10 != 0)
			{
				i++;
				n = n / 10;
			}
			return i;
		}
};

int main()
{
	Solution s;
	//cout << s.calculate("1+2 * 5 / 3 ") << endl;
	cout << s.calculate("1+900 + 2 * 5 / 3 + 6 / 4 * 2*3") << endl;
	return 0;
}
