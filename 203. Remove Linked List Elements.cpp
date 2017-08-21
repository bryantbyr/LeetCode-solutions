//203. Remove Linked List Elements.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Creatde by bryantbyr on 20170821
//Time:O(n)
//Space:O(1)
//Linked List (remove)
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* h = head;
        ListNode* pre = head;
        int k = 1;//判断链表是否每个节点的值都一样
        while (h != NULL) {
            if (h->val == val) {
                if (h->next != NULL){//删除节点
                    ListNode* t = h->next;
                    *h = *h->next;
                    delete t;
                }
                else {
                    pre->next = NULL;
                    break;
                }
            }
            else {
                pre = h;
                h = h->next;
                k = 0;
            }
        }
        return k == 1 ? NULL : head;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    for (int i = 1; i < 5; ++i)
    {
        ListNode* n1 = new ListNode(i);
        h1->next = n1;
        h1 = n1;
    }
    l1 = s.removeElements(l1, 4);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
