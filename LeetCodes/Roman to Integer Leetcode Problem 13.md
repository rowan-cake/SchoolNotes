
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


My starting intution of it being a [[Hash Map]] was right and I shouldve pursued this idea a bit futher. 
Using the character as the key and the number as the value

A post from the website "The key intuition lies in the fact that in Roman numerals, when a smaller value appears before a larger value, it represents subtraction, while when a smaller value appears after or equal to a larger value, it represents addition" which makes a ton of sense. 

With knowing that main peice of info then you can reason that the for loop will pretty much do the same thing as my solution with a condtion that if the char after the one you are on is bigger  then you should substract it. 

```java

class Solution { 
	public int romanToInt(String s) { 
	Map<Character, Integer> m = new HashMap<>();
		m.put('I', 1); 
		m.put('V', 5); 
		m.put('X', 10); 
		m.put('L', 50); 
		m.put('C', 100); 
		m.put('D', 500); 
		m.put('M', 1000); 
		int ans = 0; 
		for (int i = 0; i < s.length(); i++) { 
			if (i < s.length() - 1 && m.get(s.charAt(i)) < m.get(s.charAt(i + 1))) { 
				ans -= m.get(s.charAt(i)); 
			} else { 
				ans += m.get(s.charAt(i)); 
			} 
		} 
		return ans; 
	} 
}
```



--- 

# Questions 


Little confused on how he can just substrtact the chars value from if it's one of those edge cases

IV => 4 

so edge case hit therefore
we subrtact the value of "I" => 1
then on second pass we hit the "V"=>5
so the ans = 4 and everything works out nice! 

so it makes sense 




