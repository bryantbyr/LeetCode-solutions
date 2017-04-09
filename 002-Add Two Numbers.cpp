//002-Add Two Numbers.cpp

#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//2017/03/18
//Time:O(N)
//Space:O(N)
//Brute Force
class Solutiuon{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3;
        ListNode* t=new ListNode(0);
        ListNode* s=new ListNode(0);//用于串联节点
    
        int temp=0;
        l3=new ListNode((temp+l1->val+l2->val)%10);
        s=l3;
        t=s;//注意赋值变化
        temp=(temp+l1->val+l2->val)/10;
        l1=l1->next;
        l2=l2->next;
        while(l1&&l2){
        	l3=new ListNode((temp+l1->val+l2->val)%10);
            s->next=l3;
            s=l3;
            temp=(temp+l1->val+l2->val)/10;
            l1=l1->next;
            l2=l2->next;
        }
        while(l1){
            l3=new ListNode((l1->val+temp)%10);
            s->next=l3;
            s=l3;
            temp=(l1->val+temp)/10;
            l1=l1->next;
        }
        while(l2){
            l3=new ListNode((l2->val+temp)%10);
            s->next=l3;
            s=l3;
            temp=(l2->val+temp)/10;
            l2=l2->next;
        }
        if(temp){
    		l3=new ListNode(temp);
            s->next=l3;
        }
        return t;
    }
};

int main()
{
    Solutiuon s;
    ListNode l1(2);
    l1.next=new ListNode(4);
    l1.next->next=new ListNode(3);
    l1.next->next->next=new ListNode(3);

    ListNode l2(5);
    l2.next=new ListNode(6);
    l2.next->next=new ListNode(4);

    ListNode* l=s.addTwoNumbers(&l1,&l2);

    while(l){
        cout<<l->val<<endl;
        l=l->next;
    }

    return 0;
}
