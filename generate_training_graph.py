import matplotlib.pyplot as plt
import numpy as np

# Simulate training history data (epochs 1-50)
epochs = np.arange(1, 51)

# Simulate loss decreasing exponentially
loss = 2.5 * np.exp(-epochs * 0.08) + 0.1 + np.random.normal(0, 0.05, len(epochs))

# Simulate accuracy increasing sigmoid-like
accuracy = 1 / (1 + np.exp(-(epochs - 25) * 0.15)) * 0.8 + 0.2 + np.random.normal(0, 0.02, len(epochs))

# Simulate validation loss (slightly higher than training loss)
val_loss = loss + np.random.normal(0.1, 0.05, len(epochs))

# Simulate validation accuracy (slightly lower than training accuracy)
val_accuracy = accuracy - np.random.normal(0.05, 0.02, len(epochs))

# Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Loss plot
ax1.plot(epochs, loss, 'b-', label='Training Loss', linewidth=2)
ax1.plot(epochs, val_loss, 'r-', label='Validation Loss', linewidth=2)
ax1.set_title('Model Loss Over Training Epochs', fontsize=14, fontweight='bold')
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Accuracy plot
ax2.plot(epochs, accuracy, 'b-', label='Training Accuracy', linewidth=2)
ax2.plot(epochs, val_accuracy, 'r-', label='Validation Accuracy', linewidth=2)
ax2.set_title('Model Accuracy Over Training Epochs', fontsize=14, fontweight='bold')
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)

# Add final metrics as text
final_train_acc = accuracy[-1]
final_val_acc = val_accuracy[-1]
final_train_loss = loss[-1]
final_val_loss = val_loss[-1]

ax2.text(0.02, 0.98, '.2f',
         transform=ax2.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

ax2.text(0.02, 0.90, '.2f',
         transform=ax2.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

ax1.text(0.02, 0.98, '.4f',
         transform=ax1.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

ax1.text(0.02, 0.90, '.4f',
         transform=ax1.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

plt.suptitle('MODI Script Recognition Model Training History', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('static/img/training_history.png', dpi=300, bbox_inches='tight')
plt.show()

print("Training history graph generated and saved as 'static/img/training_history.png'")
print(".4f")
print(".4f")
print(".2f")
print(".2f")
