//141. Linked List Cycle.cpp
#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//20170819
//Time:O(n)
//Space:O(1)
//Two Pointers + linked list
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL)
            return false;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
                return true;
        }
        return false;
    }
};

int main()
{
    Solution s;
    ListNode* h = new ListNode(0);
    ListNode* l = h;
    for (int i = 1; i < 5; i++) {
        ListNode* n = new ListNode(i);
        l->next = n;
        l = n;
    }
    // l=h;
    // while(l!=NULL){
    //     cout<<l->val<<endl;
    //     l=l->next;
    // }
    cout << s.hasCycle(h) << endl;

}
