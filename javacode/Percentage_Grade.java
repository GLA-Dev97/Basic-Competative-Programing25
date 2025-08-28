package javacode;
import java.util.Scanner;

public class Percentage_Grade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the percentage: ");
        float per = sc.nextFloat();
        if (per >= 90) {
            System.out.println("Grade: A");
        } else if (per >= 80) {
            System.out.println("Grade: B");
        }else if(per>=70){
            System.out.println("Grade: C");
        }
        else if(per>=60){
            System.out.println("Grade: D");
        }
        else{
            System.out.println("Grade: F");
        }
        sc.close();
    }
}
