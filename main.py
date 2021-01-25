from recommended import ratio
import joblib
import os

loaded_model = joblib.load('./emotion_model.pkl')

data = [0.096494,0.106731,0.089205,0.129719,0.165946,0.198439,0.107642,0.105825]

happy = loaded_model.predict_proba([data])[0][0]
sad = loaded_model.predict_proba([data])[0][1]

print(ratio(happy,sad))

input_img = ratio(happy,sad)
ref_img = 'paint02.jpg'

os.chdir('./SinGAN')
os.system('python paint2image.py --input_name %s --ref_name %s --paint_start_scale 6' %(input_img, ref_img))

