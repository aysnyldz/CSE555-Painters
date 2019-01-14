import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, BatchNormalization, MaxPooling2D, Conv2D, ZeroPadding2D, Flatten, Dense, \
    Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam



def aysennet_model(img_shape=(300, 300, 3), n_classes=12, l2_reg=0.01):
    # Initialize model
    aysennet = Sequential()

    # Layer 1
    aysennet.add(Conv2D(128, (3, 3), input_shape=img_shape,
                        padding='same', kernel_regularizer=l2(l2_reg)))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))



    # Layer 2
    aysennet.add(Conv2D(256, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 4
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(256, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))


    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))


    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 5
    aysennet.add(ZeroPadding2D((1, 1)))
    aysennet.add(Conv2D(128, (3, 3), padding='same'))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 6
    aysennet.add(Flatten())
    aysennet.add(Dense(1024))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(Dropout(0.5))



    """ # Layer 7
    aysennet.add(Dense(4096))
    #aysennet.add(BatchNormalization())
    aysennet.add(Activation('relu'))
    aysennet.add(Dropout(0.5))"""
    # Layer 8

    aysennet.add(Dense(n_classes))
    aysennet.add(BatchNormalization())
    aysennet.add(Activation('softmax'))

    return aysennet

#model = aysennet_model(img_shape=(3,300,300),n_classes=12, l2_reg=0.01)
model = aysennet_model()
#metrics_x=['accuracy']
#adam = Adam(lr=0.000074)

#model.compile(loss='categorical_crossentropy', optimizer=adam,metrics=metrics_x)
model.summary()
