---
title: "Pstat 126-HW1"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(warning=F, message=F, echo = TRUE)
```

# Question One

To find the Argmin of the function, first we must take the first derivative as shown in class notes. First with respect to X and then to y 

w.r.t. x


$$
\frac{d}{dx} (x^2+y^2-xy)\\
(\frac{d}{dx}(x^2)+\frac{d}{dx}(y^2)+\frac{d}{dx}(xy))\\
2x+0+y=2x+y\\
2x+y
$$
To find the argmin, set the equations equal to 0

$$
2x+y=0\\
-2x=y
$$
Now we also to the same w.r.t. y

$$
\frac{d}{dy} (x^2+y^2-xy)\\
(\frac{d}{dy}(x^2)+\frac{d}{dy}(y^2)+\frac{d}{dy}(xy))\\
0+2y+x\\
$$

Setting the equation equal to 0

$$
2y+x=0\\
-2y=x
$$
we thus have the following equations. 

$$
\frac{d}{dx}f(x,y)=2x+y\\
\frac{d}{dy}f(x,y)=2y+x
$$
solving them both at zero results in 

$$
2x=-y \implies y=-2x\\
2y=-x
\\then\\
2(-2x)=-x \implies 4x=x \implies x=0 \\
$$

We then plug in the x 

$$
2y=-x \implies 2y=0 \implies y=0
$$

meaning out critical points are at (0,0)

Taking the second derivatives
$$
\frac{d^2}{dx^2}f(x,y)=2\\
\frac{d^2}{dy^2}f(x,y)=2
$$

By the second partials test if the second derivative of the function is positive, then it is a minimum value. 

# Question Two
To find $Cov(\hat{\beta}_0, \hat{\beta}_1)$

Recall that $\hat{\beta}_0$ is defined as $\bar{y} - \hat{\beta}_1 \bar{x}$

and so we get 

$$
Cov(\hat{\beta}_0, \hat{\beta}_1) = Cov(\bar{y} - \hat{\beta}_1 \bar{x}, \hat{\beta}_1)
$$

which gets us 

$$
Cov(\bar{y},\hat{\beta_1})-Cov(\hat{\beta}_1\bar{x},\hat{\beta_1})
\\
Cov(\bar{y},\hat{\beta_1})-\bar{x}Cov(\hat{\beta_1},\hat{\beta_1})\\
Cov(\bar{y}, \hat{\beta_1})-\bar{x}\mathbb{V}(\hat{\beta_1})
$$

We know the variance of $\hat{\beta_1}$ to be 

$$
\mathbb{V}(\hat{\beta_1})= \frac{\hat{\sigma}^2}{S_{xx}}
$$

giving us 

$$
Cov(\bar{y}, \hat{\beta_1})-\bar{x}\frac{\hat{\sigma}^2}{S_{xx}}
$$




$$
\begin{align} \operatorname{Cov}(\bar y,\hat{\beta_1})&=\operatorname{Cov}\left(\frac{1}{n}\sum_{i=1}^n y_i,\sum_{i=1}^nc_iy_i\right)\\
&= \frac{1}{n}\sum_{i=1}^nc_i\operatorname{Var}(y_i) \\ 
&= \frac{\sigma^2}{n}\sum_{i=1}^nc_i=0 \end{align}
$$

hence, our final result becomes 

$$
\begin{align}
Cov(\hat{\beta}_0, \hat{\beta}_1)=Cov(\bar{y}, \hat{\beta_1})-\bar{x}\frac{\hat{\sigma}^2}{S_{xx}}\\
&= 0-\bar{x}\frac{\hat{\sigma}^2}{S_{xx}}\\
&=-\bar{x}\frac{\hat{\sigma}^2}{S_{xx}}
\end{align}
$$

# Question Three

We are to show that 
$$Cov(\bar{y}, \hat{\beta}_1 (x_0 - \bar{x})) = 0$$

and so we rewrite our equation also knowing that 

$$
c_i=(\frac{x_o-\bar{x}}{S_{xx}}) \implies c_iS_{xx}=(x_0-\bar{x})
$$

$$
Cov(\frac{1}{n}\sum y, \sum c_i y_i(x_0-\bar{x}))\\
Cov(\frac{1}{n}\sum y, \sum c_i^2 y_i S_{xx})\\
$$
Using bilinearity 

$$
\frac{1}{n} \sum c_i^2 S_{xx} \mathbb{V}(y_i)\\
\frac{\sigma^2S_{xx}}{n} \sum c_i^2
$$

we know that $\sum C_i = 0$ which then gives us our result.


# Question Four 

Time to create a matrix for 

\mathbf{X} = \begin{bmatrix}
2&2&1\\
2&5&2\\
1&2&2
\end{bmatrix}

```{r}
#creating the matrix
A <- matrix(
  data =c(2,2,1,2,5,2,1,2,2),
  nrow = 3)
