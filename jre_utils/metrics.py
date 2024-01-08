import torch


# class MSELossWeighted(torch.nn.Module):
#     def __init__(self):
#         super().__init__()

#     def forward(self, inputs, targets, weights):
#         return (((inputs - targets) ** 2) * weights).mean()


class MSELossWeighted(torch.nn.Module):
    def __init__(self):
        super(MSELossWeighted, self).__init__()

    def forward(self, input, target, weight):
        """
        Calculate the weighted mean squared error loss.

        Args:
            input (Tensor): Predicted values.
            target (Tensor): Ground truth values.
            weight (Tensor): Weights for each sample.

        Returns:
            Tensor: The weighted MSE loss.
        """
        # Ensure that the weight tensor is broadcastable to the input and target tensors
        weight = weight.view(-1, 1).expand_as(input)

        # Calculate the element-wise squared error
        squared_error = (input - target) ** 2

        # Apply the weights, sum, and then take the mean
        weighted_squared_error = weight * squared_error
        loss = weighted_squared_error.mean()

        return loss
