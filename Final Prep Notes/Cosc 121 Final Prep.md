[[Cosc 121 Midterm 1]]
[[Cosc 121 Midterm 2]]




---
# [[Recursion]]
- You need to remember that once the method returns then you need to remeber that the rest of the code will run 
- Very good and tricky example
```java
    public static void foo(int n){
        if(n>0){
            System.out.println("X"+n+" ");
            foo(--n-1);
            System.out.println("Y"+ n + " ");
        }
    }
// Prints X4 X2 Y1 Y3
```
- gotta remeber that in non tail recurisive that the method call then returns to where it was on the last call and excutes all the code there until it sees a return statment than leaves. 

---
# Comparator<>

- Good for comparing different atributes of a class , weight, year stuff 
- Can have mulitple class's that implemnt coparable (i.e. RobotcomapratorWeight RobotcomparatorYear , RobotComparatorHieght......)

```java
public int compare(Object o, Object k){
// comparing critria 
return o.critria-k.critria
}
```


---
# [[Interface]]
- remember that you don't have to implement the abstract methods into clases that are abstract or 
- ==an abstract class or interface that has abstract methods must be implement by its concrete children.==


---
# [[Polymorphism]]

- In a situation like this the reference type is the type that is passed to the method!
```java
Human h1 = new Student();


public void (Student s ){
sysout("yoooo");
}
public void (Human h1 ){
sysout("whatttt's uppppp");
}

// what's printed is the "whattttt's upppp"
```

---
# [[Abstract Classes]] vs [[Interface]]

==NOTE:== This is how you create a abstract class properly
```java
public abstract class Cow{
public abstract void();
}
```

- interfaces use a implements framework where as abstract classes can only extend one other abstract class. 
![[Pasted image 20240414210550.png]]


---
[[L ]]














---
# In class


Scanner in 

while(in.hasNextLine())



if ( in.next() .equals(word)) 
	then increase count++


in.hasNextInt() count++ 


---

# SL session 

- Arraylist uses random acceses 
- Linkedlist using sequential access 
- Queues first in first out 
- Stack last in first out 


Text IO 
1. Scanner and Printwritter 
2. BufferedReader and BufferedWritter




# Sorting Algo's
ALL $O(n^2)$
- [[Bubble Sort]] = bubble up the bigger number out of the two pairs  
- [[Selection Sort]] = selecting the next smallest element and add it into the sorted pile  
	- guess its bad on storage too 
- [[Insertion Sort]]  = starting at the beging of the array place it into the proper place in the sorted pile
	- also bad on storage

ALL $O(n\log n)$
- [[Merge Sort]] 
- [[Quick sort]]




