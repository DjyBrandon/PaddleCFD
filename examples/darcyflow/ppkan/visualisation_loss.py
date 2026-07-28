import numpy as np
import matplotlib.pyplot as plt

base_dir = "outputs-KANONet/2026-07-29/00-05-01"
train_losses = np.loadtxt(f"{base_dir}/train_losses.txt")
test_losses = np.loadtxt(f"{base_dir}/test_losses.txt")

epochs = np.arange(1, len(train_losses) + 1)

plt.figure(figsize=(8, 5))
plt.plot(epochs, train_losses, label="Training Loss")
plt.plot(epochs, test_losses, label="Test Loss", linestyle="--")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.yscale("log")
plt.title("Training and Test Loss of Bspline-KAN")
plt.legend()
plt.tight_layout()
plt.savefig("../../../tutorials/images/darcyflow_ppkan/loss_curves.png", dpi=300)
# plt.show()
