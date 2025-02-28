# Training

## [Transfer Learning with PyTorch](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md)

Transfer learning is a technique for re-training a DNN model on a new dataset, which takes less time than training a network from scratch. With transfer learning, the weights of a pre-trained model are fine-tuned to classify a customized dataset. Please refer to [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md) to learn more.

### Before you start

When building from source PyTorch should be installed. Therfore let's verify that PyTorch is installed and working:

```bash
python3 -c "import torchvision"
```
