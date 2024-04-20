[[Stat 230 Midterm 2]]

# General things
- If its a dice question consider drawing a table to count out the ways its possible 
- If it sounds like a bayes theorem question it probably is one (prior, - _P_ (_A_,_P_ (_A_ | _B_)-posterir, ==TREE==)
	- drug testing , computer fixing , cancer research , etc...
	- ![[Pasted image 20240412123317.png]]
- Margin of error formula
$$
m = \frac{\left( z^*_{\frac{a}{2}}\cup t^*_{\frac{a}{2}} \right)*(\sigma \cup S)}{\sqrt{ n }}
$$
- Don't forget the word at least in a binominal distribution question 
- Note that with this theorem for the variance you need to only need to square the "outside x" in the $E(x)$ formula 
![[Pasted image 20240412130334.png]]
only square the outside x 
![[Pasted image 20240412130341.png]]
- Remember the Q3 and Q1 formulas
$$
Q_{k}=\frac{k*(n+1)}{4}
$$
 - Remember that if they give you $N(\mu,\sigma)$ thats what it is not variance in the other one. 
 - Remember that you can swap the order of the bounds on a multivariable question 
 - When doing conditail probability of multivariable functions you need to keep in mind that if its a contiouns distrubution and the question looks like:
$$
P\left( X\leq \frac{3}{4}|Y=\frac{1}{2} \right)
$$
then this means that the $P\left( X\leq \frac{3}{4} \right)$ is the only one you need to calculate namely the marginal PDF of X. I believe this is because you need to account for the fact that $P\left( Y=\frac{1}{2} \right)=0$ for countinus distributions. 

- Remember to look at the Z table or T table with prescion!!!! 
- Think in terms of $P\left( Z\geq \frac{{\bar{x}-\mu}}{\frac{\sigma}{\sqrt{ n }}} \right)$ when doing hypothesis, i.e the maps between Z value and P value is either the Z table or the T table 
- ==FACT== a nother test for independance of a mulivarrible PDF $f(x,y)$ is if the product of the marginal functions equal the og function namely:
$$
f(x,y)=f_{x}(x)*f_{y}(y)
$$
==note== another way to do this is to check if the same is true for the excepted values.


---
## Data

- Comes in either Categorical or Numeric values. 

| Categorical                                                                                              | Numeric   |
| -------------------------------------------------------------------------------------------------------- | --------- |
| Binary (yes or no)                                                                                       | Discrete  |
| Nominal (Blue, green, red)                                                                               | Continous |
| Ordinal (sorted by rank, low medium high) *different from Nominal because of how it is auto sorted kinda |           |
- Population vs Sample

| Population                                                             | Sample                                                           |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Collection of objects or measurements that  <br>we wish to understand. | A subset of the population                                       |
| Usally cannot say much about whole population                          | Can say some stuff about these (mean, standard deviation etc...) |

---

# Descriptive Stats + Terminology 

[[Mean]]
- Fairly self explanatory / intuitive
[[Median]]
- Kinda weird and idk when useful but ==IF== data is ordered than it is the middle of that dataset. 
[[IQR]]
- Is = [[Q3]]-[[Q1]]
$$
IQR = \frac{3}{4}(n+1)-\frac{1}{4}(n+1)
$$
- ==Not sure why its n+1 ??==

[[Variance]]
- The square of the [[Standard Deviation]]

[[Standard Deviation]]
- A measure of how far the data is spread from the mean, (Low [[Standard Deviation]] = very close to mean )
- Very sustiable to outliers in the data (Finding outliers)

==NOTE:== There are a few different ways to calculate these "metrics" and for different type of [[probability distribution]]'s they can be calculated differentially. 


---
## Probability theory 

**Axioms of Probability**
1. probabilities must be non-negative real numbers  
2. the probability of the entire sample space must be equal to 1  
3. If two events are disjoint (i.e. they cannot happen at the same  time), the probability that either of the events happens is the sum of the probabilities that each happens
	==NOTE:== This last one here is basically just the "or" $\cup$ rule which means you add them 

- Generally the probability of a discrete event is the "amount of space that event takes over the size of the total sample space"

- ==NOTE:== This is the $\cap$ rule which means you multiply the probability of each event.  ![[Pasted image 20240405201838.png]]
	ex)![[Pasted image 20240405202743.png]]


- MAIN TWO THINGS HERE ARE THE $\cap$ =="and rule"== of multiply probability's and the $\cup$ =="or rule"== of addition.  
- Or stated differntly the "and rule" is the [[fundamental principle of counting]], which states that if there are m ways to perform one action and n ways to perform another action, then there are m×n ways to perform both actions together if they are independent of each other."
---
## Permutations  + Combinations 

[[Gamma function]]

- This is the idea that if you have $n$ distinct objects and wish to arrange them in distinct ways then you can have exactly $n!$ different combinations  
	- Types of questions here are things like pick a ball out of a hat 4 times how many distinct ways can you have of balls with replacement (Colored Balls).   
	- How many different race finishes can we have with 8 horses...
	- etc ![[Lecture 2.pdf]]


- A good example of question I got wrong on the assigment. 
![[Pasted image 20240406105827.png]]
I got B wrong because it should have been $4!*6!$ and the reason for this is because of the "[[fundamental principle of counting]], which states that if there are m ways to perform one action and n ways to perform another action, then there are m×n ways to perform both actions together if they are independent of each other."

- This is important to remember "n chose r"![[Pasted image 20240406112733.png|500]]

