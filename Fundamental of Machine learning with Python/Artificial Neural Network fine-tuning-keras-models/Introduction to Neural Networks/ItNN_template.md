

```python
from __future__ import print_function
```

#Machine Learning in Python

##Introduction to Neural Networks

###1: Neural networks and iris flowers

Many machine learning prediction problems are rooted in complex data and its non-linear relationships between features. Neural networks are a class of models that can learn these non-linear interactions between variables.

We will introduce neural networks by predicting the species of iris flowers from data with the following features:

- sepal_length - Continuous variable measured in centimeters.
- sepal_width - Continuous variable measured in centimeters.
- petal_length - Continuous variable measured in centimeters.
- petal_width - Continuous variable measured in centimeters.
- species - Categorical. 2 species of iris flowers, Iris-virginica or Iris-versicolor.

The DataFrame class includes a hist() method which creates a histogram for every numeric column in that DataFrame. The histograms are generated using Matplotlib and displayed using plt.show().

####Instructions

Visualize the data using the method hist() on our DataFrame iris and showing the plots.


```python
import pandas

# Read in dataset.
iris = pandas.read_csv("data/iris.csv")
iris.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# Shuffle rows.
shuffled_rows = np.random.permutation(iris.index)
iris = iris.loc[shuffled_rows,:]

print("iris.head():\n", iris.head())

# There are 2 species.
print("iris.species.unique()\n:", iris.species.unique())
iris.hist()
plt.show()
```

    iris.head():
          sepal_length  sepal_width  petal_length  petal_width          species
    113           5.7          2.5           5.0          2.0   Iris-virginica
    81            5.5          2.4           3.7          1.0  Iris-versicolor
    71            6.1          2.8           4.0          1.3  Iris-versicolor
    2             4.7          3.2           1.3          0.2      Iris-setosa
    84            5.4          3.0           4.5          1.5  Iris-versicolor
    iris.species.unique()
    : ['Iris-virginica' 'Iris-versicolor' 'Iris-setosa']
    


![png](output_8_1.png)


###2: Neurons

So far we have talked about methods which do not allow for a large amount of non-linearity, so we must explore other options like neural networks. Neural networks are very loosely inspired by the structure of neurons in the human brain. These models are built by using a series of activation units, known as neurons, to make predictions of some outcome. Neurons take in some input, apply a transformation function, and return an output.

An example neuron is taking in 5 units represented as x, a bias unit, and 4 features. This bias unit is similar in concept to the intercept in linear regression and it will shift the activity of the neuron to one direction or the other. These units are then fed into an activation function $h$. 

We will use the popular sigmoid (logistic) activation function because it returns values between 0 and 1 and can be treated as probabilities:

$\text{Sigmoid Function: }g(z) = \dfrac{1}{1 + e^{-z}}$

This sigmoid function then leads to the corresponding activation function:

$\text{Sigmoid Activation Function: }h_{\Theta}(x) = \dfrac{1}{1+e^{-\Theta^T x}} = \dfrac{1}{1+e^{-(\theta_01 + \theta_1x_1 + \theta_2 x_2)}}$

####Instructions

Write a function called sigmoid_activation with inputs x a feature vector and theta a parameter vector of the same length to implement the sigmoid activation function. Assign the value of sigmoid_activation(X, theta_init) to a1. a1 should be a vector.


```python
z = np.asarray([[9, 5, 4]])
y = np.asarray([[-1, 2, 4]])

# np.dot is used for matrix multiplication.
# z is 1x3 and y is 1x3,  z * y.T is then 3x3.
print("np.dot(z,y.T):", np.dot(z,y.T))

# Variables to test sigmoid_activation.
iris["ones"] = np.ones(iris.shape[0])
X = iris[['ones', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y = (iris.species == 'Iris-versicolor').values.astype(int)

# The first observation.
x0 = X[0]
print("x0:", x0)

# Initialize thetas randomly .
theta_init = np.random.normal(0,0.01,size=(5,1))
def sigmoid_activation(x, theta):
    x = np.asarray(x)
    theta = np.asarray(theta)
    return 1 / (1 + np.exp(-np.dot(theta.T, x)))
                
a1 = sigmoid_activation(x0, theta_init)
print("a1:", a1)
```

    np.dot(z,y.T): [[17]]
    x0: [ 1.   5.7  2.5  5.   2. ]
    a1: [ 0.46644269]
    

