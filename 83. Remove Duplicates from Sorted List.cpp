//83. Remove Duplicates from Sorted List.cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170820
//Time:O(n)
//Space:O(1)
//Linked List + C++ Pointer
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL)
            return NULL;
        if (head->next != NULL && head->next->val == head->val)//保留头结点
            head = head->next;
        ListNode* t = head;
        while (t->next != NULL) {
            if (t->next->val == t->val) {//注意删除的是那一个位置的节点
                ListNode* s = t;
                *s = *s->next;
                t = s;//不能写成t = t->next;
            }
            else
                t = t->next;
        }
        return head;
    }
};

int main()
{
    Solution s;
    ListNode* h = new ListNode(0);
    ListNode* l = h;
    for (int i = 1; i < 6; i++) {
        ListNode* n = new ListNode(i);
        h->next = n;
        h = n;
    }
    h = s.deleteDuplicates(l);
    while (h != NULL) {
        cout << h->val << endl;
        h = h->next;
    }

}
