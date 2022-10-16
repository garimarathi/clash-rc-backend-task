import java.util.*;

class mergearray{
 public static void main(String[] args) {
         Scanner sc  = new Scanner(System.in) ; 
         int n = sc.nextInt();
         int m = sc.nextInt()  ;
         int[] nums1 = new int[n];
         int[] nums2 = new int[m] ; 
         for(int i=0;i<n;i++){
            nums1[i] = sc.nextInt();
        }
         for(int i=0;i<m;i++){
           nums2[i] = sc.nextInt();
        }

        merge(nums1 , n , nums2 , m) ; 

    }
 public static void merge(int[] nums1, int m, int[] nums2, int n) {
    ArrayList<Integer> list = new ArrayList<>();
    for(int i=0;i<m;i++){
        list.add(nums1[i]);
    }
     for(int i=0;i<n;i++){
        list.add(nums2[i]);
    }
    int []ans = new int[list.size()] ;
    for(int i=0;i<list.size();i++){
        ans[i] = list.get(i) ; 
    }
    Arrays.sort(ans) ;
    System.out.print("[");
    for(int i=0;i<ans.length;i++){
        System.out.print(","+ans[i]);
    }
    System.out.print("]") ; 
    Arrays.toString(ans);
}
}