import scala.collection.mutable.ListBuffer

// Definition for a binary tree node.
class TreeNode(var _value: Int) {
  var value: Int = _value
  var left: TreeNode = null
  var right: TreeNode = null
}

//Created by bryantbyr on 20181120
//Time:O(N)
//Space:O(N)
//Tree + Recursion
object Solution {

  def helper(root: TreeNode, list: ListBuffer[Int]): Unit = {
    if (root == null)
      return
    if (root.left == null && root.right == null) {
      list += root.value
    } else {
      helper(root.left, list)
      helper(root.right, list)
    }
  }

  def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {
    var list1 = ListBuffer.empty[Int]
    helper(root1, list1)
    var list2 = ListBuffer.empty[Int]
    helper(root2, list2)
    return list1 == list2
  }

  def main(args: Array[String]): Unit = {
    val T1 = new TreeNode(3)
    T1.left = new TreeNode(5)
    T1.right = new TreeNode(1)
    val T2 = new TreeNode(2)
    println(leafSimilar(T1, T2))
  }
}



