package LeetCodes;

public class RomanToInteger{
 public static void main(String[] args) {
    System.out.println(romanToInt("MCMXCIV"));

 }  
    public static int romanToInt(String s) {
        int romNum = 0; // sum tracker
        

        // the edge cases to make sure i adjust for my bottom counter  
        if(s.contains("IV")){
            romNum+=-2;        
        }
         if(s.contains("IX")){
            romNum+=-2;        
        } if(s.contains("XL")){
            romNum+=-20;        
        } if(s.contains("XC")){
            romNum+=-20;        
        } if(s.contains("CD")){
            romNum+=-200;        
        } if(s.contains("CM")){
            romNum+=-200;        
        }

        for (int i = 0; i < s.length(); i++) { // go through the string and get every char and then add that value to "romNum". 
            switch(s.charAt(i)){
                case 73: romNum+=1; break;
                case 86: romNum+=5;break;
                case 88: romNum+=10;break;
                case 76: romNum+=50;break;          
                case 67: romNum+=100;break;          
                case 68: romNum+=500;break;          
                case 77: romNum+=1000;break;          
            }
        }

        return romNum;
    }
}