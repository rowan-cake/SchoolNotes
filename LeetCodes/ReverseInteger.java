package LeetCodes;

public class ReverseInteger {
    public static void main(String[] args) {
        System.out.println(reverse(-2147488));
        System.out.println(Math.abs(-2147483648));
        
    }
    public static int reverse(int number) {
        long reverse = 0; // the key insight
        int remainder = 0;
        while(number!=0) {
            remainder = number%10; // this is to extract the last digit of the number
            reverse = reverse*10+remainder; // this is "shift up" the last digit of the number and add the next digit beside it
            number = number/10; //this is to update the while loop so that 1. it will eventally stop (becasue of int division) and 2. that it stops after the number is down to its last digit (i.e. number =14, loop runs twice becauase... -> 4/10=0)
            
        }
        if(reverse>Integer.MAX_VALUE | reverse<Integer.MIN_VALUE) // check to see if its out of range here
                return 0;
        return ((int)reverse); // ayyyy
    }
}
