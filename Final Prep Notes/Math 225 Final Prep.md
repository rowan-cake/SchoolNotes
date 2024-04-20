
# Topics in review

---
# [[Numerical Methods for ODE's]]
Three main ways 
- [[Eulers Method]]
$$
y_{n+1}=y_{n}+h(f'(x_{n},y_{n}))
$$
said in words to be the y value of the function + the deriative of that function at where you are now times h.
- Foward euler usally undershoots the true $y_{n+1}$ 
- and the Backward euler usally overshoots it

- [[Heun Method]]
said in words you take the average of the the slope at this point and the slope at the next point 
$$
y_{n+1}=y_{n}+h(\frac{(f'(x_{n},y_{n})+{f'(x_{n+1},y_{n+1})})}{2})
$$

- [[Runga-Kuta Method]]


---

# [[Laplace Transform]]

- Note this bottom left identity is good to know!!!!![[Pasted image 20240412205253.png|450]]

---

# [[Disease modeling]]

### Steps

1. ==Define the ODES== (remember that they are related to rates how big the popuation is and such), (coming in - leaving = rate of change from one population to the next)
2. ==NON Dimensinlize the ODES== (I think this is just to make things easier on us sometimes)
3. ==Find the Steady states== (this is where the rate of change in the system is = to zero)
4. ==Draw the NullClines== (Draw the graph and usually you label the [[Endemic]] state and then you label the [[DFE]] which is where everyone is substile but no one has it (1,0,0) and then the [[Epidemic]])
	- if its a population constrain of U+V+R=1 then you can find all the points in terms of $\frac{1}{R_{0}}$ usually which $R_{0}$ represents the reproduction rate of the disease. 
5. ==Test the stability of the solution== (At each of the steady states that you found) (you do this by evaluating the Jacobian at each point and then seeing if the eigen values are):
	- If one eigen value is positive = UNSTABLE
	- If all negative or one negative and rest 0 = STABLE
	- If all are zero cannot draw conclusion
6. ==State Conclusion Clearly== (usally if $R_{0}$>1 then epidemic)

- How to find the eigen values of a 3x3 matrix 

---
# [[Resonance frequency stuff]] 

- ==TRUE Resonance== only happens when you have a homogenous solution that that matches the frequency of the [[Forcing Factor]]. (You also have to have no friction )

- [[Gain factor]]



- Single phase shifted sine 
looks like 
$$
A\sin(\omega\theta+\phi)
$$
where:
$A=$ the amplitude of the sin wave $\sqrt{ (c_{1})^2 +(c_{2})^2}$
$\phi=$ the phase shift which is where the sin starts from $\arctan\left( \frac{c_{2}}{c_{1}} \right)+n\pi$


| Transient solution                               | Steady State Solution                                           |
| ------------------------------------------------ | --------------------------------------------------------------- |
| The [[Second Order Homogenous ODE]] solution     | The [[Particular Solution]]                                     |
| The intial "kicking of the legs" when on a swing | When you are in sync with the [[Particular Solution]] frequency |

