# Swin Transformer Reproducibility

We used the official code (https://github.com/microsoft/Swin-Transformer) of the "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows", to reproduce the image classification of the three variants in the original paper and added hyperparameter comparison experiments, ablation experiments, and self-attention module improvement experiments.

Among them, the hyperparameter comparison experiment includes learning rate comparison, batch size comparison and num_heads comparison, mainly to modify the config.py provided by the original author. The codes are contained in "hyperparameter comparison" folder. Replace the original "config.py" in the authors' code with the files in the "hyperparameter comparison" folder to test the performance of the network with different hyperparameters. The other setups are the same as the official implementation of the Swin Transformer. 

For the ablation experiments, we remove the position embedding module, shifted window module, residual architecture, and dropout module, to testify the importance of each component. 
Replace the original "config.py" in the authors' code with "nodropout.py" in the "Ablation" folder to test the performance of the network without dropout layers. 
Replace the original "swin_transformer.py" in the authors' code with the other files in the "Ablation" folders to perform the ablation experiments.

For the improvement of the self-attention module, we reproduce three self-attention variants (Non-Local, A-SCN, Offset-Attention), which are different from the self-attention module used in the original Swin Transformer. The changed codes can be found in "self-attention variants" folder. Replace the original "swin_transformer.py" in the authors' code with the files in the "self-attention variants" folders to perform the improvement experiments.






# Citing Swin Transformer

@article{liu2021Swin,

  title={Swin Transformer: Hierarchical Vision Transformer using Shifted Windows},
  
  author={Liu, Ze and Lin, Yutong and Cao, Yue and Hu, Han and Wei, Yixuan and Zhang, Zheng and Lin, Stephen and Guo, Baining},
  
  journal={International Conference on Computer Vision (ICCV)},
  
  year={2021}
  
}
