def pred_image(model,image,class_name=class_name):

 """
 helper function for Returning predicted class with image to be predicted (multiclass classification)
 """
 img = load_prep_img(image)

# Make a prediction
 pred = model.predict(tf.expand_dims(img, axis=0))

# Match the prediction class to the highest prediction probability
 pred_class = class_name[pred.argmax()]
 plt.imshow(img)
 plt.title(pred_class)
 plt.axis(False);