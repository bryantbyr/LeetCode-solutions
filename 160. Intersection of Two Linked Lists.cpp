//160. Intersection of Two Linked Lists.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Learn From Discuss on 20170821
//Time:O(m+n)
//Space:O(1)
//Linked List + Two Pinters
//Hint:If the two linked lists have an intersection,it will end at the end of both List A and List B
// class Solution {
// public:
//     ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
//         ListNode* t1 = headA;
//         ListNode* t2 = headB;
//         while (t1 != t2) {
//             t1 = t1 ? t1->next : headB;
//             t2 = t2 ? t2->next : headA;
//         }
//         return t1;
//     }
// };

//Created by bryantbyr on 20170821
//Time:O(m+n)
//Space:O(1)
//Simple Loop
//Hint:If the two linked lists have an intersection,it will end at the end of both List A and List B
// class Solution {
// public:
//     int getLength(ListNode* head) {
//         int r = 0;
//         while (head != NULL) {
//             r++;
//             head = head->next;
//         }
//         return r;
//     }
//     ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
//         ListNode* t1 = headA;
//         ListNode* t2 = headB;
//         int l1 = getLength(t1);
//         int l2 = getLength(t2);
//         while (l1 > l2) {
//             headA = headA->next;
//             l1--;
//         }
//         while (l1 < l2) {
//             headB = headB->next;
//             l2--;
//         }
//         while (headA != NULL && headB != NULL) {
//             if (headA == headB)
//                 return headA;
//             headA = headA->next;
//             headB = headB->next;
//         }
//         return NULL;
//     }
// };

//Created by bryantbyr on 20170821
//Time:O(m+n)
//Space:O(1)
//Two Pointers
//Hint:The two linked lists can be any ones
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* t1 = headA;
        ListNode* t2 = headB;
        if(t1==NULL||t2==NULL)
            return NULL;
        int k=0;
        while ((t1 == NULL && t2 == NULL) || t1 != t2) {
            t1 = t1 ? t1->next : headB;
            t2 = t2 ? t2->next : headA;
            if(t1==NULL&&t2==NULL)
                k++;
            if(k==2)
                return NULL;
        }
        return t1;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    ListNode* h2 = new ListNode(1);
    ListNode* l2 = h2;
    for (int i = 1; i < 3; ++i)
    {
        ListNode* n1 = new ListNode(i);
        h1->next = n1;
        h1 = n1;
        h2->next = h1;
        h2 = n1;
    }
    // for (int i = 1; i < 3; ++i)
    // {
    //     ListNode* n2 = new ListNode(i);
    //     h2->next = n2;
    //     h2 = n2;
    // }
    ListNode* r = s.getIntersectionNode(l1, l2);
    if (r != NULL)
        cout << r->val << endl;
    else
        cout << "NULL" << endl;
}
