//82. Remove Duplicates from Sorted List II.cpp
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
//Linked List (general remove)
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode node(0);// a useful skill
        ListNode* h = &node;
        h->next = head;
        while (h->next != NULL && h->next->next != NULL) {
            ListNode* t = h->next;
            while (t->next != NULL && t->val == t->next->val) {
                ListNode* s = t;
                t = t->next;
                delete s;
            }
            if (t == h->next)
                h = h->next = t;
            else {
                h->next = t->next;
                delete t;
            }
        }
        return node.next;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    ListNode* n1 = new ListNode(1);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(2);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(3);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(4);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(4);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(5);
    h1->next = n1;
    l1 = s.deleteDuplicates(l1);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
