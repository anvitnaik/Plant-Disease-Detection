n_of_image,label_name = 650,['Apple scab', 'Apple Black rot', 'Apple Cedar apple rust', 'Apple healthy', 'Cherry Powdery mildew',
         'Cherry healthy','Corn Cercospora leaf spot Gray leaf spot', 'Corn Common rust', 'Corn Northern Leaf Blight','Corn healthy', 
         'Grape Black rot', 'Grape Esca', 'Grape Leaf blight', 'Grape healthy','Peach Bacterial spot','Peach healthy', 'Pepper bell Bacterial spot', 
         'Pepper bell healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy', 'Strawberry Leaf scorch', 'Strawberry healthy',
         'Tomato Bacterial spot', 'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot',
         'Tomato Spider mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus', 'Tomato healthy']
                              
img,label,img_size = [],[],(150,150)

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Apple___Apple_scab'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(0) # Apple___Apple_scab

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Apple___Black_rot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(1) # Apple___Black_rot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Apple___Cedar_apple_rust'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(2) # Apple___Cedar_apple_rust

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Apple___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(3) # Apple___healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Cherry_(including_sour)_Powdery_mildew'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(4) # Cherry_(including_sour)_Powdery_mildew

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Cherry_(including_sour)_healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(5) #Cherry_(including_sour)_healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(6) # Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Corn_(maize)Common_rust'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(7) # Corn_(maize)Common_rust

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Corn_(maize)_Northern_Leaf_Blight'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(8) # Corn_(maize)_Northern_Leaf_Blight

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Corn_(maize)_healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(9) # Corn_(maize)_healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Grape___Black_rot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(10) # Grape___Black_rot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Grape__Esca(Black_Measles)'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(11) # Grape__Esca(Black_Measles)

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Grape__Leaf_blight(Isariopsis_Leaf_Spot)'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(12) # Grape__Leaf_blight(Isariopsis_Leaf_Spot)

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Grape___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(13) # Grape___healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Peach___Bacterial_spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(14) # Peach___Bacterial_spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Peach___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(15) # Peach___healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Pepper,bell__Bacterial_spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(16) # Pepper,bell__Bacterial_spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Pepper,bell__healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(17) # Pepper,bell__healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Potato___Early_blight'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(18) # Potato___Early_blight

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Potato___Late_blight'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(19) # Potato___Late_blight

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Potato___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(20) # Potato___healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Strawberry___Leaf_scorch'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(21) # Strawberry___Leaf_scorch

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Strawberry___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(22) # Strawberry___healthy

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Bacterial_spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(23) # Tomato___Bacterial_spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Early_blight'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(24) # Tomato___Early_blight

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Late_blight'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(25) # Tomato___Late_blight

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Leaf_Mold'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(26) # Tomato___Leaf_Mold

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Septoria_leaf_spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(27) # Tomato___Septoria_leaf_spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Spider_mites Two-spotted_spider_mite'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(28) # Tomato___Spider_mites Two-spotted_spider_mite

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Target_Spot'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(29) # Tomato___Target_Spot

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Tomato_Yellow_Leaf_Curl_Virus'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(30) # Tomato___Tomato_Yellow_Leaf_Curl_Virus

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___Tomato_mosaic_virus'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(31) # Tomato___Tomato_mosaic_virus

path_dir = '/content/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train/Tomato___healthy'
os.chdir(path_dir)
img_path_list = os.listdir(path_dir)
for len_no,img_path in enumerate(img_path_list):
  if len_no == n_of_image:break
  else:
    img.append(img_to_array(load_img(img_path,target_size=img_size))/255)
    label.append(32) # Tomato___healthy

img,label = np.array(img),np.array(label)
