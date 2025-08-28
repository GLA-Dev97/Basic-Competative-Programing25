package javacode;
import java.util.Scanner;

public class LastDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the any number :");
        int n = sc.nextInt();
        if(n%10==4){
            System.out.println("Last digit is 4");

        }
        else{
            System.out.println("Last digit is not 4");
        }
        sc.close();
        
    }
}
