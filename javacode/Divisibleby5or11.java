package javacode;

import java.util.Scanner;

public class Divisibleby5or11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Number: ");
        int n = sc.nextInt();
        if((n%5==0)&&(n%11==0)){
            System.out.println("Number is divisible by 5 or 11");
        }
        else{
            System.out.println("Number is not divisible by 5 or 11");
        }
        sc.close();

    }
    
}