- LAW OF LARGE NUMBERS ![[Pasted image 20240406113428.png]]
 THINGS TO REMEBER HERE
 - Really consider if what type of situation the problem is (is there replacement, does order matter, is there hidden outcomes, etc...)
 - don't forget the [[fundamental principle of counting]]

---

# Multiple Events (Sample Sets)

- [[Mutually Exclusive Events]] 
![[Pasted image 20240406114302.png|400]]

- =="OR RULE"== ![[Pasted image 20240406114946.png]]
ex) 
![[Pasted image 20240406115257.png|400]]
$$
\begin{equation}
P(Black\cup Jack)=P(Black)+P(Jack)-P(Black\cap Jack)
\end{equation}
$$
And then note that since these events arent [[Mutually Exclusive Events]] (i.e. there are Black Jacks 2 of them to be precise)

$$
\begin{equation}
P(Black\cup Jack)=\frac{26}{52}+\frac{4}{52}-\frac{2}{52} = \frac{28}{52}
\end{equation}
$$


- Conditional probability [[Bayes theorem]] ? ![[Pasted image 20240406121028.png|450]]
ex)
![[Pasted image 20240406121444.png]]


$$
P(odd|number>3)=\frac{P(odd\cap number>3)}{P(number>3)} \implies \left( \frac{\left( \frac{1}{2} \right)*\left( \frac{1}{2} \right)}{\frac{1}{2}} \right)=\frac{2}{3}
$$
==NOTE:== This is wrong!!!! I thought that you could calculate it this way but I made a oversight namely: 
$$
P(A\cap B)=P(A)*P(B)
$$
==ONLY IF THE EVENTS ARE INDEPENDANT==

==HERES THE EXAMPLE REWORKED!!!==
   However, this calculation is incorrect because events A (rolling an odd number) and B (rolling a number greater than 3) are not independent. The outcome of rolling the die is influenced by both conditions. For example, the outcome of rolling a 5 (an odd number greater than 3) satisfies both events A and B.
2. ==**Using direct counting**:==
   We directly identified the outcomes that satisfy both events A and B. The only outcome that satisfies both A and B is rolling a 5.
   Therefore, $( P(A \cap B) = \frac{1}{6} )$.
The key difference lies in the independence of events. In this scenario, events A and B are not independent because the occurrence of one event affects the probability of the other event occurring. Therefore, we cannot use the multiplication rule to calculate the joint probability. Instead, we directly identify the outcome that satisfies both events, leading to $$( P(A \cap B) = \frac{1}{6} )$$

- Multiple sample sets
![[Pasted image 20240407164833.png|450]]
this would get you all the circles areas without the intersection part

- Heres where I got confused last time [[Statistical Independence]]
![[Pasted image 20240407165148.png|400]]

| Independance                                                     | Mutually Exclusive                                                                                                  |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| The probability of B happening has no effect on probability of A | The events are intertwined with each other such that if event B happened then there is no way for event A to happen |
| Rolling two dice and getting a 5 on one and a 4 on the other     | Probability of picking a King and a Ace (if only picking one card this is then impossible)                          |
| ...                                                              | Online I saw $P(A\cap B)=0$ is the defintion of [[Mutually Exclusive Events]]                                       |
| If true then $P(A\cap B)=P(A)P(B)$                               | If true then $P(A\cap B)=P(A\|B)P(B)$                                                                               |


- The Complement of a Set is to be everything not in that set. 
- ![[Pasted image 20240407170623.png|400]]
- A bit tricky but i will study this more in depth soon. 


- ==Partition Theorem stuff==
- ...


==THINGS TO REMEMBER:==
- Is the compliment useful in this question 
- Memorize both the "and + or" rules
- Remember to think if the events are independent or not
- Never underestimate a good old fashion counting 
- Drawing out a Ven Diagram helps !!!!
- 
---
# Random Varribles (Odd distrubutions)

- Keep in mind that they can be just about anything on the real line
 ![[Pasted image 20240407172301.png]]


- [[probability mass function]] = discrete 
- [[Cumulative distribution function]] = discrete 

- Note that with this theorem for the variance you need to only need to square the "outside x" in the $E(x)$ formula 
![[Pasted image 20240412130334.png]]
only square the outside x 
![[Pasted image 20240412130341.png]]

---
# [[Bernoulli Trial]] 
- Binary Outcome 
![[Pasted image 20240407172642.png]]
- ==NOTE==




---

# [[Hypothesis testing]]

- [[Standard error]] = $\frac{s}{\sqrt{ n }}$ 
- P value



---
# Chi Squared Distribution

- This is important because this is what
![[Pasted image 20240407195656.png]]
- Different Margin of error
![[Pasted image 20240407201044.png]]

- The number of degrees of freedom is not n-1 for this it is = n (how many squared normal distrubutions there are)
- This distribution is skewed to the right whatever that means lol 
- This is a forumla that says the same thing as two bullet points above  ![[Pasted image 20240415090725.png]]
- YOU LOSE A DEGREE OF FREEDOM IF YOU ESTIMATE $\mu=\bar{x}$ i.e![[Pasted image 20240415091056.png]]
- 

---
# [[Joint Distributions]]

### Discrete

Good example of how you can get fucked on a test:
![[Pasted image 20240413094436.png]]
![[Pasted image 20240413094321.png|600]]
this example shows that if you want to calculate all the new probability values for Y given you know X is = to -1 then you have to collapse all the x values greater than -1 into the new probability so that it equals to 1. 
Namely here we are dividing by the probability that x = 1 on each term so that it can account for this new knowledge we have. (Probably bayes theorem somehow).

---
# Tree questions 

