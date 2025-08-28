package javacode;
import java.util.Scanner;

public class Angles {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Angle of Triangle: ");
        int Angle = sc.nextInt();
        if(Angle == 90 ){
            System.out.println("Right Angled Triangle. ");
        }
        else if( Angle<=90){
            System.out.println("Acute Angled Tringle");
        }
        else{
            System.out.println("Obtuse Angled Triangle");
        }
        sc.close();
        
    }
    
}
