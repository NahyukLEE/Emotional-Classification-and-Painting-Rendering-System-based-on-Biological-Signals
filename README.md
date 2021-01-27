
# Emotional classification and Painting rendering system based on Biological signals

[Paper](https://drive.google.com/file/d/10U2h2FI7Werj9rdcbjAglw2g9R5F3Yvl/view?usp=sharing) | [Project](https://drive.google.com/file/d/1KKKzKKXDGYLnVxo6IKglSMEkLFIPi1No/view?usp=sharing) | [Presentation](https://drive.google.com/file/d/1vdqw6_wS0JVksHec_CEPYjCppfYjO90Z/view?usp=sharing)

**This repository contains source codes which used for "Final Project for CUAI 3rd Conference".**

**CUAI 3rd Final Conference 1st place Award 🏆 (Grand Prize)**

Paper and Presentation are in Korean.

### Our Team 
 - **Byunghyun Bae** (School of Pharmaceutics, Chung-Ang Univ.)
 - **Hearyeon Seo** (School of Mechanical Engineering, Chung-Ang Univ.)
 - **Nahyuk Lee** (School of Computer Science & Engineering, Chung-Ang Univ.)
 - **Borim Lee** (School of Computer Science & Engineering, Chung-Ang Univ.)
 - **Hayun Lee** (School of Computer Science & Engineering, Chung-Ang Univ.)
 - **Whanjin Lee** (School of Energy Systems Engineering, Chung-Ang Univ.)


## Application
### Rendering using SinGAN example
![](imgs/rendering.jpg)

## System Flow
The system flow of our project is as follows. 
![](imgs/SystemFlow.jpg)
1) Measuring brain waves data and Emotional classification with them.
2) Recommending reference paintings according to the emotional evaluation results.
3) Rendering paintings for target image using [SinGAN](https://github.com/NahyukLEE/SinGAN).

## Code

### Install dependencies
We recommend you to use Anaconda that already including mandotory packages. 
```
python -m pip install -r requirements.txt
```
Our code was tested with Python 3.6, Pytorch 1.7, CUDA 11.

### Train Emotional Classification Model
To train emotional classification models with your own brain waves dataset(*'ratio.csv'*), you can handle IPython notebook with *'model.ipynb'* . By using *dump* method in *joblib*, you can export your model as *'emotion_modle.pkl'*.

### 
