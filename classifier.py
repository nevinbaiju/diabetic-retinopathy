
# coding: utf-8

# In[1]:

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator


# In[16]:


def prediction():
    
    """
    Function to predict if the retina image has diabetic retinopathy or not.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    y_pred: bool
            Whether or not the retina has diabetic retinopathy.
    percent_chance: float
            Percentage of chance the retina image has diabetic retinopathy.
    """
    
    
    mod=load_model('model.hd5')
    
    test_gen = ImageDataGenerator(rescale = 1./255)

    import os
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    CAPTHA_ROOT = os.path.join(PROJECT_PATH,'test_images')
    
    test_data = test_gen.flow_from_directory(CAPTHA_ROOT,
                                              target_size = (64, 64),
                                              batch_size = 32,
                                              class_mode = 'binary', shuffle=False)
    
    predicted = mod.predict_generator(test_data)
    
    y_pred = predicted[0][0] > 0.4
    percent_chance = round(predicted[0][0]*100, 2)
    
    return y_pred, percent_chance
# In[17]:

if __name__ == '__main__':
    print(prediction())


