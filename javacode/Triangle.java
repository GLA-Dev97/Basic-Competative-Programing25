package javacode;
import java.util.Scanner;

public class Triangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the angles of Triangle: ");
        int Angle_A= sc.nextInt();
        int Angle_B = sc.nextInt();
        int Angle_C = sc.nextInt();
        int Sum = Angle_A + Angle_B + Angle_C;
        if(Sum == 180){
            System.out.println("Valid Triangle");
        }
        else{
            System.out.println("Invalid Triangle");
            }
            sc.close();

    }
    
}
