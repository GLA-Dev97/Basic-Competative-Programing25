package javacode;

import java.util.Scanner;

public class MaximumOf2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first Number");
        int A = sc.nextInt();
        System.out.println("Enter the second number");
        int B = sc.nextInt();
        if(A>B){
            System.out.println("A is maximum " + A);
        }  
        else{
            System.out.println("B is maximum " + B);
        }

    sc.close();
    }
}
