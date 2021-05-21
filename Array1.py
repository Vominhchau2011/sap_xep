import java.util.Scanner;
import java.util.Arrays;

public class Array_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("NHap so phan tu cua mang: "); 
        int n = sc.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a,1,n);
        for (int i = 0;i < n;i++) {
            System.out.print(a[i] + " ");
        }
    }
}
