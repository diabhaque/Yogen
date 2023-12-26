import math

import torch
from torch.nn import TransformerEncoder, TransformerEncoderLayer


class PositionalEncoding(torch.nn.Module):
    def __init__(self, d_model: int, dropout: float = 0.0, max_len: int = 5000):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)

        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model)
        )
        pe = torch.zeros(max_len, 1, d_model)
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Arguments:
            x: Tensor, shape ``[seq_len, batch_size, embedding_dim]``
        """
        x = x + self.pe[: x.size(0)]
        return self.dropout(x)


class TimeSeriesTransformerModel(torch.nn.Module):
    def __init__(
        self,
        n_features: int,
        d_model: int,
        nhead: int,
        d_hid: int,
        nlayers: int,
        target_size: int = 1, 
        dropout: float = 0.1,
        enc_dropout: float = 0.1,
        device: str = "cpu",
    ):
        super().__init__()
        self.d_model = d_model
        self.embedding = torch.nn.Linear(n_features, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout=enc_dropout)
        self.transformer_encoder = TransformerEncoder(
            TransformerEncoderLayer(d_model, nhead, d_hid, dropout), nlayers
        )
        self.linear = torch.nn.Linear(d_model, target_size)
        self.device = device

    def init_weights(self) -> None:
        initrange = 0.1
        self.linear.bias.data.zero_()
        self.linear.weight.data.uniform_(-initrange, initrange)

    def forward(self, window: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """
        Arguments:
            src: Tensor, shape ``[batch_size, seq_len, n_features]`` -> ``[seq_len, batch_size, n_features]``
            src_mask: Tensor, shape ``[batch_size, seq_len]``

        Returns:
            output: Tensor, shape ``[batch_size, 1]``
        """
        window = window.permute(1, 0, 2)
        window = self.embedding(window)
        window = self.pos_encoder(window)
        output_layer = self.transformer_encoder(window, src_key_padding_mask=mask)
        pooled_output = torch.mean(output_layer, dim=0)
        final_output = self.linear(pooled_output)
        return final_output
