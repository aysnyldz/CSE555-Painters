from model import aysennet_model
from data_loader import load_train_batch_data

awesome_model = aysennet_model()
awesome_model.summary()

awesome_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',metrics=['accuracy'])


#print(x_train.shape)
#print(y_train.shape)


for x in range(0, 100):
    x_train, y_train = load_train_batch_data(x)
    awesome_model.fit(x=x_train, y=y_train, batch_size=100, epochs=10, verbose=1, shuffle=True)

    awesome_model.train_on_batch()


print("hello")