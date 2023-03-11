import torch
import numpy as np
import matplotlib.pyplot as plt

# Load
model = torch.load(PATH)
model.eval()

inputs, classes = next(iter(val_loader))

model = model.to(device)
inputs=inputs.to(device)

outputs=model(inputs)
_, preds = torch.max(outputs, 1)
preds=preds.cpu().numpy()
classes=classes.numpy()
print(preds)
print(classes)

figure = plt.figure(figsize=(12, 14))
cols, rows = 4, 4
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(val_set), size=(1,)).item()
    
    inp = inputs.cpu()[i-1].numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    
    figure.add_subplot(rows, cols, i)
    plt.title('A: '+index_to_breed[classes[i-1]]+'\nP: '+index_to_breed[preds[i-1]])
    plt.axis("off")
    plt.imshow(inp)

plt.show()

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

model = torch.load(PATH)
model.eval()

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    tensor=tensor.to(device)
    output = model.forward(tensor)
    
    probs = torch.nn.functional.softmax(output, dim=1)
    conf, classes = torch.max(probs, 1)
    return conf.item(), index_to_breed[classes.item()]

image_path="/content/test/06b3a4da7b96404349e51551bf611551.jpg"
image = plt.imread(image_path)
plt.imshow(image)

with open(image_path, 'rb') as f:
    image_bytes = f.read()

    conf,y_pre=get_prediction(image_bytes=image_bytes)
    print(y_pre, ' at confidence score: {0:.2f}'.format(conf))