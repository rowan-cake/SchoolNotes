
# ==NAME = "Roman to Integer"== 

---
# Initial thoughts 

Switch statement for all the cases and have a sum at the top. 
	- few edge cases for example the number 4 and  9 have this werid rule about them 
	- substing comes to mind or the .contains("CM")
	- 

- Is there a unique way to make the number ? hashMap question? 
- had a for loop and a switch statment now just need to figure out how to get edge cases.
	- saw there was only six edge cases and thought that the if staments dont add any extra time to the solution BUt felt there was a better way still. 
	- if the number is always a 4 or a 9 times 1 , 10 or 100, then i fell like there has got to be a way to factor this out 

IDEA:
- since my bottom loop is adding it how it should add them i.e. at each postion it adds that postion to the sum. If i keep track of how many times there are special chars and then keep a seprate number to keep track of that and then subratct that away at the end I might be good 
Example test:
"IVI" mine bottom loop says this is equal to 7 (which is wrong)
but if i go and check `if(s.contains(IV)` and then know that my loop will count that wrong by 1 then i can substract 1 to the total.
"IXI" => 1+10+1 = 12
but it really should be => 9+1 = 10 so therefore -2 `if(s.contains(IX)` and now i countine on.... 


NOW i realize i have to count all occurances of the edge cases in the string and how should i do this????
	- well now after trying a few test cases i realize that this might not be possible with roman numerals.





---
# Solution 

first solution:
```java
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
```



---

# Logic behind solution 

1. go through the string and check if there are occurances of one of the 6 edge cases. if true then substrac off the approite amount from the integer counter. 
2. go through eveyr char on the strigng and add that chars value to a number
3. retrurn the number


-  feels like a pretty brute force solution and pretty ugly wouldnt be surprised if there was a way to get a better solution. something with the moidulus 4 and 9 seems possilbe.  


---
# How I would improve this 

Not sure yet 


--- 

# Questions 

NOthing yet 


