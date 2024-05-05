# Initial thoughts 


I have some code in the useful code section that will do this perfectly !

---
# Solution 

```java
   public int reverse(int number) {
        int reverse = 0;
        int remainder = 0;
        while(number!=0) {
            remainder = number%10; // this is to extract the last digit of the number
            reverse = reverse*10+remainder; // this is "shift up" the last digit of the number and add the next digit beside it
            number = number/10; //this is to update the while loop so that 1. it will eventally stop (becasue of int division) and 2. that it stops after the number is down to its last digit (i.e. number =14, loop runs twice becauase... -> 4/10=0)
        }
        return reverse;
    }
```

---

# Logic behind solution 

It kinda runs on this werid kind of algorythm that makes sense but would defintely take me a while to come up with on my own for sure (I cant remeber the exact source but I saw this in a youtube video somewhere for sure)

---
# How I would improve this 


forget about this part pf the probelm "If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`."

so think that maybe I should have a if statment in the for loop to see if at any point its gonna be over it 
^ 
new idea maybe I should look for some pattern that will tell me if the number is gonna be over the 32 bit limit before I reverse it to give me some speed


Test case broke at "1 534 236 469" which reversed is 9 000 000 000 so I am confused on if they both have 9 digits why is the revered one outside of 32 bit integer range
- thats because this is the 32 bit integer limit =="2,147,483,647"== so thats why the one that starsts with 1 is smaller and the one with 9 is bigger 


So to know if its above the limit obviously if the number is 10 digits long and has a 3 as last digit its too big so thats a easy way to check but obvioulsly doesnt chechk it all 

need to have a way to check the length of it 

this has turned out to be harder than I thought , I'm not sure how to do this 



what i've finally come to is that even tho it seems so ineffeiecent to run this code to check if the number reversed is out of the 32 bit Integer limit everytime (because this can only happen if the number is 9 digits big) I think i'm gonna try it and see if it works
	- it didnt work :((


Looked up how to check if a interger is out of the limit and saw some stuff about longs and then remembered this [[Cosc 111 Final]]
![[Pasted image 20230908145825.png|500]]
now i think i can defeintley figure it out with this info 


think all i need to do is to make the `reverse` varrible a long and then everything should work 


--- 
# What I learned 


- weirdly enough the abosulte  value operator doent work for this number at the edge of the 32 bit integers 
```java
sysout(Math.abs(-2147483648)) // => -2147483648
```
- you can't really do arithmetic with numbers that are close to the 32 bit integer limit 
```java
if( 900 000 000*10>INT_MAX){
	sysout("hi");
} // => doesnt run 
```

- Learned that these are methods you can use 
```java
Integer.MAX_VALUE;
Integer.MIN_VALUE
```

- Thinking about the primitives is helpful , knowing that there is something bigger than a `int` was the key insight here. 

==How other people did it==
- used the same algorithm i did from what i can tell(looking at other peoples solution i realized i can speed my code up a bit) 

---
# Questions 

- I'd like to know more about space complexity or memory because I'm confused on why my solutions are always so bad in that 

