//24. Swap Nodes in Pairs.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170821
//Time:O(n)
//Space:O(1)
//Linked List (swap nodes) : 改变地址对应节点的内容
// class Solution {
// public:
//     ListNode* swapPairs(ListNode* head) {
//         ListNode* h=head;
//         ListNode* s=NULL;
//         ListNode* t=new ListNode(0);
//         while(h!=NULL&&h->next!=NULL){
//             *t=*h;
//             s=h->next;
//             *h=*s;
//             *s=*t;
//             s->next=h->next;
//             h->next=s;
//             h=s->next;
//         }
//         return head;
//     }
// };

//Created by bryantbyr on 20170821
//Time:O(n)
//Space:O(1)
//Linked List (swap) : 仅改变节点链接方式
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL||head->next==NULL)
            return head;
        ListNode* h=head;
        ListNode* r=h->next;
        ListNode* s=NULL;
        ListNode* t=NULL;
        while(h!=NULL&&h->next!=NULL){
            s=h->next;
            if(s->next!=NULL&&s->next->next!=NULL)
                h->next=s->next->next;
            else
                h->next=s->next;
            t=s->next;
            s->next=h;
            h=t;
        }
        return r;
    }
};


int main()
{
    Solution s;
    ListNode* h1 = new ListNode(0);
    ListNode* l1 = h1;
    for (int i = 1; i < 5; ++i)
    {
        ListNode* n1 = new ListNode(i);
        h1->next = n1;
        h1 = n1;
    }
    l1 = s.swapPairs(l1);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
