import matplotlib.pyplot as plt

# total_loss와 val_total_loss 값을 저장할 리스트 생성
total_losses = [
    1.2753,
    1.3369,
    1.4167,
    1.4259,
    1.4412,
    1.3866,
    1.3270,
    1.3170,
    1.2376,
    1.2098,
    1.1699,
    1.1707,
    1.1097,
    1.0923,
    1.1053,
    1.0474,
    1.0522,
    0.99155,
    0.9951,
    0.97016,
    0.93681,
    0.93537,
    0.8553,
    0.82932,
    0.81761,
    0.78086,
    0.73044,
    0.71105,
    0.69185,
    0.67639,
]
val_total_losses = [
    1.3392,
    2.0497,
    2.1685,
    2.3337,
    1.7713,
    1.3804,
    1.5615,
    1.4721,
    1.4332,
    1.6651,
    1.3318,
    1.3561,
    1.2323,
    1.5525,
    1.545,
    1.2456,
    1.3678,
    1.2663,
    1.2857,
    1.1712,
    1.2617,
    1.1418,
    1.1451,
    1.0948,
    1.2056,
    1.1580,
    1.0887,
    1.1129,
    1.1183,
    1.0947,
]

# 에폭(epoch) 수
epochs = range(1, len(total_losses) + 1)

# 그래프 그리기
plt.plot(epochs, total_losses, label="Training loss")
plt.plot(epochs, val_total_losses, label="Validation loss")
plt.title("Training and validation loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

# 그래프 표시
plt.show()
