//445-Add Two Numbers II.cpp

#include<iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


//2017/03/19
//Time:O(N)
//Space:O(N)
//Brute Force
class Solution{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* L1=reverseList(l1);
        ListNode* L2=reverseList(l2);

        ListNode* L;
        ListNode* p=new ListNode(0);
        ListNode* r=p;
        int temp=0;
        while(L1||L2){
            L=new ListNode(temp);
            p->next=L;
            p=L;
            if(L1){
                L->val=(L->val+L1->val)%10;
                temp=L1->val+temp;
                L1=L1->next;
            }
            if(L2){
                L->val=(L->val+L2->val)%10;
                temp=temp+L2->val;
                L2=L2->next;
            }
            temp/=10;
        }
        if(temp)
            L->next=new ListNode(temp);

        return reverseList(r->next);
    }
    ListNode* reverseList(ListNode* l)
    {
        ListNode* prev=NULL;
        while(l){
            ListNode* temp=l->next;//be verified
            l->next=prev;
            prev=l;
            l=temp;
        }
        return prev;
    }

};

int main()
{
    Solution s;
    ListNode l1(9);
    l1.next=new ListNode(9);
    //l1.next->next=new ListNode(4);
    //l1.next->next->next=new ListNode(3);

    ListNode l2(1);
    //l2.next=new ListNode(6);
    //l2.next->next=new ListNode(4);

    ListNode* l=s.addTwoNumbers(&l1,&l2);

    while(l){
        cout<<l->val<<endl;
        l=l->next;
    }

    return 0;
}
