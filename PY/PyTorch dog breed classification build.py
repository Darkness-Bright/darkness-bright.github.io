import torch
import torch.nn.functional as F
import torchvision

from torchvision import transforms
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
from torch.optim import lr_scheduler

import time
import os
import copy
import io

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from PIL import Image

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

label_df = pd.read_csv('labels.csv')

print('Training set: {}'.format(label_df.shape))

# Encode the breed into digits
label_df['label'] = LabelEncoder().fit_transform(label_df.breed)

# Create a breed-2-index dictionary
dict_df = label_df[['label','breed']].copy()
dict_df.drop_duplicates(inplace=True)
dict_df.set_index('label',drop=True,inplace=True)

index_to_breed = dict_df.to_dict()['breed']

train_dir='train'

label_df.id = label_df.id.apply(lambda x: x+'.jpg')
label_df.id = label_df.id.apply(lambda x:train_dir+'/'+x)

# Drop the breed column
label_df.pop('breed')

class DogDataset(Dataset):
    def __init__(self,dataframe,transform=None,test=False):
        self.dataframe = dataframe
        self.transform = transform
        self.test = test
        
    def __getitem__(self,index):
        x = Image.open(self.dataframe.iloc[index,0])
        if self.transform:
            x = self.transform(x)
        if self.test:
            return x
        else:
            y = self.dataframe.iloc[index,1]
            return x,y
        
    def __len__(self):
        return self.dataframe.shape[0]

# Creat transfomers
train_transformer = transforms.Compose([transforms.RandomResizedCrop(224),
                                        transforms.RandomRotation(15),
                                        transforms.RandomHorizontalFlip(),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

val_transformer = transforms.Compose([transforms.Resize(256),
                                      transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

batch_size = 64

train_df,test_df=train_test_split(label_df, test_size=0.1, random_state=0)

train_df.shape,test_df.shape

# Create dataloaders form datasets
train_set = DogDataset(train_df, transform=train_transformer)
val_set = DogDataset(test_df, transform=val_transformer)

train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_set , batch_size=batch_size, shuffle=True)

dataset_sizes=len(train_set)

print(dataset_sizes,len(val_set))

# Get a batch of training data
inputs, classes = next(iter(val_loader))
classes=classes.numpy()

figure = plt.figure(figsize=(12, 12))
cols, rows = 4, 4
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(val_set), size=(1,)).item()
    
    inp = inputs[i-1].numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    
    figure.add_subplot(rows, cols, i)
    plt.title(index_to_breed[classes[i-1]])
    plt.axis("off")
    plt.imshow(inp)
plt.show()

# Use resnet-50 as a base model
class Model(torch.nn.Module):
    def __init__(self, base_model, base_out_features, num_classes):
        super(Model,self).__init__()
        self.base_model=base_model
        self.linear1 = torch.nn.Linear(base_out_features, 512)
        self.output = torch.nn.Linear(512,num_classes)
    def forward(self,x):
        x = F.relu(self.base_model(x))
        x = F.relu(self.linear1(x))
        x = self.output(x)
        return x

resNet = torchvision.models.resnet50(pretrained=True)

# Setting up gpu
device = "cuda" if torch.cuda.is_available() else "cpu"

for param in resNet.parameters():
    param.requires_grad=False

model = Model(base_model=resNet, base_out_features=resNet.fc.out_features, num_classes=120)
model = model.to(device)

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):    
    since = time.time()
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print(f'Epoch {epoch}/{num_epochs - 1}')
        print('-' * 10)

        model.train()  # Set model to training mode    
        running_loss = 0.0
        running_corrects = 0

        # Iterate over data.
        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward
            # track history if only in train
            with torch.set_grad_enabled(True):
                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)
                loss = criterion(outputs, labels)

                loss.backward()
                optimizer.step()

                # statistics
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            
        scheduler.step()

        epoch_loss = running_loss / dataset_sizes
        epoch_acc = running_corrects.double() / dataset_sizes

        print(f' Training Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

        # deep copy the model
        if epoch_acc > best_acc:
            best_acc = epoch_acc
            best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
    print(f'Best val Acc: {best_acc:4f}')

    # load best model weights
    model.load_state_dict(best_model_wts)
    
    return model

# Cost function and optimzier
loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam([param for param in model.parameters() if param.requires_grad], lr=0.0003)

scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

model = train_model(model, loss_function, optimizer,scheduler)

# Specify a path
PATH = "DogBreedClassifierModel.pth"

# Save
torch.save(obj=model.state_dict(),f=PATH)
print('Model saved to '+PATH)