A
#grabbing the eigen-vectors/values
spec_decomp = eigen(A)
#creation of P 
P = spec_decomp$vectors
#inverse of P
solve(P)
#transposition of P
t(P)

```

to know whether or not something is positive definite, then all the eigen-values must be positive

```{r}
A <- matrix(
  data =c(2,2,1,2,5,2,1,2,2),
  nrow = 3)

eigen(A)
``` 
We see that the eigen values are positive and thus is positive definite. 

# Question Five
```{r}
#grabbing our data
#install.packages("alr4")
library(alr4)
library(ggplot2)
data(UN11)
head(UN11)
```
Considering that we are studying the dependence of fertility on ppgdp. Our response variable will be ppgdp and the predictor variable will be fertility. 

Here we plot fertility on the horizontal axis and ppgdp on the vertical axis

```{r}
ggplot(data=UN11, aes(y=fertility, x=ppgdp))+
  geom_point()+
  xlab("PPGDP")+
  ylab("Fertility")+
  ggtitle("Fertility and PPGDP")
```

As we can see, the data does not intuitively demonstrate a straight line to be the summary of the graph. 

we show this by adding lines to the graph
```{r}
ggplot(data=UN11, aes(y=fertility, x=ppgdp))+
  geom_point()+
  xlab("PPGDP")+
  ylab("Fertility")+
  ggtitle("Fertility and PPGDP")+
  geom_smooth(method=lm, se=F)
```

Seeing this as unreasonable, we ought log our data to make analysis easier. 

```{r}
#adding the logged data to the dataframe

UN11$lnppgdp<- with(UN11, log(ppgdp))
UN11$lnfertility <- with(UN11, log(fertility))
head(UN11)
```

Now we add make our new graph

```{r}
UN11$lnppgdp<- with(UN11, log(ppgdp))
UN11$lnfertility <- with(UN11, log(fertility))
ggplot(data=UN11, aes(y=lnfertility, x=lnppgdp))+
  geom_point()+
  xlab("Log of PPGDP")+
  ylab("Log of Fertility")+
  ggtitle("Logged Fertility and PPGDP")+
  geom_smooth(method=lm, se=F)
```





Using a simple linear regression we get the get the following results 

```{r}
lmod<- lm(formula = ppgdp~fertility, data=UN11)
summary(lmod)
```
Our model now becomes 

$$
\hat{ppgdp}=19712-6047fertility
$$
We decide to test the following: whether the that the slope of the model versus the alternative that it is negative (one-sided test) at a 5% significance level. ie:

$$
H_0: \hat{\beta_1} \ge 0 \\
H_a: \hat{\beta_1} < 0
$$

from earlier, the p value of our model's slope  is 2*e^-16 meaning it is below our rejection region. Thus, we fail to reject the null hypothesis at the 5% significance level 

We see that the the adjusted $R^2$ value is .1898. $R^2$ values are values from one to 0 that represent the proportion of the variance of a dependent variable. Simply put, in our case, 19% of the observed variation can be explained by the inputs of our model. 

we can use the predict function to get our estimate. 

```{r}
#new_data<-data.frame(ppgdp=1000)
#names(new_data)<-c('ppgdp, xi(fertility)')
#predict(lnfertility,
  #      newdata=new_data,
  #      interval='confidence',
   #     level=c(0.95))
```

which leaves us (1.47, 3.23, 7.094)

Niger has the highest fertility. Bosnia and Herzegovina has the lowest fertility. 
