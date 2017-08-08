//107--Binary Tree Level Order Traversal II.cpp

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//20170530
//BFS&&Creat_BinaryTree
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> r;
        r.clear();
        if(root==NULL)
            return r;
        queue<TreeNode*> s;
        s.push(root);
        s.push(NULL);
        vector<int> t;
        while(!s.empty()){
            TreeNode* p=s.front();
            s.pop();
            if(p){
                t.push_back(p->val);
                if(p->left)
                    s.push(p->left);
                if(p->right)
                    s.push(p->right);
            }
            else{
            	if(!t.empty()){
	                r.push_back(t);
	                t.clear();
	                s.push(NULL);
				}
            }
        }
        reverse(r.begin(),r.end());
        return r;
    }
};

TreeNode* creatTree()
{
    TreeNode* Q[100];
    TreeNode* root;
    int front=0,rear=0;
    int data=0;
    cin>>data;
    while(data!=-1){
        if(data!=-2)
            Q[rear]=new TreeNode(data);
        else
            Q[rear]=NULL;

        if(rear==0)
            root=Q[0];
        else{
            if(rear%2==1){
                Q[front]->left=Q[rear];
            }
            else{
                Q[front]->right=Q[rear];
                front++;
            }
        }
        rear++;
        cin>>data;
    }

    return root;
}

int main()
{
    TreeNode* t;
    t=creatTree();

    Solution s;
    vector<vector<int>> r;
    r=s.levelOrderBottom(t);
    for(int i=0;i<r.size();i++){
        for(int j=0;j<r[i].size();j++)
            cout<<r[i][j]<<"  ";
        cout<<endl;
    }
    return 0;
}
