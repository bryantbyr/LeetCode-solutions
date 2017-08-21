//19. Remove Nth Node From End of List.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170821
//Time:O(n)
//Sapce:O(1)
//Linked List (delete (c++ pointer)) delete释放指针ptr指向的内存空间后,ptr的值不变,最好令ptr=NULL
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
//     ListNode* removeNthFromEnd(ListNode* head, int n) {
//         ListNode* h = head;
//         ListNode* t = NULL;
//         int pos = getLength(head) - n + 1;
//         if (pos - 1 < 0 || n < 1)
//             return head;
//         for (int i = 0; i < pos - 1; ++i) {//find the node
//             t = h;
//             h = h->next;
//         }
//         if (h->next != NULL)//delete the node  无法通过某个指针改变其他所有同级指针的值,因此引入t
//             *h = *h->next;
//         else {
//             if (t != NULL)
//                 t->next = NULL;
//             else
//                 return NULL;
//         }
//         return head;
//     }
// };

//Learn from discuss on 20170821
//Time:O(n)
//Space:O(1)
//Two Pointer !
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL)
            return NULL;
        ListNode* fir = head;
        ListNode* sec = head;
        for (int i = 0; i < n+1; ++i)//How to set the gap of the two pointers also needs consideration
        {
            if(sec==NULL)
                return head->next;
            sec=sec->next;
        }
        while(sec!=NULL) {
            sec=sec->next;
            fir=fir->next;
        }
        ListNode* temp=fir->next;
        fir->next=fir->next->next;
        delete temp;
        temp=NULL;
        return head;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(0);
    ListNode* l1 = h1;
    for (int i = 1; i < 5; ++i)
    {
        ListNode* n1 = new ListNode(i);
        h1->next = n1;
        h1 = n1;
    }
    l1 = s.removeNthFromEnd(l1, 5);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
