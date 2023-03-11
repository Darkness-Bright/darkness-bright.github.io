# https://pytorch.org/docs/stable/torch.html


import torch

# Set seed
torch.manual_seed(42)

# Setup device-agnostic code 
if torch.cuda.is_available():
  device = "cuda" # NVIDIA GPU
elif torch.backends.mps.is_available():
  device = "mps" # Apple GPU
else:
  device = "cpu"

"""
Data types:

torch.bool
torch.uint8
torch.int8
torch.int16 or torch.short
torch.int32 or torch.int
torch.int64 or torch.long
torch.float16 or torch.half
torch.float32 or torch.float
torch.float64 or torch.double
torch.complex64 or torch.cfloat
torch.complex128 or torch.cdouble
"""
"""
Settings:

torch.set_default_dtype(d)
Sets the default floating point dtype to d.

torch.get_default_dtype()
Get the current default floating point dtype.

torch.set_default_tensor_type(t)
Sets the default torch.torch.tensor type to floating point tensor type t.
"""
torch.set_default_dtype(torch.half)
print('Floating point default dtype:',torch.get_default_dtype())





"""
Print options:

torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)
Set options for printing.

precision – Number of digits of precision for floating point output (default = 4).

threshold – Total number of array elements which trigger summarization rather than full repr (default = 1000).

edgeitems – Number of array items in summary at beginning and end of each dimension (default = 3).

linewidth – The number of characters per line for the purpose of inserting line breaks (default = 80). Thresholded matrices will ignore this parameter.

profile – Sane defaults for pretty printing. Can override with any of the above options. (any one of default, short, full)

sci_mode – Enable (True) or disable (False) scientific notation. If None (default) is specified, the value is defined by torch._tensor_str._Formatter. This value is automatically chosen by the framework.
"""
torch.set_printoptions(precision=3, threshold=9, edgeitems=1)

"""
torch.tensor creation:

torch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)

torch.tensor.full(size, fill_value)
Returns a torch.tensor of size size filled with fill_value.

torch.tensor.empty(size)
Returns a torch.tensor of size size filled with uninitialized data.

torch.tensor.ones(size)
Returns a torch.tensor of size size filled with 1.

torch.tensor.zeros(size)
Returns a torch.tensor of size size filled with 0.
"""
tensor = torch.tensor([[0.1, 1.2], [2.2, 3.1], [4.9, 5.2]], dtype=torch.double)

print(tensor)

"""
torch.sparse_coo_tensor creation:

torch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)
"""
sparse_coo_tensor = torch.sparse_coo_tensor(torch.empty([1, 0]), torch.empty([0, 2]), [1, 2])

print(sparse_coo_tensor)

"""
Tensor methods:
Note: there are over 100 tensor methods...

tensor.T
Returns a view of this tensor with its dimensions reversed.

tensor.H
Returns a view of a matrix (2-D tensor) conjugated and transposed.

tensor.mT
Returns a view of this tensor with the last two dimensions transposed.

tensor.abs()
Returns the absolute value of each element in the tensor.

tensor.mean()
Returns the mean value of all elements in the tensor.

tensor.max()
Returns the maximum value of all elements in the tensor.

tensor.min()
Returns the minimum value of all elements in the tensor.

tensor.exp()
Returns the exponential of each element in the tensor.

tensor.sin()
Returns the sine of each element in the tensor.

tensor.cos()
Returns the cosine of each element in the tensor.

tensor.mm(matrix)
Perform matrix multiplication with a matrix.

tensor.transpose(dim1, dim2)
Transposes the dimensions dim1 and dim2 in the tensor.
"""
print(tensor.T)
print(tensor.max())

"""
Check:

torch.is_tensor(input)
Returns True if obj is a PyTorch tensor.

torch.is_storage(input)
Returns True if obj is a PyTorch storage object.

torch.is_complex(input)
Returns True if the data type of input is a complex data type i.e., one of torch.complex64, and torch.complex128.

torch.is_conj(input)
Returns True if the input is a conjugated tensor, i.e. its conjugate bit is set to True.

torch.is_floating_point(input)
Returns True if the data type of input is a floating point data type i.e., one of torch.float64, torch.float32, torch.float16, and torch.bfloat16.

torch.is_nonzero(input)
Returns True if the input is a single element tensor which is not equal to zero after type conversions.

torch.numel(input)
Returns the total number of elements in the input tensor.
"""















from torch import nn

class Model(nn.Module):
  def __init__(self, input_size, hidden_size, num_layers, num_classes):
    super(Model, self).__init__()
    self.hidden_size = hidden_size
    self.num_layers = num_layers
    self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
    self.fc = nn.Linear(hidden_size * 2, num_classes)
  def forward(self, x):
    h0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)
    c0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)
    out, _ = self.lstm(x, (h0, c0))
    out = self.fc(out[:, -1, :])
    return out







"""
import requests
from bs4 import BeautifulSoup
def get_html(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
  else:
    text = ""
  return text



class Consciousness(nn.Module):
  def __init__(self, input_size, hidden_size, output_size):
    super(Consciousness, self).__init__()
    self.fc1 = nn.Linear(input_size, hidden_size)
    self.fc2 = nn.Linear(hidden_size, output_size)
  
  def forward(self, x):
    x = self.fc1(x)
    x = torch.relu(x)
    x = self.fc2(x)
    return x

# Make model
# input shape: torch.Size([256])
# output shape: torch.Size([256])
model = Consciousness(input_size=256, hidden_size=256, output_size=256)

# Random tensor
input = torch.tensor()
print

# Loop 300
for i in range(300):
  output = model
  print(output)
"""


"""
# The data
string = get_html("https://www.google.com/search?q=记得记得")


numbers = []
for i in string:
  numbers.append(ord(i))

numbers = [(i - 32767) * -1 if i > 32767 else i for i in numbers]

tensor = torch.tensor(numbers,dtype=torch.int16)

print(tensor)
print(tensor.shape)

"""