###3: Cost function

We can train a single neuron as a two layer network using gradient descent. We need to minimize a cost function which measures the error in our model. The cost function measures the difference between the desired output and actual output, defined as:

$J(\Theta) = -\dfrac{1}{m} \sum_{k=1}^{m} (y_i * log(h_{\Theta}(x_i)) + (1-y_i) log(1-h_{\Theta}(x_i)))$

Since our targets, $y_i$, are binary, either $y_i$ or $(1-y_i)$ will equal zero. One of the terms in the summation will disappear because of this result and. the activation function is then used to compute the error. For example, if we observe a true target, $y_i=1$, then we want $h_{\Theta}(x_i)$ to also be close to 1. So as $h_{\Theta}(x_i)$ approaches 1, the $log(h_{\Theta}(x_i))$ becomes very close to 0. Since the log of a value between 0 and 1 is negative, we must take the negative of the entire summation to compute the cost. The parameters are randomly initialized using a normal random variable with a small variance, less than 0.1.

####Instructions

Write a function that can compute the cost from just a single observation. Write a function singlecost() using input features X, targets y, and parameters theta to compute the cost function. Assign the cost of variables x0, y, and init_theta to variable first_cost.


```python
# First observation's features and target.
x0 = X[0]
y0 = y[0]

# Initialize parameters, we have 5 units and just 1 layer.
theta_init = np.random.normal(0,0.01,size=(5,1))
def singlecost(X, y, theta):
    # Compute activation.
    h = sigmoid_activation(X.T, theta)
    # Take the negative average of target*log(activation) + (1-target) * log(1-activation).
    cost = -np.mean(y * np.log(h) + (1-y) * np.log(1-h))
    return cost

first_cost = singlecost(x0, y0, theta_init)
```

###4: Compute the Gradients

Calculating derivatives are more complicated in neural networks than in linear regression. Here we must compute the overall error and then distribute that error to each parameter. Compute the derivative using the chain rule:

$\dfrac{\partial J}{\partial \theta_j} = \dfrac{\partial J}{\partial h(\Theta)} \dfrac{\partial h(\Theta)}{\partial \theta_j}$

This rule may look complicated, but we can break it down. The first part is computing the error between the target variable and prediction. The second part then computes the sensitivity relative to each parameter. In the end, the gradients are computed as: $\delta = (y_i - h_\Theta(x_i)) * h_\Theta(x_i) * (1-h_\Theta(x_i)) * x_i$.

Now we will step through the math. $(y_i - h_\Theta(x_i))$ is a scalar and the error between our target and prediction. $h_\Theta(x_i) * (1-h_\Theta(x_i))$ is also a scalar and the sensitivity of the activation function. $x_i$ is the features for our observation $i$. $\delta$ is then a vector of length 5, 4 features plus a bias unit, corresponding to the gradients.

To implement this, we compute $\delta$ for each observation, then average to get the average gradient. The average gradient is then used to update the corresponding parameters.

####Instructions

Compute the average gradients over each observation in X and corresponding target y with the initialized parameters theta_init. Assign the average gradients to variable grads.

Write a function gradients() which will estimate and return the gradient of each parameter in a vector. The inputs of this function should be features (X), observations (y), a set of parameters (theta), and an epsilon (eps) to control the numerial computation. Assign the gradients using theta_init, X, y, and eps to variable first_gradient.


```python
# Initialize parameters.
theta_init = np.random.normal(0,0.01,size=(5,1))

# Store the updates into this array.
grads = np.zeros(theta_init.shape)

# Number of observations.
n = X.shape[0]
for j, obs in enumerate(X):
    # Compute activation.
    h = sigmoid_activation(obs, theta_init)
    # Get delta.
    delta = (y[j]-h) * h * (1-h) * obs
    # Accumulate.
    grads += delta[:,np.newaxis]/X.shape[0]
```

