package javacode;
import java.util.Scanner;

public class Average {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 5 numbers:");
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();
        int E = sc.nextInt();
        float avg =  (A + B + C + D + E)/5;
        System.out.println("The Sum of these 5 number is "+ avg);
        sc.close();
    }
}
