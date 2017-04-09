//206-Reverse Linked List.cpp

#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//2017/03/19
//Time:O(N)
//Space:O(1)
//iteration
class Solution{
public:
     ListNode* reverseList(ListNode* head)
     {
        ListNode* prev=NULL;
        while(head){
            ListNode* t=head->next;
            head->next=prev;
            prev=head;
            head=t;
        }

        return prev;
     }
};


int main()
{
    Solution s;
    ListNode* L=new ListNode(-1);
    ListNode* h=L;
    for(int i=0;i<7;i++){
        ListNode* l=new ListNode(i);
        L->next=l;
        L=l;
    }

    ListNode* r=s.reverseList(h);
    while(r){
        cout<<r->val<<endl;
        r=r->next;
    }
    return 0;
}