###5: Two layer network

Now that you can compute the gradients, use gradient descent to learn the parameters and predict the species of iris flower given the 4 features. Gradient descent minimizes the cost function by adjusting the parameters accordingly. Adjust the parameters by substracting the product of the gradients and the learning rate from the previous parameters. Repeat until the cost function coverges or a maximum number of iterations is reached.

The high level algorithm is,

    while ( number_of_iterations < max_iterations and (prev_cost - cost) > convergence_thres ) {
      update paramaters
      get new cost
      repeat
    }

We have implemented all these pieces in a single function learn() that can learn this two layer network. After setting a few initial variables, we begin to iterate until convergence. During each iteration we compute our gradients, update accordingly, and compute the new cost.


```python
import matplotlib.pyplot as plt
%matplotlib inline

theta_init = np.random.normal(0,0.01,size=(5,1))

# Set a learning rate.
learning_rate = 0.1
# Maximum number of iterations for gradient descent.
maxepochs = 10000       
# Costs convergence threshold, ie. (prevcost - cost) > convergence_thres.
convergence_thres = 0.0001  

def learn(X, y, theta, learning_rate, maxepochs, convergence_thres):
    costs = []
    cost = singlecost(X, y, theta) # Compute initial cost.
    costprev = cost + convergence_thres + 0.01 # Set an inital costprev to past while loop.
    counter = 0 # Add a counter.
    # Loop through until convergence.
    for counter in range(maxepochs):
        grads = np.zeros(theta.shape)
        for j, obs in enumerate(X):
            h = sigmoid_activation(obs, theta) # Compute activation.
            delta = (y[j]-h) * h * (1-h) * obs # Get delta.
            grads += delta[:,np.newaxis]/X.shape[0] # Accumulate.
        
        # Update parameters.
        theta += grads * learning_rate
        counter += 1
        costprev = cost # Store prev cost.
        cost = singlecost(X, y, theta) # Compute new cost.
        costs.append(cost)
        if np.abs(costprev-cost) < convergence_thres:
            break
        
    plt.plot(costs)
    plt.title("Convergence of the Cost Function")
    plt.ylabel("J($\Theta$)")
    plt.xlabel("Iteration")
    plt.show()
    return theta
        
theta = learn(X, y, theta_init, learning_rate, maxepochs, convergence_thres)
```


![png](output_26_0.png)


###6: Neural Network

Neural networks are usually built using mulitple layers of neurons. Adding more layers into the network allows you to learn more complex functions.

An example neural network has 3 layer neural network with four input variables x1,x2,x3, and x4 and a bias unit. Each variable and bias unit is then sent to four hidden units, a(2)1,a(2)2,a(2)3, and a(2)4. The hidden units have different sets of parameters $\theta$.

$a_1^{(2)} = g(\theta_{1,0}^{(1)} + \theta_{1,1}^{(1)} x_1 + \theta_{1,2}^{(1)} x_2 + \theta_{1,3}^{(1)} x_3 + \theta_{1,4}^{(1)} x_4)$

$a_2^{(2)} = g(\theta_{2,0}^{(1)} + \theta_{2,1}^{(1)} x_1 + \theta_{2,2}^{(1)} x_2 + \theta_{2,3}^{(1)} x_3 + \theta_{2,4}^{(1)} x_4)$

$a_3^{(2)} = g(\theta_{3,0}^{(1)} + \theta_{3,1}^{(1)} x_1 + \theta_{3,2}^{(1)} x_2 + \theta_{3,3}^{(1)} x_3 + \theta_{3,4}^{(1)} x_4)$

$a_4^{(2)} = g(\theta_{4,0}^{(1)} + \theta_{4,1}^{(1)} x_1 + \theta_{4,2}^{(1)} x_2 + \theta_{4,3}^{(1)} x_3 + \theta_{4,4}^{(1)} x_4)$

