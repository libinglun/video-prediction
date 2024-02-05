import torch


def check_range(tensor, lb: int, ub: int):
    return torch.all((tensor >= lb) & (tensor <= ub))


def has_nan(tensor):
    return torch.isnan(tensor).any()
