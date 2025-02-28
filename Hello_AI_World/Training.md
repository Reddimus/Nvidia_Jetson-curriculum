# Training

## [Transfer Learning with PyTorch](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md)

Transfer learning is a technique for re-training a DNN model on a new dataset, which takes less time than training a network from scratch. With transfer learning, the weights of a pre-trained model are fine-tuned to classify a customized dataset. Please refer to [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md) to learn more.

### Before you start

When building from source PyTorch should be installed.

If PyTorch is not installed dont worry we can install it now in the `build` directory:

```bash
./install-pytorch.sh
```

> Note: If you are still having trouble installing PyTorch, please run `sudo pip3 install -U pip` and `sudo pip3 install -U cython` and then try again.

Let's verify that PyTorch is installed and working:

```bash
python3
```

```python
import torch
print(torch.__version__)
print('CUDA available: ' + str(torch.cuda.is_available()))
a = torch.cuda.FloatTensor(2).zero_()
print('Tensor a = ' + str(a))
b = torch.randn(2).cuda()
print('Tensor b = ' + str(b))
c = a + b
print('Tensor c = ' + str(c))

import torchvision
print(torchvision.__version__)
```

> If PyTorch is not installed, please refer to [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md#installing-pytorch).

