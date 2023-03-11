import torch
import numpy as np
from torch import nn
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Data generation
# The data generated will be different each time

# Change these parameters if you want to
N = 100 # number of points per class
D = 2 # dimensionality
K = 3 # number of classes
X = np.zeros((N*K,D)) # data matrix (each row = single example)
y = np.zeros(N*K, dtype='uint8') # class labels
for j in range(K):
  ix = range(N*j,N*(j+1))
  r = np.linspace(0.0,1,N) # radius
  t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.3 # theta
  X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
  y[ix] = j

# Turn data into tensors
coordinates = torch.from_numpy(X).type(torch.float) # features as float32
categories = torch.from_numpy(y).type(torch.LongTensor) # labels need to be of type long

class SpiralModel(nn.Module):
  def __init__(self):
    super().__init__()
    self.linear1 = nn.Linear(in_features=2, out_features=10)
    self.linear2 = nn.Linear(in_features=10, out_features=10)
    self.linear3 = nn.Linear(in_features=10, out_features=3)
    self.relu = nn.ReLU()

  def forward(self, x):
    return self.linear3(self.relu(self.linear2(self.relu(self.linear1(x)))))

# Make a spiral model
model = SpiralModel()
# Load model into this spiral model
model.load_state_dict(torch.load('./SpiralModel.pth'))
# Write model to device
model.to(device)
# Evaluate model
model.eval()

# Graph inputs and outputs of the model
def plot_decision_boundary(model, X, y):
  X, y = X.to('cpu'), y.to('cpu')
  x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
  y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
  xx, yy = np.meshgrid(np.linspace(x_min, x_max, 101),np.linspace(y_min, y_max, 101))
  X_to_pred_on = torch.from_numpy(np.column_stack((xx.ravel(), yy.ravel()))).float()
  model.eval()
  with torch.inference_mode():
    y_logits = model(X_to_pred_on)
  if len(torch.unique(y)) > 2:
    y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)
  else: 
    y_pred = torch.round(torch.sigmoid(y_logits))
  y_pred = y_pred.reshape(xx.shape).detach().numpy()
  plt.contourf(xx, yy, y_pred, cmap=plt.cm.RdYlBu, alpha=0.7)
  plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
  plt.xlim(xx.min(), xx.max())
  plt.ylim(yy.min(), yy.max())

# Plot the input data and the categorized output
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('This is the data from the torch.tensor() coordinates')
plt.scatter(coordinates[:, 0], coordinates[:, 1], c=categories, s=40, cmap=plt.cm.RdYlBu)
plt.subplot(1, 2, 2)
plt.title('How this model analyzes and categorizes the data:')
plot_decision_boundary(model, coordinates, categories)
plt.show()