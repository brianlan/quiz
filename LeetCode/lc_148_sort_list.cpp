#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


// ListNode* sortList(ListNode* head) {
//     if (head == nullptr || head->next == nullptr) {
//         return head;
//     }
//     bool exchange;
//     do {
//         exchange = false;
//         ListNode *r = nullptr, *p = head, *q = head->next;
//         while (q != nullptr) {
//             if (p->val > q->val) { // exchange
//                 p->next = q->next;
//                 q->next = p;
                
//                 if (head == p) {
//                     head = q;
//                     r = q;
//                 } else {
//                     r->next = q;
//                 }
//                 r = q;
//                 q = p->next;
//                 exchange = true;
//             } else {
//                 if (r == nullptr) {
//                     r = head;
//                 } else {
//                     r = r->next;
//                 }
//                 p = p->next;
//                 q = q->next;
//             }
//         }
//     }
//     while (exchange);
    
//     return head;
// }

void splitList(ListNode* head, ListNode** left, ListNode** right) {
    ListNode* slowslow = nullptr;
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        fast = fast->next->next;
        slowslow = slow;
        slow = slow->next;
    }
    *right = slow;
    slowslow->next = nullptr;
    *left = head;
}

ListNode* mergeList(ListNode* left, ListNode* right) {
    if (left == nullptr) {
        return right;
    }
    if (right == nullptr) {
        return left;
    }
    if (left == nullptr && right == nullptr) {
        return nullptr;
    }
    ListNode *head = nullptr, *p = nullptr;
    if (head == nullptr) {
        if (left->val <= right->val) {
            head = left;
            p = left;
            left = left->next;
        } else {
            head = right;
            p = right;
            right = right->next;
        }
    }

    while (left != nullptr && right != nullptr) {
        if (left->val <= right->val) {
            p->next = left;
            left = left->next;
            p->next->next = right;
            p = p->next;
        } else {
            p->next = right;
            right = right->next;
            p->next->next = left;
            p = p->next;
        }
    }

    if (left != nullptr) {
        p->next = left;
    }
    
    if (right != nullptr) {
        p->next = right;
    }

    return head;
}

ListNode* sortList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    ListNode *left = nullptr, *right = nullptr;
    splitList(head, &left, &right);
    left = sortList(left);
    right = sortList(right);
    head = mergeList(left, right);
    return head;
}

int main () {
    ListNode* head = new ListNode(-1, new ListNode(5, new ListNode(3, new ListNode(4, new ListNode(0, nullptr)))));
    ListNode* sorted = sortList(head);
    int a = 100;
}