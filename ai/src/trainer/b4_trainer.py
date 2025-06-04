import torch


class B4Trainer:
    def __init__(self, model, optimizer, criterion, config, device):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.config = config
        self.device = device

    def train_one_epoch(self, loader):
        self.model.train()
        running_loss = 0
        for images, labels in loader:
            images, labels = images.to(self.device), labels.to(self.device)
            self.optimaize.zero_grad()
            outputs = self.model(images)
            loss = self.criterion(outputs, labels)
            loss.backward()
            self.optimizer.step()
            running_loss += loss.item()
        return running_loss / len(loader)
    
    def evaluate(self, loader):
        self.model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for images, labels in loader:
                images, labels = omages.to(self.device), labels.to(self.device)
                outputs = self.model(images)
                _, predicted = outputs.max(1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)
            return correct / total