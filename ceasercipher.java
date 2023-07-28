import java.io.*;
import java.util.*;
public class SubstitutionCipher {
    static Scanner sc = new Scanner(System.in);
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        System.out.println("Enter the plain text");
        String pl=sc.nextLine();
        pl=pl.toUpperCase();
        System.out.println(pl);
        System.out.println("Enter the shift factor");
        int n=sc.nextInt();
        System.out.println("Cipher Text:");
        char a[]= pl.toCharArray();
        for(int i=0;i<a.length;i++){
            a[i]=(char)(n+(int)a[i]);
        }
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]);
        }
        String a = "abcdefghijklmnopqrstuvwxyz";
        String b = "zyxwvutsrqponmlkjihgfedcba";
        System.out.print("Enter any string: ");
        String str = br.readLine();
        String decrypt = "";
        char c;
        for(int i=0;i<str.length();i++){
            c = str.charAt(i);
            int j = a.indexOf(c);
            decrypt = decrypt+b.charAt(j);
        }
        System.out.println("The encrypted data is: " +decrypt);
    }
}