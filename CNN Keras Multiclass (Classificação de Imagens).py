# Livro Ciência de Dados e Aprendizado de Máquina - https://www.amazon.com.br/dp/B07X1TVLKW
# Livro Inteligência Artificial com Python - Redes Neurais Intuitivas - https://www.amazon.com.br/dp/B087YSVVXW
# Livro Redes Neurais Artificiais - https://www.amazon.com.br/dp/B0881ZYYCJ

from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras import backend as B
import numpy as np

data_treino = 'C:/Users/Fernando/Desktop/CNNMINISET/dataset/train/'
data_teste = 'C:/Users/Fernando/Desktop/CNNMINISET/dataset/test/'

if B.image_data_format() == 'channels_first':
    input_shape = (3, 300, 300)
else:
    input_shape = (300, 300, 3)

data_gen_treino = ImageDataGenerator(rescale= 1. / 255,
                                     shear_range=0.2,
                                     zoom_range=0.2,
                                     horizontal_flip=True)
data_gen_teste = ImageDataGenerator(rescale=1. / 255)

gerador_treino = data_gen_treino.flow_from_directory(data_treino,
                                                     target_size=(300, 300),
                                                     batch_size=20,
                                                     class_mode='categorical')

gerador_teste = data_gen_teste.flow_from_directory(data_teste,
                                                     target_size=(300, 300),
                                                     batch_size=20,
                                                     class_mode='categorical')

model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(4))
model.add(Activation('softmax'))
model.summary()
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'rmsprop',
              metrics = ['accuracy'])
model.fit_generator(gerador_treino,
                    steps_per_epoch=100,
                    epochs=20,
                    validation_data=gerador_teste,
                    validation_steps=50)

img_teste = image.load_img('C:/Users/Fernando/Desktop/CNNMINISET/dataset/amostra_teste/normal.jpeg',
                           target_size = (300, 300))
img_teste = image.img_to_array(img_teste)
img_teste = np.expand_dims(img_teste,
                           axis = 0)

model = Sequential()
model = load_model('model.h5')

img_teste = image.load_img('C:/Users/Fernando/Desktop/CNNMINISET/dataset/amostra_teste/pneumonia.jpeg',
                           target_size = (300, 300))
img_teste = image.img_to_array(img_teste)
img_teste = np.expand_dims(img_teste,
                           axis = 0)

resultado_teste = model.predict(img_teste)
resultado_final = resultado_teste

if resultado_final[0,0].any() > 0.5:
    print('Esta radiografia apresenta as estruturas do Tórax sem alterações significativas..')
elif resultado_final[0,1].any() > 0.5:
    print('Esta radiografia apresenta características compatíveis com PNEUMONIA')
elif resultado_final[0,2].any() > 0.5:
    print('Esta radiografia apresenta características compatíveis com DERRAME PLEURAL')
elif resultado_final[0,3].any() > 0.5:
    print('Esta radiografia apresenta características compatíveis com TUBERCULOSE')
else:
    print('A imagem fornecida não cumpre os requisitos mínimos para ser processada,')
    print('ou o resultado do processamento da mesma é inconclusivo.')

# Livro Python do ZERO à Programação Orientada a Objetos - https://www.amazon.com.br/dp/B07P2VJVW5
# Livro Programação Orientada a Objetos com Python - https://www.amazon.com.br/dp/B083ZYRY9C
# Livro Tópicos Avançados em Python - https://www.amazon.com.br/dp/B08FBKBC9H
# Livro Ciência de Dados e Aprendizado de Máquina - https://www.amazon.com.br/dp/B07X1TVLKW
# Livro Inteligência Artificial com Python - Redes Neurais Intuitivas - https://www.amazon.com.br/dp/B087YSVVXW
# Livro Redes Neurais Artificiais - https://www.amazon.com.br/dp/B0881ZYYCJ
# Livro Análise Financeira com Python - https://www.amazon.com.br/dp/B08B6ZX6BB
# Livro Arrays com Python + Numpy - https://www.amazon.com.br/dp/B08BTN6V7Y
