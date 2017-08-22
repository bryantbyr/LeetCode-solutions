//86. Partition List.cpp
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
//Linked List (partition) (+ Two Pointer)
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* h = head;
        ListNode *h1 = NULL, *h2 = NULL;
        ListNode *H1 = NULL, *H2 = NULL;
        while (h != NULL) {
            if (h->val < x) {
                if (h1 == NULL)
                    // H1=h;
                    // h1=h;
                    h1 = H1 = h;
                else
                    // h1->next=h;
                    // h1=h;
                    h1 = h1->next = h;
            }
            else {
                if (h2 == NULL)
                    h2 = H2 = h;
                else
                    h2 = h2->next = h;
            }
            h = h->next;
        }
        if (h1 != NULL)
            h1->next = H2;
        if (h2 != NULL)
            h2->next = NULL;
        return H1 == NULL ? H2 : H1;
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
    l1 = s.partition(l1, 3);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
