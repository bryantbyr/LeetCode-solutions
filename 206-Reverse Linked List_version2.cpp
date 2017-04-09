//206-Reverse Linked List_version2.cpp


#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution{
public:
     ListNode* reverseList(ListNode* head)
     {
     	if(!head)
     		return NULL;
        if(!head->next)
            return head;
        ListNode* r=reverseList(head->next);
        head->next=NULL;
        ListNode* t=r;
        
        while(t){
            if(!t->next){
                t->next=head;
                break;
            }
        	t=t->next;
        }
        
//        while(t)
//        	t=t->next;
//        t=head;
        
//        while(t){
//        cout<<t->val<<endl;
//        t=t->next;
//    }
        return r;
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
