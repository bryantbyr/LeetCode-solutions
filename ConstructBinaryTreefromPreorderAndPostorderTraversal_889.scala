
import utils.TreeUtils
import utils.TreeNode

// Created by bryantbyr on 20181122
// Time:O(N^2)
// Space:O(1)
// Tree + Recursion
object ConstructBinaryTreefromPreorderAndPostorderTraversal_889 {
  def constructFromPrePost(pre: Array[Int], post: Array[Int]): TreeNode = {
    val len = pre.length
    helper(pre, post, 0, len - 1, 0, len - 1)
  }

  def helper(pre: Array[Int], post: Array[Int], a: Int, b: Int, c: Int, d: Int): TreeNode = {
    if (a > b || c > d)
      return null

    val root = new TreeNode(pre(a))
    if (a != b) {
      val partition = post.indexOf(pre(a + 1))
      root.left = helper(pre, post, a + 1, a + partition - c + 1, c, partition)
      root.right = helper(pre, post, a + partition - c + 2, b, partition + 1, d - 1)
    }

    return root
  }

  def main(args: Array[String]): Unit = {
    val T = constructFromPrePost(Array(1, 2, 4, 5, 3, 6, 7), Array(4, 5, 2, 6, 7, 3, 1))
    val treeUtils = new TreeUtils("")
    treeUtils.PrintTree(T)
  }
}
