//92. Reverse Linked List II.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170822
//Time:O(n)
//Space:O(1)
//Linked List (general reverse)
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == NULL)
            return NULL;
        ListNode* h = head;
        ListNode* t = NULL;
        ListNode* s = NULL;
        ListNode* H =  NULL;
        for (int i = 1; i <= n; ++i)
        {
            if (i < m) {
                t = h;
                h = h->next;
            }
            else {
                s = h->next;
                h->next = H;
                H = h;
                h = s;
            }
        }
        if (t != NULL) {
            ListNode* p = t->next;
            t->next = H;
            p->next = h;
        }
        else
            head->next = h;
        return t == NULL ? H : head;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    ListNode* n1 = new ListNode(4);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(3);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(2);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(5);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(2);
    h1->next = n1;
    l1 = s.reverseBetween(l1, 2, 4);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
