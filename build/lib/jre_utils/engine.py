import torch
from torcheval.metrics import R2Score

from torch.nn import MSELoss
from jre_utils.metrics import MSELossWeighted

from torchmetrics import Accuracy


def train(model, dataloader, optimizer, lr_scheduler, progress_bar=None, device="cpu"):
    model.train()

    running_loss = 0.0
    r2_score = R2Score(device=device)
    mse_loss = MSELoss().to(device)

    for batch in dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}

        outputs = model(batch["window"], batch["mask"])
        loss = mse_loss(outputs, batch["target"])

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        lr_scheduler.step()

        running_loss += loss.item() * len(batch)
        r2_score.update(
            outputs[:, 0].unsqueeze(1).to(device),
            batch["target"][:, 0].unsqueeze(1).to(device),  # get the first column
        )

        if progress_bar is not None:
            progress_bar.update(1)

    return running_loss / len(dataloader), r2_score.compute().item()


def evaluate(model, dataloader, device="cpu"):
    # outputs can have multiple dimensions, R2_score is computed only for the first column
    model.eval()

    running_loss = 0.0
    r2_score = R2Score(device=device)
    mse_loss = MSELoss().to(device)

    with torch.no_grad():
        for batch in dataloader:
            batch = {k: v.to(device) for k, v in batch.items()}

            outputs = model(batch["window"], batch["mask"])
            loss = mse_loss(outputs, batch["target"])

            running_loss += loss.item() * len(batch)
            r2_score.update(
                outputs[:, 0].unsqueeze(1).to(device),
                batch["target"][:, 0].unsqueeze(1).to(device),  # get the first column
            )

    return running_loss / len(dataloader), r2_score.compute().item()


def train_weighted(
    model, dataloader, optimizer, lr_scheduler, progress_bar=None, device="cpu"
):
    model.train()

    running_loss = 0.0
    r2_score = R2Score(device=device)
    mse_loss_weighted = MSELossWeighted().to(device)

    for batch in dataloader:
        batch = {
            k: v.to(device) for k, v in batch.items()
        }  # may be faster to move whole dataloader to device at once

        outputs = model(batch["window"], batch["mask"])
        loss = mse_loss_weighted(outputs, batch["target"], batch["weight"])

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        lr_scheduler.step()

        running_loss += loss.item() * len(batch)
        r2_score.update(
            outputs[:, 0].unsqueeze(1).to(device),
            batch["target"][:, 0].unsqueeze(1).to(device),  # get the first column
        )

        if progress_bar is not None:
            progress_bar.update(1)

    return running_loss / len(dataloader), r2_score.compute().item()


def evaluate_weighted(model, dataloader, device="cpu"):
    model.eval()

    running_loss = 0.0
    r2_score = R2Score(device=device)
    mse_loss_weighted = MSELossWeighted().to(device)

    with torch.no_grad():
        for batch in dataloader:
            batch = {k: v.to(device) for k, v in batch.items()}

            outputs = model(batch["window"], batch["mask"])
            loss = mse_loss_weighted(outputs, batch["target"], batch["weight"])

            running_loss += loss.item() * len(batch)
            r2_score.update(
                outputs[:, 0].unsqueeze(1).to(device),
                batch["target"][:, 0].unsqueeze(1).to(device),  # get the first column
            )

    return running_loss / len(dataloader), r2_score.compute().item()


def train_classification(
    model, dataloader, optimizer, lr_scheduler, progress_bar=None, device="cpu"
):
    model.train()

    running_loss = 0.0
    accuracy = Accuracy(task="multiclass", num_classes=3).to(device)
    criterion = torch.nn.CrossEntropyLoss().to(device)

    for batch in dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}

        outputs = model(batch["window"], batch["mask"])
        loss = criterion(outputs, batch["target"].squeeze(1).to(torch.long))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        lr_scheduler.step()

        running_loss += loss.item() * len(batch["window"])
        accuracy.update(outputs.argmax(dim=1), batch["target"].squeeze())

        if progress_bar is not None:
            progress_bar.update(1)

    return running_loss / len(dataloader), accuracy.compute().item()


def evaluate_classification(model, dataloader, device="cpu"):
    model.eval()

    running_loss = 0.0
    accuracy = Accuracy(task="multiclass", num_classes=3).to(device)
    criterion = torch.nn.CrossEntropyLoss().to(device)

    with torch.no_grad():
        for batch in dataloader:
            batch = {k: v.to(device) for k, v in batch.items()}

            outputs = model(batch["window"], batch["mask"])
            loss = criterion(outputs, batch["target"].squeeze(1).to(torch.long))

            running_loss += loss.item() * len(batch["window"])
            accuracy.update(outputs.argmax(dim=1), batch["target"].squeeze())

    return running_loss / len(dataloader), accuracy.compute().item()


class EarlyStopper:
    def __init__(self, patience=1, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.min_validation_loss = float("inf")

    def early_stop(self, validation_loss):
        if validation_loss < self.min_validation_loss:
            self.min_validation_loss = validation_loss
            self.counter = 0
        elif validation_loss > (self.min_validation_loss + self.min_delta):
            self.counter += 1
            if self.counter >= self.patience:
                return True
        return False
