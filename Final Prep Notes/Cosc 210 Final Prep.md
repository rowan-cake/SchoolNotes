# Things to remember

- A [[parameter]] is something being passed to the method:
```java
public int someMehtod(int number){
	ArrayList<int> beat = new ArrayList<>();
	if(beat.contain(number)){
		return 1;
	}
	return -1;
}
```
number is the parameter.

- A [[argument]] is the actual value being passed to the method i.e. `someMethod(56);` "56" is the value
- All [[Abstract Methods]] need to be implemented by the children 

---
# Basic's

Object need to be instantiated to exist (other wise it's just a refence not technically a obejct): 
```java
Cat mycat; // just a reference no object yet
mycat = new Cat(); // a class now 

```

---
# [[Specifications]]

- usually for the [[Method]]'s sometimes for [[Class]]'s
example:
```java
// REQUIRES
// EFFECTS
// MODIFIES
public int someMethod(int i){

}
```

1. REQUIRES
	- what does the method need to "work" and not break or give a logical error
2. EFFECTS
	- what does the method literally return i.e. the point of it and so on
3. MODIFIES
	- what the method modifies if the modies clause says "this" it means that it modifes the classs in somet way


---
# [[Unit Testing]]

- need the @Before part and the 
- @test part

- quick example:
```java
import static org.junit.Assert.*;
import org.junit.*;
import ca.ubc.cpsc210.taskmanager.model.Task;
public class TestProject {
    private Project prj;
    @Before
    public void setUp() {
        prj = new Project();
    }
    @Test
    public void testEmpty() {
        assertEquals(0, prj.hoursToComplete());
    }
    @Test
    public void testOneTask() {
        prj.add(new Task(4));
        assertEquals(4, prj.hoursToComplete());

    }
```



---
# [[UML DIAGRAMS]]



- [[Aggregation]] 
	- A bit confused on this but I think its when a class has a =="Class B can't exist without Class A"== relationship.  
	- Is represented with a closed paraleglram on the UML diagram or a bidirection relationship.
	- You put this at the base of the paraleglram at the class with all the fields of it.  (can have multiplies)
- [[Dependency]] 
	- Is when a class uses methods or global variables from another class (can only happen in package related ways maybe)
	- Is represented by a dotted line and a open triangle in UML notation 
	- An example of this would be when you have import some class and use a static method or varrible from that class (think `Math.Random();` or `Circle.PI()` or something of that nature) 
- [[Association]]
	- Is when a class has a [[Attributes|attribute]] (or list of [[Attributes]]) of the type of some class class
	- Is repersented with a straight arrow and a open triangle in UML notation. (can have multiplies) 
- [[Bi Directional]]
	- When two classes both have fields of each other 
	- Could be many to one or so on. 
	- Is reperesented with no arrow head. (can have multiplies)
- [[Inheritance]]
	- When you have a parent child relationship
	- Repersented by a striaght line and a closed arrow triangle.  
- [[Interface]]
	- Repersented by a dotted line and a closed triangle arrow. 



==NOTE:== For a multiple relationship of either the [[Aggregation]] or the [[Association]] the way you draw the [[UML DIAGRAMS]] is as follows:
	1. The class that has the fields points to the fields class's
	2. The number (multiplicity) of the how objects some class has is depicted at the tip of the arrow. 
ex)
```java
Class A {
public B b;
public B c;
}
Class B{

}
```
diagram: 
$A\to _{2}B$

==NOTE:== There is no "discernible difference between the [[Aggregation]] code and the [[Association]] code" it is more of a qualitive description. I.E the difference between =="Class A can't exist without Class B"== $\implies$ [[Aggregation]] and the inverse for [[Association]].  Just there to understand the topology of the code.




---
# [[Sequence Diagram]]

- They start from inside a method call 
- You draw it as if it was the debugger. ==Because its same pathway as the debugger would take==
- Remember a loop has a box around it in the sequence diagram 
- [[if statements]] in a sequence diagram: (probably won't be on test but in case)
![[Pasted image 20240422125545.png|400]]


==NOTE:== Think about what objects are in play in the method (including [[ArrayList]] or anything of that nature).
==Note:== When drawing this you always are making the name of the method calls on the top of the arrows.
ex)
![[Pasted image 20240422124624.png|400]]
==NOTE:== Any [[ArrayList]] or any default java classes are called and also written on the sequence diagram. 
==NOTE:== note that every method call comes from out of town and then called what the method name is called.  

---
# [[Hash Map]]
- main things are don't forget to overide the `equals` and the `hashcode` methods if you need to store a object as a value in the hashmap. 
- 


---
# [[Interface]]
- Declare common behaviour of objects that implement 

---
# [[Cohesion]] + [[Coupling]] 
- High Cohesion Low Coupling = GOOD
- Low Cohesion High Coupling = BAD


- Two main types of [[Coupling]]: 
	1. semantic $\implies$ similar printing format 
	2. moderate $\implies$ sharing some sort of class attribute that will mess up one class if you change it (happens at compile time)
- Best way to find the coupling is to see if there is any semantic coupling and then see if there is any moderate coupling (I know not helpful but there is no other way i can think of to find this )
example of improving coupling:
![[Pasted image 20240424115410.png]]


- [[Cohesion]] means that within a class it is only doing stuff related to the same class's purpose(a little abstract but it makes the point known)
- 

==MORE ON THIS LATER==


---
# [[Single Resbonsility Principle]]


---
# [[Liskov Substitution Principle]]  

- change super class specifications with the sub class specifications  ? 
Remember this and you should be good
	1. ==sub-method cannot accept a narrower range of inputs than the original method==.
	2. The post conditions of a sub-method cannot be weakened, meaning that the ==sub-method cannot have a broader range of effect than the original method==.
because then it violates LSP! 

---
# [[Refactoring]] 

- think math factoring.
- wanna have fully exhaustive tests when doing this so you know nothing will break. 
- this is usually done to improve the [[Single Resbonsility Principle]] (thereby increasing cohesion ) or to make the [[Coupling]] lower
- Involves yanking code (methods or code within methods) and putting them into somewhere new and more abstract (a new class or a new method)
 
---
# Design Patterns 


- Three main ones

1. [[Observer Pattern]]
	- A response to needing a system to be more cohesive.
	- Twitter example of (following and updating followers)
	- Four main classes
	- Remember where the methods go
1. [[Composite Pattern]]
	- 
2. [[Singleton pattern]] ([http://en.wikipedia.org/wiki/Singleton_pattern](http://en.wikipedia.org/wiki/Singleton_pattern)) ==DIDNT GET TO THIS ONE IN THE CLASS==




---

# [[Iterator]]
