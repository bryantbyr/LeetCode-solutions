//21. Merge Two Sorted Lists.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170820
//Time:O(m+n)
//Space:O(1)
//Linked List(Merge Sorted List: 2 methods mainly of space O(1) or O(m+n))
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* h = l1; //h用作记录合并之后List的头结点
        ListNode* t = NULL; //t用来记录待插入节点的上一个相邻节点
        ListNode* s = NULL; //s用来记录待插入节点
        while (l2 != NULL) {
            while (l1 != NULL) {
                if (l2->val > l1->val) {//决定插入l1的位置
                    t = l1; //修改上一个相邻节点
                    l1 = l1->next; //向前移动l1当前节点
                }
                else
                    break;
            }
            if (t != NULL) {//连接上一个相邻节点
                t->next = l2;
                t = t->next;
            }
            else if (s == NULL) //修改头节点
                h = l2;
            s = l2; //连接下一个节点并向前移动l2当前节点
            l2 = l2->next;
            s->next = l1;
            t = s; //修改上一个相邻节点
        }
        return h;
    }
};

int main()
{
    Solution S;
    ListNode* h1 = new ListNode(5);
    ListNode* l1 = h1;
    for (int i = 0; i < 4; ++i)
    {
        ListNode* n1 = new ListNode(i + 3);
        h1->next = n1;
        h1 = n1;
    }
    ListNode* h2 = new ListNode(1);
    ListNode* l2 = h2;
    for (int i = 2; i < 5; ++i)
    {
        ListNode* n2 = new ListNode(i);
        h2->next = n2;
        h2 = n2;
    }
    ListNode* h = S.mergeTwoLists(l1, l2);
    while (h != NULL) {
        cout << h->val << endl;
        h = h->next;
    }
}