$\theta_{i,k}^{(j)}$ represents the parameter of input unit $k$ which transform the units in layer $j$ to activation unit $a_i^{(j+1)}$.

This layer is known as a hidden layer because the user does not directly interact with it by passing or retrieving data. The third and final layer is the output, or prediction, of our model. Similar to how each variable was sent to each neuron in the hidden layer, the activation units in each neuron are then sent to each neuron on the next layer. Since there is only a single layer, we can write it as:

$h_{\Theta}(X) = g(\theta_{1,0}^{(2)} + \theta_{1,1}^{(2)} a_1^{(2)} + \theta_{1,2}^{(2)} a_2^{(2)} + \theta_{1,3}^{(2)} a_3^{(2)} + \theta_{1,4}^{(2)} a_4^{(2)})$

While the mathematical notation may seem confusing at first, at a high level, we are organizing multiple logistic regression models to create a more complex function.

####Instructions

Write a function feedforward() that will take in an input X and two sets of parameters theta0 and theta1 to compute the output $h_{\Theta}(X)$. Assign the output to variable h using features X and parameters theta0_init and theta1_init.


```python
theta0_init = np.random.normal(0,0.01,size=(5,4))
theta1_init = np.random.normal(0,0.01,size=(5,1))

def feedforward(X, theta0, theta1):
    # Feedforward to the first layer.
    a1 = sigmoid_activation(X.T, theta0).T
    # Add a column of ones for bias term.
    a1 = np.column_stack([np.ones(a1.shape[0]), a1])
    # Activation units are then inputted to the output layer.
    out = sigmoid_activation(a1.T, theta1)
    return out

h = feedforward(X, theta0_init, theta1_init)
print("h:\n", h)
```

    h:
     [[ 0.50367013  0.50367445  0.50367333  0.50368859  0.50367454  0.50367181
       0.50368795  0.50367393  0.50366919  0.50368791  0.50368751  0.50368864
       0.50366186  0.50368741  0.50368806  0.50368673  0.5036875   0.5036744
       0.50368878  0.5036868   0.50368673  0.5036737   0.50368882  0.5036696
       0.5036677   0.5036877   0.50367228  0.50368852  0.50367202  0.50367098
       0.50367415  0.50367679  0.50366931  0.50367228  0.50366743  0.50367529
       0.50367115  0.50367387  0.50366882  0.50366893  0.50368748  0.50368719
       0.50366685  0.50366804  0.50367016  0.50368673  0.50367231  0.50367113
       0.50366437  0.50367415  0.50366832  0.50368983  0.5036664   0.50366996
       0.50366208  0.50367336  0.50368674  0.50366762  0.50367418  0.50366416
       0.50367541  0.50367094  0.50368772  0.50367321  0.50368573  0.5036693
       0.5036889   0.50368978  0.50367276  0.50368702  0.5036877   0.5036704
       0.50365874  0.50366385  0.5036868   0.50367126  0.50367883  0.50367099
       0.50367167  0.50366031  0.50366619  0.5036891   0.50367265  0.50366991
       0.50367097  0.50368573  0.50366759  0.50366328  0.50366695  0.50367016
       0.50368793  0.50366756  0.50366822  0.50366753  0.50368828  0.50366883
       0.50367615  0.50368774  0.50368735  0.50366172  0.5036865   0.5036702
       0.5036742   0.50368568  0.50366992  0.50367514  0.5036723   0.50365743
       0.50366699  0.50367116  0.50368807  0.50366708  0.50367396  0.50368943
       0.50368941  0.50367193  0.50368871  0.503688    0.50367011  0.50367292
       0.50368951  0.5036687   0.50366745  0.50369165  0.50367423  0.50368897
       0.50368766  0.50366874  0.50366821  0.50368969  0.50367451  0.50366999
       0.50367711  0.50366652  0.50366812  0.50366888  0.50368976  0.50366857
       0.50367416  0.50368666  0.50367058  0.50366681  0.50366451  0.50366825
       0.50367316  0.50368745  0.50367782  0.5036865   0.50366292  0.50368819]]
    

