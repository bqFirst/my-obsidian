# PyTorch 环境检查
import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
print(f"cuDNN版本: {torch.backends.cudnn.version()}")
# TensorFlow 环境检查
import tensorflow as tf
print(f"TensorFlow版本: {tf.__version__}")
print(f"GPU 可用: {tf.config.list_physical_devices('GPU')}")
