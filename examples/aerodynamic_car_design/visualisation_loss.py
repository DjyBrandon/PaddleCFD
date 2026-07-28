import numpy as np
import matplotlib.pyplot as plt

base_dir = "output/Transolver/20260725_124606"
train_loss = np.loadtxt(f"{base_dir}/train_loss_200.txt")
val_loss = np.loadtxt(f"{base_dir}/val_loss_200.txt")

epochs = np.arange(1, len(train_loss) + 1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss, label="Training Loss", linewidth=2)
plt.plot(epochs, val_loss, label="Validation Loss", linewidth=2, linestyle="--")
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Loss", fontsize=12)
plt.title("Training and Validation Loss Curves", fontsize=14)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("../../tutorials/images/aerodynamic_car_design/loss_curves.png", dpi=300)
# plt.show()
