# CIFAR10 Sandbox

## Mixup 
### 200 epochs  (Learning rate divided by 10 at epoch 100 and 150)

|Method|Acc/Error (%)|Config|Notes|
|:----:|:-----:|:-----:|:---:|
|Baseline|94.86/5.14|baseline.yaml||
|Mixup|96.01/3.99|mixup/200/mixup.yaml|&alpha;=1|
|Manifold Mixup|96.10/3.90|mixup/200/manifold\_mixup01.yaml|&alpha;=2 <br> layers=[0,1]|
|Manifold Mixup|96.01/3.99|mixup/200/manifold\_mixup012.yaml|&alpha;=2 <br> layers=[0,1,2]|
|Cutmix|96.20/3.80|mixup/200/cutmix.yaml|&alpha;=1|
|Manifold Cutmix|-|mixup/200/manifold\_cutmix.yaml|&alpha;=1 <br> layers=[0,1,2]|

### 1200 epochs  (Learning rate divided by 10 at epoch 400 and 800)

|Method|Acc/Error (%)|Config|Notes|
|:----:|:-----:|:-----:|:---:|
|Baseline|95.59/4.41|baseline\_1200.yaml||
|Mixup|96.85/3.15|mixup/1200/mixup.yaml|&alpha;=1|
|Manifold Mixup|97.19/2.81|mixup/1200/manifold\_mixup.yaml|&alpha;=2 <br> layers=[0,1,2]|

## Training with GAN Data
- Images generated from conditional BigGAN.

### 200 epochs  (Learning rate divided by 10 at epoch 100 and 150)

|\% Generated Data|Acc/Error (%)|Config|
|:----:|:-----:|:-----:|
|100\%|66.23/33.77|gan/gan\_100.yaml|
|50\%|92.34/7.66|gan/gan\_50.yaml|
|25\%|93.67/6.33|gan/gan\_25.yaml|
|10\%|94.33/5.67|gan/gan\_10.yaml|
|0\%|94.86/5.14|baseline.yaml||

## Augmentations
- Random horizonal flip, translation and
  normalization is applied first 
  in all models. Cutout is applied after AutoAugment/RandAugment when used
  together.
### 200 epochs  (Learning rate divided by 10 at epoch 100 and 150)

|Method|Acc/Error (%)|Config|Notes|
|:----:|:-----:|:-----:|:---:|
|Baseline|94.86/5.14|baseline.yaml||
|Cutout|95.88/4.12|augment/cutout.yaml|cutout=16x16|
|AutoAugment|95.90/4.10|augment/autoaugment.yaml||
|AutoAugment + Cutout|96.31/3.69|augment/autoaugment\_cutout.yaml|cutout=16x16|
|RandAugment|95.02/4.98|augment/randaugment\_n3m5.yaml|n=3 <br> m=5|
|RandAugment|94.93/5.07|augment/randaugment\_n3m4.yaml|n=3 <br> m=4|
|RandAugment|94.37/5.63|augment/randaugment\_n3m2.yaml|n=3 <br> m=2|
|RandAugment|95.65/4.35|augment/randaugment\_n2m5.yaml|n=2 <br> m=5|
|RandAugment|95.50/4.50|augment/randaugment\_n2m6.yaml|n=2 <br> m=6|
|RandAugment + Cutout|95.64/4.36|augment/randaugment\_cutout.yaml|n=2 <br> m=5 <br> cutout=16x16|

### 1200 epochs  (Learning rate divide by 10 at epoch 400 and 800)   

|Method|Acc/Error (%)|Config|Notes|
|:----:|:-----:|:-----:|:---:|
|Baseline|95.59/4.41|baseline\_1200.yaml||
|AutoAugment + Cutout|-|augment/autoaugment\_cutout.yaml|cutout=16x16|
|RandAugment + Cutout|-|augment/randaugment\_cutout.yaml|n=2 <br> m=5|


- AutoAugment shows better results on CIFAR compared to RandAugment which appears to make the
  augmentations too strong for the size of the model without proper hyperparameter tuning.
  The hyperparameters however offer better flexiblity which should benefit a wider variety
  of datasets compared to AutoAugment which is tuned specifically on a target dataset.


## To Do
- Label smoothing
- DropBlock
- DropBlock/Cutmix fusion
- CIFAR100
- Other models
- Architecture modifications  (Shake-Shake, ShakeDrop, etc)
