//328-Odd Even Linked List.cpp

#include<iostream>
using namespace std;

//2017/03/19
//Time:O(N)
//Space:O(1)
//data struct:list basic function
struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
    ListNode* oddEvenList(ListNode* head)
    {
    	if(!head)
    		return NULL;
        ListNode* headOdd=head;
        ListNode* headEven=head->next;
        if(!headEven)
        	return head;
        ListNode* n=headEven;
        ListNode* t1=headEven->next;
        while(t1){
            headOdd->next=t1;
            headOdd=t1;
            ListNode* t2=t1->next;
            if(t2){
                headEven->next=t2;
                headEven=t2;
                t1=t2->next;
            }
            else
                break;
        }
        headOdd->next=n;
        headEven->next=NULL;

        return head;
    }
};

int main()
{
    Solution s;
    ListNode* p=new ListNode(1);
    ListNode* head=p;
    for(int i=2;i<5;i++){
        ListNode* s=new ListNode(i);
        p->next=s;
        p=s;
    }

    ListNode* newHead=s.oddEvenList(head);
    while(newHead){
        cout<<newHead->val<<endl;
        newHead=newHead->next;
    }

    return 0;
}
