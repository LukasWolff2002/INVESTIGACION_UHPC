#para entrenar a la IA antes haciamos el reescalado o normalizacion de los pixeles
#pero tambien podemos rotar la imagen entre otras

train_datagen = ImageDataGenerator(
    rescale = 1./255,
    rotacion_range = 40,
    width_shift_range = 0.2,#shifting mueve la imagen para que no este siempre centrada
    height_shift_range = 0.2,
    shear_range = 0.2,#se modifica la perspectiva
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = 'nearest' #rellena los pixeles
) 

#link a colab:
#https://colab.research.google.com/github/tinyMLx/colabs/blob/master/2-4-6-HorseOrHumanWithAugmentation.ipynb