import torchvision.transforms as transforms
def get_transform():
    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), ((0.5, 0.5, 0.5)))])
    return transform