// 863. All Nodes Distance K in Binary Tree


import utils.{TreeNode, TreeUtils}
import scala.collection.mutable.Map

// object AllNodesDistanceKinBinaryTree_863 {

//   var map:Map[Int,List[Int]] = Map()

//   def connect(root: TreeNode): Unit ={
//     if(root == null)
//       return
//     if(root.left != null){
//       map(root.value) = map.getOrElse(root.value, List[Int]()) ++ List(root.left.value)
//       map(root.left.value) = map.getOrElse(root.left.value, List[Int]()) ++ List(root.value)
//     }
//     if(root.right != null){
//       map(root.value) = map.getOrElse(root.value, List[Int]()) ++ List(root.right.value)
//       map(root.right.value) = map.getOrElse(root.right.value, List[Int]()) ++ List(root.value)
//     }
//     connect(root.left)
//     connect(root.right)
//   }

//   def distanceK(root: TreeNode, target: TreeNode, K: Int): List[Int] = {
//     connect(root)

//     var res: List[Int] = List[Int](target.value)
//     var seen: Set[Int] = res.toSet
//     for(i <- 0 until(K)){
//       var temp: List[Int] = List()
//       for(x <- res){
//         for(y <- map.getOrElse(x,List())){
//           if(!seen.contains(y))
//             temp :+= y
//         }
//       }
//       res = temp
//       seen |= res.toSet
//     }
//     return res
//   }

//   def main(args: Array[String]): Unit = {
//     val T = TreeUtils.CreateTree("1 null null")
//     println(distanceK(T, new TreeNode(1), 3))
//   }
// }

// Learn from discuss on 20181129
// Time:O(N)
// Space:O(N)
// fix the above bug (the global variable "map" is not reentrant!)
object AllNodesDistanceKinBinaryTree_863 {

  def distanceK(root: TreeNode, target: TreeNode, K: Int): List[Int] = {
    var map:Map[Int,List[Int]] = Map()

    def connect(root: TreeNode): Unit ={
      if(root == null)
        return
      if(root.left != null){
        map(root.value) = map.getOrElse(root.value, List[Int]()) ++ List(root.left.value)
        map(root.left.value) = map.getOrElse(root.left.value, List[Int]()) ++ List(root.value)
      }
      if(root.right != null){
        map(root.value) = map.getOrElse(root.value, List[Int]()) ++ List(root.right.value)
        map(root.right.value) = map.getOrElse(root.right.value, List[Int]()) ++ List(root.value)
      }
      connect(root.left)
      connect(root.right)
    }

    connect(root)

    var res: List[Int] = List[Int](target.value)
    var seen: Set[Int] = res.toSet
    for(i <- 0 until(K)){
      var temp: List[Int] = List()
      for(x <- res){
        for(y <- map.getOrElse(x,List())){
          if(!seen.contains(y))
            temp :+= y
        }
      }
      res = temp
      seen |= res.toSet
    }
    return res
  }

  def main(args: Array[String]): Unit = {
    val T = TreeUtils.CreateTree("1 null null")
    println(distanceK(T, new TreeNode(1), 3))
  }
}
