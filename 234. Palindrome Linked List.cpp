//234. Palindrome Linked List.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170820
//Time:O(n)
//Space:O(n)
//反转链表,然后与原来链表进行比较
class Solution {
public:
    ListNode* reverseLinkedList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode* cur = head->next;//待放到链表头部的节点
        ListNode* t = NULL;//临时变量
        ListNode* pre = head;//记录原头结点
        while (cur != NULL) {
            pre->next = cur->next;
            t = cur;
            cur = cur->next;
            t->next = head;
            head = t;
        }
        return head;
    }
    ListNode* copyLinkedList(ListNode* head) {
        if (head == NULL)
            return NULL;
        ListNode* nhead = new ListNode(head->val);
        ListNode* h = nhead;
        head = head->next;
        while (head != NULL) {
            ListNode* n = new ListNode(head->val);
            h->next = n;
            h = n;
            head = head->next;
        }
        return nhead;
    }
    bool isPalindrome(ListNode* head) {
        ListNode* thead = copyLinkedList(head);
        ListNode* rhead = reverseLinkedList(head);
        while (thead != NULL) {
            if (thead->val != rhead->val)
                return false;
            thead = thead->next;
            rhead = rhead->next;
        }
        return true;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(1);
    ListNode* l1 = h1;
    for (int i = 1; i < 3; ++i)
    {
        ListNode* n1 = new ListNode(i);
        h1->next = n1;
        h1 = n1;
    }
    ListNode* n1 = new ListNode(1);
    h1->next = n1;
    h1 = n1;
    // for (int i = 3; i > 0; --i)
    // {
    //     ListNode* n1 = new ListNode(i);
    //     h1->next = n1;
    //     h1 = n1;
    // }
    cout << s.isPalindrome(l1) << endl;
    // l1 = s.reverseLinkedList(l1);
    // while (l1 != NULL) {
    //     cout << l1->val << endl;
    //     l1 = l1->next;
    // }
}
