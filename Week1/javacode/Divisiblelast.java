package javacode;
import java.util.Scanner;

public class Divisiblelast {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Number: ");
        int n = sc.nextInt();
        if(n%3==0){
            System.out.println("Number is divisible by 3");
            if(n%10==4){
                System.out.println("the last digit is 4");
            }
            else{
                System.out.println("The last digit is not 4");
            }
        }
        else{
            System.out.println("Number is not divisible by 3");
        }
        sc.close();
    }
    
}
