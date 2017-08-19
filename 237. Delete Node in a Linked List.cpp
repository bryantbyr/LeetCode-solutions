//237. Delete Node in a Linked List.cpp
#include <iostream>
#include <vector>
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//Learn from discuss on 20170819
//Time:O(1)
//Space:O(1)
//Linked List + C++ Pointer
class Solution {
public:
    void deleteNode(ListNode* node) {
        *node=*node->next;
        //node=node->next;
        //node->next=node->next->next;
        /*
        注意上面3种写法的区别和效果
        (指针作形参时,仅操作地址(指针)指向(关联)的内容具有传引用效果)
         */
    }
};

int main()
{
    Solution s;
    ListNode* h = new ListNode(0);
    ListNode* l = h;
    for (int i = 1; i < 5; i++) {
        ListNode* n = new ListNode(i);
        h->next = n;
        h = n;
    }
    s.deleteNode(l);
    while (l != NULL) {
        cout << l->val << endl;
        l = l->next;
    }
}
