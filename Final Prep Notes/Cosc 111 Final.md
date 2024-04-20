==48mins==

- No tracing code (but finding the answer at the end) questions
- Every topic all the way up to "final" 


# Covered in class 

## First half

- `printf` use case:
	- When you want to print the output in a specific format
	- Less concatenation 
	- Less code 
	- Can present with specific presession `System.out.printf(%.3f)`
	- Can align them with text `System.out.printf(%-14s)` , `System.out.printf(%14s)`
	- To print a '%' or a ' " ' `System.out.printf(%-14s%%)` , `System.out.printf(\"%d\"")`  

- local variable 
	- Variable defined in a method (code block)

- global variable
	- [[Attributes]] of a class 

- ^ operator (x or) 
	- whenever they are similar then output is false
	- whenever they are different then output is true

### short cut operator 
ex)
```java 
int x = 5;
if(x<1 && x++>5){
sysout("a");
}
sysout(x);
// Out put is 5

```
vs
```java 
int x = 5;
if(x<10 && x++>5){
sysout("a");
}
sysout(x);
// Out put is 6
```

- `in.nextLine();` vs `in.next();`
	- `in.next();` does not take spaces between intput i.e `abc def` "abc" will be taken 
	- `in.nextLine();` takes the whole line

- Specific case of `in.nextLine();` vs `in.nextInt();`
	- When reading a number before a string be very careful to "throw away the empty string" because the `nextLine()` will read a `enter` as a input. 

- Switch statements 
ex)
```java 
int x = 7;
String s = switch(x){
case 7 -> "Seven"
};
sysout(s)
// s = seven
```

- Conditional operator
	- always yields a single value
	- downside is its less flexible 
	- 
ex)
```java
int age = 10;
String s = age>=19?"ADult":"Minor";
sysout(S)
//minor
```

- Pass by value vs method changing things 
- [[Encapsulation]]
- [[Overriding.canvas|Overriding]] same name as the parent [[Method]]. 


## Questions

How to print a 2d array with one line of code:
```java
for(int[] r:arr){
Sysout(Arrays.toString(r));
}
```

Making a array of objects:
```java
Circle[] circle = new Cricle[4]; //space for 4 circles but value is null rn 
for(int i = 0; i>circle.lenght; i++){
circles[i] = new Circle(Math.random()*100);
}
// makes 4 circles 

```


---

### Java Aims
1. ==[[OOP]]== 
	- Java was designed from the start to be object-oriented. • Object-oriented programming (OOP) is a popular programming approach that is replacing traditional procedural programming techniques.

2. ==SIMPLE== 
	- Java is partially modeled on C++, but greatly simplified and improved. • It is like C++ but with more functionality and fewer negative aspects.

3. ==Multithread== 
	- programming is smoothly integrated in Java. • Multithreading is a program’s capability to perform several tasks simultaneously

---
### Primitive Datatypes

![[Pasted image 20230908145825.png|500]]
==NOTE:== what is important here is the size in memory.
8 bits
2 bytes
4 bytes
8 bytes
4 bytes
8 bytes
8 bytes
8 bytes
2 bytes
1 byte

==NOTE:== Strings are not primitives 

---
### Variable scope  

- Variables can only be used within their block of code 
-  BLOCKS of code 
ex) ==Correct== 
```java

for(int i = 1; i<2;i++){
int x = 15;
// This is the start of the block of code 

//Note: this is the end of the block of code 
}
System.out.println(x); //error because x is not seen by the rest of the code
```

---
### [[explicate casting]] vs [[implicit casting]](aka "Type widening")

Explicate example:
```java
int z = (int)1.2; // can pass the varrible the not same datatype with explicte casting
```
==NOTE:== remember that java variables can only store data of their same type 

Implicit example:
```java
double z = 1;
```
Java has this built in hierarchy that allows for a double variable to convert '1' $\to$ "1.0" because java variables can only store data of their same type.
![[Pasted image 20230915145615.png]]

---
### Scanner related things

Syntax for importing 
```java
import java.util.Scanner;
//Class statment 
Scanner in = new Scanner(System.in); // importing the scanner object called "in"
```

##### `in.nextInt()` before `in.nextLine()` logic error

