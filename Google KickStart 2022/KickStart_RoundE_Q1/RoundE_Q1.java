import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T =  input.nextInt();
        
        for (int t = 0; t<=T ; t++){
            int ans = 0;
            int n = input.nextInt();
            if (n<=3){
                ans = 1;
            }
            if (n>=4){
                ans = (n/2)-1;
            }
            System.out.printf("Case #%d: %d" , t + 1, ans);
        }
    }
}
