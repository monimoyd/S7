# S7
Repository for assignment S7

In this assignment I have trainded CIPHAR 10 dataset using CNN. I have developed APIs for loading data, training, testing and getting and plotting metrics

Number of Parameters: 358,016
Number of Epochs: 25
Best Validation Accuracy: 84.53%
Final Validation Accuracy: 84.47%

The logs are as below:

  0%|          | 0/391 [00:00<?, ?it/s]

EPOCH: 0

/content/model.py:99: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
  return F.log_softmax(x)
Loss=3.0993175506591797 Batch_id=390 Accuracy=45.47: 100%|██████████| 391/391 [00:18<00:00, 21.68it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 1.1598, Accuracy: 5830/10000 (58.30%)

EPOCH: 1

Loss=2.338263750076294 Batch_id=390 Accuracy=59.94: 100%|██████████| 391/391 [00:18<00:00, 21.49it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 1.1825, Accuracy: 5813/10000 (58.13%)

EPOCH: 2

Loss=2.075066566467285 Batch_id=390 Accuracy=63.34: 100%|██████████| 391/391 [00:18<00:00, 22.84it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 1.0150, Accuracy: 6443/10000 (64.43%)

EPOCH: 3

Loss=1.9200961589813232 Batch_id=390 Accuracy=65.59: 100%|██████████| 391/391 [00:18<00:00, 21.46it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 1.0760, Accuracy: 6260/10000 (62.60%)

EPOCH: 4

Loss=1.8132764101028442 Batch_id=390 Accuracy=66.88: 100%|██████████| 391/391 [00:18<00:00, 21.16it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.9558, Accuracy: 6677/10000 (66.77%)

EPOCH: 5

Loss=1.925611138343811 Batch_id=390 Accuracy=68.00: 100%|██████████| 391/391 [00:18<00:00, 21.36it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.9954, Accuracy: 6538/10000 (65.38%)

EPOCH: 6

Loss=1.3925871849060059 Batch_id=390 Accuracy=76.57: 100%|██████████| 391/391 [00:18<00:00, 21.58it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5961, Accuracy: 7977/10000 (79.77%)

EPOCH: 7

Loss=1.3910529613494873 Batch_id=390 Accuracy=79.19: 100%|██████████| 391/391 [00:18<00:00, 21.69it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5908, Accuracy: 7952/10000 (79.52%)

EPOCH: 8

Loss=1.0594148635864258 Batch_id=390 Accuracy=79.87: 100%|██████████| 391/391 [00:18<00:00, 22.81it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5776, Accuracy: 8019/10000 (80.19%)

EPOCH: 9

Loss=1.126666784286499 Batch_id=390 Accuracy=80.05: 100%|██████████| 391/391 [00:17<00:00, 22.84it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5826, Accuracy: 8040/10000 (80.40%)

EPOCH: 10

Loss=1.117760181427002 Batch_id=390 Accuracy=80.21: 100%|██████████| 391/391 [00:18<00:00, 22.94it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5775, Accuracy: 8034/10000 (80.34%)

EPOCH: 11

Loss=1.2313487529754639 Batch_id=390 Accuracy=80.50: 100%|██████████| 391/391 [00:18<00:00, 21.44it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.5668, Accuracy: 8056/10000 (80.56%)

EPOCH: 12

Loss=0.9950528740882874 Batch_id=390 Accuracy=84.18: 100%|██████████| 391/391 [00:18<00:00, 21.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4833, Accuracy: 8339/10000 (83.39%)

EPOCH: 13

Loss=1.106369972229004 Batch_id=390 Accuracy=85.42: 100%|██████████| 391/391 [00:18<00:00, 22.19it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4761, Accuracy: 8386/10000 (83.86%)

EPOCH: 14

Loss=1.1093295812606812 Batch_id=390 Accuracy=85.63: 100%|██████████| 391/391 [00:18<00:00, 21.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4708, Accuracy: 8391/10000 (83.91%)

EPOCH: 15

Loss=0.8309308886528015 Batch_id=390 Accuracy=86.19: 100%|██████████| 391/391 [00:18<00:00, 22.70it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4683, Accuracy: 8409/10000 (84.09%)

EPOCH: 16

Loss=0.9945316910743713 Batch_id=390 Accuracy=86.23: 100%|██████████| 391/391 [00:18<00:00, 22.41it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4734, Accuracy: 8411/10000 (84.11%)

EPOCH: 17

Loss=0.8507850170135498 Batch_id=390 Accuracy=86.59: 100%|██████████| 391/391 [00:18<00:00, 22.07it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4701, Accuracy: 8408/10000 (84.08%)

EPOCH: 18

Loss=0.9178498387336731 Batch_id=390 Accuracy=87.40: 100%|██████████| 391/391 [00:18<00:00, 21.59it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4645, Accuracy: 8445/10000 (84.45%)

EPOCH: 19

Loss=1.0169169902801514 Batch_id=390 Accuracy=87.34: 100%|██████████| 391/391 [00:18<00:00, 21.13it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4627, Accuracy: 8446/10000 (84.46%)

EPOCH: 20

Loss=0.8140555620193481 Batch_id=390 Accuracy=87.45: 100%|██████████| 391/391 [00:18<00:00, 22.36it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4626, Accuracy: 8447/10000 (84.47%)

EPOCH: 21

Loss=0.9583560228347778 Batch_id=390 Accuracy=87.46: 100%|██████████| 391/391 [00:18<00:00, 21.91it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4633, Accuracy: 8445/10000 (84.45%)

EPOCH: 22

Loss=0.967059850692749 Batch_id=390 Accuracy=87.41: 100%|██████████| 391/391 [00:18<00:00, 21.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4629, Accuracy: 8453/10000 (84.53%)

EPOCH: 23

Loss=1.009822964668274 Batch_id=390 Accuracy=87.65: 100%|██████████| 391/391 [00:18<00:00, 21.20it/s]
  0%|          | 0/391 [00:00<?, ?it/s]


Test set: Average loss: 0.4617, Accuracy: 8446/10000 (84.46%)

EPOCH: 24

Loss=0.896560549736023 Batch_id=390 Accuracy=87.81: 100%|██████████| 391/391 [00:18<00:00, 21.01it/s]


Test set: Average loss: 0.4606, Accuracy: 8447/10000 (84.47%)


