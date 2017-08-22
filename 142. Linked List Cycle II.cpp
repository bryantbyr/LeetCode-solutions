//142. Linked List Cycle II.cpp
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
//Linked List + Two Pointers
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL)
            return NULL;
        ListNode* first = head;
        ListNode* second = head;
        ListNode* third = head;
        while (second != NULL && second->next != NULL) {
            second = second->next->next;
            first = first->next;
            if (second == first)
                break;
        }
        if (second != first)
            return NULL;
        while (first != third) {
            first = first->next;
            third = third->next;
        }
        return first;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    ListNode* n1 = new ListNode(4);
    h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(3);
    // h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(2);
    // h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(5);
    // h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(2);
    // h1->next = n1;
    l1 = s.detectCycle(l1);
    if (l1 != NULL)
        cout << l1->val << endl;
    else
        cout << "l1=NULL" << endl;
}
