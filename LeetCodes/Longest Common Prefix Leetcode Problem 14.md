# Initial thoughts 

obvioulsy could use the `.contains()` somewhere 
have to loop over every string ? could be bad 

IDEA: could build a new string by checking if all 

REALIZATION: its longest common prefix! so this kinda becasue easier i think 
	- just build a string strating with the fisrt char in the first string and then check if the other two have that char and keep going until one doesnt have that and return the string

GOT to a solution i think 

---
# Solution 

INTAL solution:
```java
 public static String longestCommonPrefix(String[] s){
        String ans = "";
        if(s[0].length() == 0)
            return "";
            for (int i = 0; i < s[0].length()-1; i++) {
                ans += s[0].charAt(i); // add the first strings char
                for(int j = 1; j < s.length; j++){ // start at the next string in the array and see if all of them have this first letter
                    if(s[j].length() == 0){return "";} // edge case
                    if(s[j].charAt(i)==(ans.charAt(i))){ // check to see if all the strings in the array have that same letter as the first one
                    continue; 
                    }else{
                        return ans.substring(0, i); // because it prematurally adds the intail strings next char so u have to cut it short
                    }
                }
            }
        return ans;
}
```

==Feel like this first for loop might be unessarcy==


---

# Logic behind solution 

- Pretty much add the fisrt char of the fisrt string in the array to the anserw string then check if all the other strings in the array have that char and if they do then keep going. if they don't then you should return the substring up until that point (which is gonna be one less char than the stirng has becasue i added the next char first then compared)   

---
# How I would improve this 

- I feel like this has one too many for loops. I think i could cut down the outter loop somehow or maybe at least have like a best case. 
	- can't think of any better way
	- dont think theres any hashmap solution  (keys being the )

right now my solution is $O(m*n)$ where $m=$ the length of the first string and then $n =$ length of the matrix in the worst case.  


- also not sure if it handles the sinlge array entry => it does :)
- oh wow it didnt get accepted on the "A" test case fixed that

--- 


# What I learned 

so here is a optimal solution:
```java
class Solution { 
	public String longestCommonPrefix(String[] v) { 
		StringBuilder ans = new StringBuilder(); 
		Arrays.sort(v); String first = v[0]; 
		String last = v[v.length-1]; 
		for (int i=0; i<Math.min(first.length(), last.length()); i++){                               if(first.charAt(i) != last.charAt(i)) {
				 return ans.toString(); 
			} 
			ans.append(first.charAt(i)); 
		} 
		return ans.toString(); 
	} 
}
```

- pretty clever idea noticing that you could sort the array fisrt by length of the sting and then you will instatly know some information, 
- A `StringBuilder` is a good way to extract a substring withouth losing some performance! (the `.substring()` method is what killed my time i think)
- trying to narrow down the search space 
	- a note on this tho is that i think the big O time complexitys might be the same-ish (the `Arrays.sort()` depends on O(n) in worst case , and then the for loop depends on the length of the shortest string in the array in O(m). 

- main point is try to see if you know anything special about how you could order your data before you get it. 

---

# Questions 




