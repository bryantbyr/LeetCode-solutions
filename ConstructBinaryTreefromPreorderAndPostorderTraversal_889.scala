
import utils.{TreeNode, TreeUtils}
import utils.TreeUtils._

object ConstructBinaryTreefromPreorderAndPostorderTraversal_889 {
  def constructFromPrePost(pre: Array[Int], post: Array[Int]): utils.TreeNode = {
    val len = pre.length
    helper(pre,post,0,len-1,0,len-1)
  }

  def helper(pre: Array[Int], post: Array[Int],a:Int,b:Int,c:Int,d:Int): utils.TreeNode = {
    if(a==b)
      return null
    val root = new TreeNode(pre(a))
    root.left = helper(pre,post,a+1,)
    root.right = helper(pre,post,)


  }

  def main(args: Array[String]): Unit = {
    val T = constructFromPrePost(Array(1,2,4,5,3,6,7),Array(4,5,2,6,7,3,1))
    val treeUtils = new TreeUtils("")
    treeUtils.PrintTree(T)
  }
}
