package SchoolNotes.Code;

import java.util.Arrays;

public class UsefullCode {

    // Reversing a number in java:
    public static int reverse(int number) {
        int reverse = 0;
        int remainder = 0;
        while(number!=0) {
            remainder = number%10; // this is to extract the last digit of the number
            reverse = reverse*10+remainder; // this is "shift up" the last digit of the number and add the next digit beside it
            number = number/10; //this is to update the while loop so that 1. it will eventally stop (becasue of int division) and 2. that it stops after the number is down to its last digit (i.e. number =14, loop runs twice becauase... -> 4/10=0)
        }
        return reverse;
    }
    // Sorting a Array and creating a new array not modify the original:
    public static int[][] sortRows(int[][] m){
        int [][] copy = m;
        for (int i = 0; i < copy.length; i++) {
            Arrays.sort(copy);
            
        }
        return copy;
    }
    // Shuffling the Array rows randomly: 
    public static void shuffle(int[][] m) {
	    for(int i = 0; i < m.length; i++) {
		    int random_row = (int) (Math.random() * m.length);
		    int [] temp = m[i]; // to store the values of the swapped row
		    m[i] = m[random_row]; // swap row m[0] with m[2] for example and all the m[o] data is lost but in kept in "temp[]"
		    m[random_row] = temp; // now the m[2] gets swaped with m[0] or "temp[]" because tahts where the values are stotred
	    }
    }
    // Checking if each array is strictly equal (rectangular arrays):
    public static boolean equals(int[][] m1, int[][] m2) {
        if (m1.length != m2.length || m1[0].length != m2[0].length) { // check size of array
            return false;
        }
        for (int i = 0; i < m2.length; i++) {
            for (int j = 0; j < m2[i].length; j++) {
                if (m1[i][j] != m2[i][j]) {
                 return false;
                }
            }
        }
        return true;
    }
        // Reverses a string in java:
        public static String reverse(String s) {
            String reverse = "";
            for (int i = s.length()-1; i >= 0 ; i--) {
                reverse = reverse + s.charAt(i);
            }
            return reverse;
        }
        // Adding two square [[Matrix]]'s in java:
        public static int[][] addMatrix(int[][] a, int[][] b) {
            while(a.length != b.length || a[0].length != b[0].length) { // check size of the matrix
                System.out.println("Matrix's are not same size, try again");
            }
            int[][] sum_a_b = new int[a.length][a[0].length]; // new matrix with size of the orginal ones
            for (int i = 0; i < sum_a_b.length; i++) { //nested for loop because of the 2 dimenosnal nature of the matrix
                for (int j = 0; j < sum_a_b.length; j++) {
                    sum_a_b[i][j] = a[i][j]+b[i][j]; // every element in sum_a_b should be a + b for that respective row and column, and since everything is the same size this works good
                }
            }
            return sum_a_b;
        }
        // Sum of a column of a square [[Matrix]] in java:
        public static int sumCol(int[][] m, int colIdx) {
            int col_sum = 0; // inztailize the varrible
            for (int i = 0; i < m.length; i++) { // for whatever colindx givien go and take each
                col_sum += m[i][colIdx];
            }
            return col_sum;
        }
        // Number is palindrome in java:
        public boolean isPalindrome(int x) {
            int reverse = 0;
            int remainder = 0;
            int y = x;
            while(y!=0) {
                remainder = Math.abs(y%10); // this is to extract the last digit of the number
                reverse = reverse*10+remainder; // this is "shift up" the last digit of the number and add the next digit beside it
                y = y/10; //this is to update the while loop so that 1. it will eventally stop (becasue of int division) and 2. that it stops after the number is down to its last digit (i.e. number =14, loop runs twice becauase... -> 4/10=0)
            }
            if(reverse==x){
                return true;
            }else
                return false;
        }
        // How to print a 2d array with one line of code:
        public void print2Darray(Object[][] arr){
            for(Object[] r:arr){
                System.out.println(Arrays.toString(r));
            }
        }
        // How to get the average of a [[Matrix]] in java:
        public static double findAverageOfmatrix(int[][] x) {
            double sum = 0;
            double size = 0; // size means number of elements in the matrix.
            for (int i = 0; i < x.length; i++) {
                for (int j = 0; j < x[i].length; j++) {
                    sum += x[i][j];
                    size++;
                }
            }
            return sum / size;
        }
       // Factorial in java using recursion:
       public static int factorial(int n ){
		    if(n>0){
		    return n*factorial(n-1);
		    }else{
		    return 1;
		    }
        }
       // Palindrome in recursion:
       public static boolean isPal(String s ){
            if(s.length()<=1)//base case 
                return true;
            else if(s.charAt(0)!=s.charAt(s.length()-1))
                return false;
            else
                return isPal(s.substring(1,s.length()-1));
        }
       // 

}
