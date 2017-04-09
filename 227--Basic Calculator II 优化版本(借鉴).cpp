#include<iostream>
#include<string>
using namespace std;

class Solutioin{
	public:
		int calculate(string s)
		{
			replacee(s);
			unsigned int i = 0;
			long cur = getNum(i, s);
			long prev = cur;
			char c;
			long n;
			while (i < s.size())
			{
				c = s[i];
				i++;
				n = getNum(i, s);
				if (c == '+')
				{
					cur += n;
					prev = n;
				}
				else if (c == '-')
				{
					cur -= n;
					prev = -n;
				}
				else if (c == '*')
				{
					cur = cur - prev + prev*n;
					prev = prev*n;
				}
				else if (c == '/')
				{
					cur = cur - prev + prev / n;
					prev = prev / n;
				}
			}
			return cur;
		}

		void replacee(string& s)
		{
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
				if (key == 1)
					s.erase(i - count, count);
				i = i - count;
				i++;
				count = 0;
				key = 0;
			}
		}
		long getNum(unsigned int& i, string& s)
		{
			unsigned int pos = i;
			long res = 0;
			while (pos < s.size() && isDigit(s[pos]))
			{
				res = res * 10 + s[pos] - '0';
				pos++;
			}
			i = pos;
			return res;
		}
		bool isDigit(char c)
		{
			if ('0' <= c&&c <= '9')
				return 1;
			else
				return 0;
		}
};

int main()
{
	Solutioin s;
	cout<<s.calculate("42")<<endl;
	return 0;
}

