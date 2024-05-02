import matplotlib.pyplot as plt

# total_loss와 val_total_loss 값을 저장할 리스트 생성
total_losses = [
    2.6134,
    1.0989,
    0.7539,
    0.5615,
    0.4581,
    0.3756,
    0.3291,
    0.2988,
    0.2885,
    0.2939,
    0.2484,
    0.2481,
    0.2255,
    0.2098,
    0.1987,
    0.1868,
    0.2075,
    0.2105,
    0.2258,
    0.1907,
    0.1802,
    0.1675,
    0.1658,
    0.1833,
    0.1792,
    0.1529,
    0.1727,
    0.1428,
    0.1722,
    0.1719,
]
val_total_losses = [
    1.2102,
    0.8434,
    0.6750,
    0.6274,
    0.5986,
    0.6020,
    0.6050,
    0.6218,
    0.6435,
    0.5605,
    0.6086,
    0.5635,
    0.5683,
    0.5675,
    0.6011,
    0.6011,
    0.6189,
    0.6295,
    0.6362,
    0.5930,
    0.5972,
    0.6184,
    0.6231,
    0.6190,
    0.5932,
    0.5816,
    0.5892,
    0.5802,
    0.5804,
    0.6266,
]

# 에폭(epoch) 수
epochs = range(1, len(total_losses) + 1)

# 그래프 그리기
plt.plot(epochs, total_losses, "bo", label="Training loss")
plt.plot(epochs, val_total_losses, "r", label="Validation loss")
plt.title("Training and validation loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

# 그래프 표시
plt.show()
