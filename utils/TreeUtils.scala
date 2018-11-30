package utils

import scala.collection.mutable._

class TreeNode(var _value: Int) {
  var value: Int = _value
  var left: TreeNode = null
  var right: TreeNode = null
}


object TreeUtils {

  var queue = Queue[String]()


  def CreateTree(list: String): TreeNode = {
    val arrayList = list.split("\\s")
    for (i <- 0 until (arrayList.length))
      queue += arrayList(i)
    CreateTreeReally()
  }

  def CreateTreeReally(): TreeNode = {
    val value = queue.dequeue()

    if (value != "null") {
      var node = new TreeNode(value.toInt)
      node.left = CreateTreeReally()
      node.right = CreateTreeReally()
      return node
    } else {
      return null
    }
  }



  def PrintTree(root: TreeNode): Unit = {
    if (root == null)
      return
    println(root.value)
    PrintTree(root.left)
    PrintTree(root.right)
  }

}

object Test {

  def main(args: Array[String]): Unit = {
    val T = TreeUtils.CreateTree("1 null 3 null null")
    TreeUtils.PrintTree(T)
  }
}
