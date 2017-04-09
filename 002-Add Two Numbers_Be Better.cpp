//002-Add Two Numbers_Be Better.cpp

#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solutiuon{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* L=new ListNode(0);
        ListNode* t=new ListNode(0);
        ListNode* p=new ListNode(0);//用于串联节点

        p=L;
        t=p;//注意赋值变化
        int temp=0;
        while(l1||l2){
            L=new ListNode(temp);
            p->next=L;
            p=L;
            if(l1){
                L->val=(L->val+l1->val)%10;
                temp=l1->val+temp;
                l1=l1->next;
            }
            if(l2){
                L->val=(L->val+l2->val)%10;
                temp=temp+l2->val;
                l2=l2->next;
            }
            temp/=10;
        }
        if(temp)
            L->next=new ListNode(temp);
        return t->next;
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
