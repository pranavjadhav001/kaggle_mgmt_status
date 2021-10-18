# kaggle_mgmt_status
Attempt at [Kaggle mgmt](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification competition) with [Raghav](https://github.com/PhenomenalOnee)
Even though there is no evidence that there is any correlation between mri brain scans and presence/absence of mgmt status  
It was a good learning experience  

## Methods
1. Conv3Dnet
   * Since mgmt status can be determined in scans with tumor.we first filter out data with only tumor
   * We trained a simple cnn model for tumor classification, this reduces the depth and allows the model to focus on important slices
   * trained a resnet18_3d/efficientnet_3d/vanilla_3d with variable depth 
   * Model overfitting with 100% acc on train dataset,performing poorly on validation dataset
2. Pretrained Conv2d + transformer
   * Features and deep layer embeddings of a image stacked with all slices fed into a time series model like transformer
   * Batch_size,height,width,depth,channels-> Conv2d -> Batch_size,depth,features -> transformer -> classification
   * Not enough information in feature space
3. voxel + Conv3dnet
   * Bring all patients scan into 1 modality using voxel orientation code
   * Use the same pipeline as 1
  
