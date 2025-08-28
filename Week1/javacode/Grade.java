package javacode;

import java.util.Scanner;

public class Grade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the percentage :");
        float per = sc.nextFloat();
        if(per<=35){
            System.out.println("Grade D");
        }
        else if(per<=55){
            System.out.println("Grade C");
        }
    
    else if(per<=65){
        System.out.println("Grade B");
    }
    else if(per<=85){
        System.out.println("Grade A");
    }
    else{
        System.out.println("Grade O ");
    }
    sc.close();
}
}