###7: Multiple neural network cost function

The cost function to multiple layer neural networks is identical to the cost function previously used above, but hΘ(xi) is more complicated.

$J(\Theta) = -\dfrac{1}{m} \sum_{i=1}^m (y_{i} * log(h_{\Theta}(x_{i}))  +  (1-y_{i}) log(1-h_{\Theta}(x_i))$

####Instructions

Write a function multiplecost() which estimates the cost function. Use the observations in X, targets y and inital parameters theta0_init and theta1_init. Assign the cost to variable c.


```python
theta0_init = np.random.normal(0,0.01,size=(5,4))
theta1_init = np.random.normal(0,0.01,size=(5,1))

# X and y are in memory and should be used as inputs to multiplecost().
def multiplecost(X, y, theta0, theta1):
    # Feed through network.
    h = feedforward(X, theta0, theta1) 
    # Compute error.
    inner = y * np.log(h) + (1-y) * np.log(1-h)
    # Negative of average error.
    return -np.mean(inner)

c = multiplecost(X, y, theta0_init, theta1_init)
print("c:", c)
```

    c: 0.696836613836
    

###8: Backpropagation

Now that we have mulitple layers of parameters to learn, we must implement a method called backpropagation. We've already implemented forward propagation by feeding the data through each layer and returning an output. Backpropagation focuses on updating parameters starting at the last layer and circling back through each layer, updating accordingly. As there are multiple layers we are forced to compute $\dfrac{\partial}{\partial \Theta_{i,j}^{(l)}} J(\Theta)$ where $l$ is the layer. For a three layer network, use the following approach,

$\delta_j^l \text{ is the 'error' for unit j in layer l}$

$\delta^3 = h_\Theta(X) - y$

$\delta^2 = (\Theta^{(2)})^T \delta^3 .* g^{'}(z^{(2)})$

$\text{There is no } \delta^1 \text{ since the first layer are the features and have no error.}$

In the code cell below, we have written code to train a three layer neural network. You will notice that there are many parameters and moving parts to this algorithm. To make the code more modular, we have refactored our previous code as a class, allowing us to organize related attributes and methods.

We have reused feedforward() and multiplecost() but in more condensed forms. During initialization, we set attributes like the learning rate, maximum number of iterations to convergence, and number of units in the hidden layer. In learn() you'll find the backpropagation algorithm, which computes the gradients and updates the parameters. We then test the class by using the features and the species of the flower.


```python
import matplotlib.pyplot as plt
%matplotlib inline

# Use a class for this model, it's good practice and condenses the code.
class NNet3:
    def __init__(self, learning_rate=0.5, maxepochs=1e4, convergence_thres=1e-5, hidden_layer=4):
        self.learning_rate = learning_rate
        self.maxepochs = int(maxepochs)
        self.convergence_thres = 1e-5
        self.hidden_layer = int(hidden_layer)
        
    def _multiplecost(self, X, y):
        # Feed through network.
        l1, l2 = self._feedforward(X) 
        # Compute error.
        inner = y * np.log(l2) + (1-y) * np.log(1-l2)
        # Negative of average error.
        return -np.mean(inner)
    
    def _feedforward(self, X):
        # Feedforward to the first layer.
        l1 = sigmoid_activation(X.T, self.theta0).T
        # Add a column of ones for bias term.
        l1 = np.column_stack([np.ones(l1.shape[0]), l1])
        # Activation units are then inputted to the output layer.
        l2 = sigmoid_activation(l1.T, self.theta1)
        return l1, l2
    
    def predict(self, X):
        _, y = self._feedforward(X)
        return y
    
    def learn(self, X, y):
        nobs, ncols = X.shape
        self.theta0 = np.random.normal(0,0.01,size=(ncols,self.hidden_layer))
        self.theta1 = np.random.normal(0,0.01,size=(self.hidden_layer+1,1))
        
        self.costs = []
        cost = self._multiplecost(X, y)
        self.costs.append(cost)
        costprev = cost + self.convergence_thres+1 # Set an inital costprev to past while loop.
        counter = 0 # Intialize a counter.

        # Loop through until convergence.
        for counter in range(self.maxepochs):
            # Feedforward through network.
            l1, l2 = self._feedforward(X)

            # Start backpropagation.
            # Compute gradients.
            l2_delta = (y-l2) * l2 * (1-l2)
            l1_delta = l2_delta.T.dot(self.theta1.T) * l1 * (1-l1)

            # Update parameters by averaging gradients and multiplying by the learning rate.
            self.theta1 += l1.T.dot(l2_delta.T) / nobs * self.learning_rate
            self.theta0 += X.T.dot(l1_delta)[:,1:] / nobs * self.learning_rate
            
            # Store costs and check for convergence.
            counter += 1
            costprev = cost # Store prev cost.
            cost = self._multiplecost(X, y) # Get next cost.
            self.costs.append(cost)
            if np.abs(costprev-cost) < self.convergence_thres and counter > 500:
                break

# Set a learning rate.
learning_rate = 0.5
# Maximum number of iterations for gradient descent.
maxepochs = 10000       
# Costs convergence threshold, ie. (prevcost - cost) > convergence_thres.
convergence_thres = 0.00001  
# Number of hidden units.
hidden_units = 4

# Initialize model.
model = NNet3(learning_rate=learning_rate, maxepochs=maxepochs,
              convergence_thres=convergence_thres, hidden_layer=hidden_units)
# Train model.
model.learn(X, y)

# Plot costs.
plt.plot(model.costs)
plt.title("Convergence of the Cost Function")
plt.ylabel("J($\Theta$)")
plt.xlabel("Iteration")
plt.show()
```


![png](output_39_0.png)


###9: Splitting data

Now that we have learned about neural networks, learned about backpropagation, and have code which will train a 3-layer neural network, we will split the data into training and test datasets and run the model.

####Instructions

Choose the first 70 rows in both X and y assigning them respectively to X_train and y_train. The last 30 rows should be assigned to variables X_test and y_test.


```python
# First 70 rows to X_train and y_train.
# Last 30 rows to X_train and y_train.
X_train = X[:70]
y_train = y[:70]

X_test = X[-30:]
y_test = y[-30:]
```

###10: Predicting iris flowers

To benchmark how well a three layer neural network performs when predicting the species of iris flowers, you will have to compute the AUC, area under the curve, score of the receiver operating characteristic. The function NNet3 not only trains the model but also returns the predictions. The method predict() will return a 2D matrix of probabilities. Since there is only one target variable in this neural network, select the first row of this matrix, which corresponds to the type of flower.

####Instructions

Train the neural network using X_test and y_test and model, which has been initialized with a set of parameters. Once training is complete, use the predict() function to return the probabilities of the flower matching the species Iris-versicolor. Compute the AUC score, using roc_auc_score() and assign it to auc.


```python
from sklearn.metrics import roc_auc_score

# Set a learning rate.
learning_rate = 0.5
# Maximum number of iterations for gradient descent.
maxepochs = 10000       
# Costs convergence threshold, ie. (prevcost - cost) > convergence_thres.
convergence_thres = 0.00001  
# Number of hidden units.
hidden_units = 4

# Initialize model.
model = NNet3(learning_rate=learning_rate, maxepochs=maxepochs,
              convergence_thres=convergence_thres, hidden_layer=hidden_units)
model.learn(X_train, y_train)

yhat = model.predict(X_test)[0]
print("yhat:\n", yhat)

auc = roc_auc_score(y_test, yhat)
print("auc:", auc)
```

    yhat:
     [ 0.03813336  0.53067014  0.53142452  0.01621694  0.52952666  0.03103196
      0.07921387  0.53096063  0.53104193  0.02971528  0.52387143  0.52910485
      0.51003402  0.53142621  0.53168838  0.52994371  0.02100924  0.53116928
      0.52214693  0.05558063  0.52898834  0.53162224  0.5316589   0.53058843
      0.52622519  0.07020778  0.50794709  0.0981216   0.53179472  0.03494109]
    auc: 0.486772486772
    