- If you read in a int before a string you will have a logic error.
- The reason this happens is because the user inputs are "42" followed by "enter"
- The `in.nexInt()` will take the '42' value and the user clicks enter the `in.nextLine()` will take the "enter" as a its value and read a empty string. 
==Different explanation== 
- Specific case of `in.nextLine();` vs `in.nextInt();`
	- When reading a number before a string be very careful to "throw away the empty string" because the `nextLine()` will read a `enter` as a input. 

#####  `in.nextLine();` vs `in.next();`

- `in.next();` does not take spaces between intput i.e `abc def` "abc" will be taken 
- `in.nextLine();` takes the whole line

---
### Short cut operator 
ex) for &&
```java 
int x = 5;
if(x<1 && x++>5){
sysout("a");
}
sysout(x);
// Out put is 5

```
vs
```java 
int x = 5;
if(x<10 && x++>5){
sysout("a");
}
sysout(x);
// Out put is 6
```

ex) for ||
```java
int x = 5;

if(x<10 || x++>5){ //true || false

System.out.println('a');

}

System.out.println(x);

// Out put is a, 5
```
vs
```  java

x = 5;

if(x<1 || x++>1){ //false || true

System.out.println('a');

}

System.out.println(x);
// Out put is a, 6
```

---
### Built in methods 

==Must know more of these== 
1. Math class
2. String Class
3. Character Class
4. Array Sort method (`System.arrayCopy()`)

---
### [[if statements]] $\to$ [[switch statements]]

- To go between them basically you'd have a bunch of conditions(and a bunch of if statement) that you are checking in the if statement and to make it look better you go to switch.

Here's maybe a example 

```java
int x = 12;
if(x>=12||x==1){
Sysout
("Num is 12 or 1")
}
```
Maps too:
```java
int x = 12;
switch(x){
case 1 -> sysout
case 12-> sysout
}
```

---
### [[For loops]] $\to$ [[For Each loop]]

---
### [[For loops]] $\to$ [[While loops]]

---

### [[While loops]] $\to$ [[Do while loops]]

---
### [[Method overloading]]

Things to remember here are
- java will go for the closer mismatch away from the type if both of them are wrong
- ambiguous invocation = when there is a equal amount of "distance" between the methods 
ex)
```java
public static void main(String[] args) {
System.out.println(sum(3,5));
}
public static double sum(double x , int y) { // same name
System.out.println("a");
return x+y;
}
public static double sum(int x , double y) { // same name different signatures
System.out.println("b");
return x+y;
}
}
// output is error because 3 is a int but can be taken as a double, but 5 is also a int and can be taken as a double and so therefore the both methods get called at same time I think ?  
```

---
### [[arrays]]
---
### [[OOP]]

Static 
- An example is the `Math.pow()` method because you don't need a object to perform this [[Method]] on. 
- General purpose
- Use this in a method or variable header if you want it to apply to the whole class (i.e. a counter , or smth else)
- 

Instance 
- Something like a `Circle1.moveUp()` because you need a object. (I think )
- Can only apply to a [[Objects|Object]] of that [[Class]]


---

# Presentation

- if there is no counter in a loop its a sentinel controlled loop
- ex)![[Pasted image 20231211160932.png]]
- going through the "a++", and "++a".
- ex)![[Pasted image 20231211162328.png]]
- look at the second line as "`int b =a; `  followed by  ` a++;`"
- understanding the increment 

Q1
```java
import java.util.Scanner;

public class 1
public static void main(String[] args) {
Scanner in = new Scanner(System.in);
double initial_pay = 100;
double score = in.nextDouble();
if(score>90){
increase = initial_pay*0.03;
initial_pay += increase;
}
```

Q2
```java
import java.util.Scanner;

Scanner in = new Scanner(System.in);
do{
System.out.println("Enter a int , the input ends if it is a 0");
int number = in.nextInt();
}while(number!=0){
int sum = 0;
sum+=number;
System.out.println("Enter a int , the input ends if it is a 0");
number = in.nextInt();
}
```

Q3
```java
Class TV{




}

```

- this keyword
	- Current class

- super keyword
	- refers to the 

---
### Recourses

Total overview:
![](https://www.youtube.com/watch?v=eIrMbAQSU34)

Inheritance overveiw:
![](https://www.youtube.com/watch?v=Zs342ePFvRI)


 ---
 