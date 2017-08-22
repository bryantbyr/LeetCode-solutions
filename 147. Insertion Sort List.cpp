//147. Insertion Sort List.cpp
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

//Created by bryantbyr on 20170822
//Time:O(n^2)
//Space:O(1)
//Linked List (insert)
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* t = head;//to loop and compare
        ListNode* s = head;//临时变量,记录节点h的下一个节点
        ListNode* r = head;//记录链表实时的头结点
        ListNode* preH = NULL;//插入节点,修改前一部分
        ListNode* preT = NULL;//修改尾部
        while (head != NULL) {//loop for every node
            s = head->next;
            t = r;
            while (t != head) {//For some node, find the position to insert
                if (t->val > head->val) {
                    head->next = t;
                    preT->next = s;
                    if (t == r) //在链表头部插入
                        r = head;
                    else //在链表非头部位置插入
                        preH->next = head;
                    break;
                }
                else {
                    preH = t;
                    t = t->next;
                }
            }
            preT=head;
            while(preT->next!=s)
                preT=preT->next;
            head = s;
        }
        return r;
    }
};

int main()
{
    Solution s;
    ListNode* h1 = new ListNode(4);
    ListNode* l1 = h1;
    ListNode* n1 = new ListNode(19);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(14);
    h1->next = n1;
    h1 = n1;
    n1 = new ListNode(5);
    h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(-3);
    // h1->next = n1;
    // h1 = n1;
    // n1 = new ListNode(1);
    // h1->next = n1;
    l1 = s.insertionSortList(l1);
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
