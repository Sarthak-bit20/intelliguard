import torch, torch.nn as nn
class JudgeNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Dropout(0.2), nn.Linear(16, 8), nn.ReLU(), nn.Linear(8, 1))
    def forward(self, x): return self.network(x)

model = JudgeNN()
model.load_state_dict(torch.load('models/judge.pt', map_location='cpu'))
model.eval()

print('Probs (Safe, Inj, Safe, Inj):', torch.sigmoid(model(torch.tensor([[0.01, 0.99, 0.15, 0.85]]))).item())
print('Probs (Inj, Safe, Inj, Safe):', torch.sigmoid(model(torch.tensor([[0.99, 0.01, 0.85, 0.15]]))).item())
print('Logits (Safe, Inj, Safe, Inj):', torch.sigmoid(model(torch.tensor([[-3.0, 3.0, -2.0, 2.0]]))).item())
print('Logits (Inj, Safe, Inj, Safe):', torch.sigmoid(model(torch.tensor([[3.0, -3.0, 2.0, -2.0]]))).item())
print('Mixed Logits (Inj, Safe, Safe, Inj):', torch.sigmoid(model(torch.tensor([[3.0, -3.0, -2.0, 2.0]]))).item())
