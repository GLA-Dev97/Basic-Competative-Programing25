package javacode;
import java.util.Scanner;
public class last{
    public static void main(String args[]){
        Scanner rdx=new Scanner(System.in);
        System.out.print("Enter a number");
        int num=rdx.nextInt();
        if(num%10==4){
            System.out.println("Last digit is 4");
        }
        else{
            System.out.println("Last digit is not 4");
        }
        rdx.close();
    }
}
