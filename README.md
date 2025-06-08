# NEURAL-STYLE-TRANSFER

*COMPANY* : CODTECH IT SOLUTION

*NAME* : ELAINE JOSE

*INTERN ID* : CT04DN1322

*DOMAIN* : ARTIFICAL INTELLIGENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

Through the usage of a TensorFlow Hub hosted pre-trained model, this project implements an arbitrary neural style transfer system. Neural style transfer is an engrossing technique in computer vision and deep learning that enables the merging of the content of one image with the style from another. This creates a brand-new image that basically preserves the original content but assumes the artistic style from the second image, exhibiting breathtaking visual effects akin to that of renowned paintings or art patterns.

Project Objective
The core idea of this project is that there will be two input images — content and style images — and output will be an image that contains content from the first but style from the other. This project relies on deep learning techniques in TensorFlow and a very capable model hosted on TensorFlow Hub, by means of which pre-trained neural nets can be integrated easily.

Key Components
Loading and preprocessing images:
The function loads the images from a given path, decodes them into tensors, and normalizes pixel values. Images are loaded on a format expected by the TensorFlow model so pixel values are scaled between 0 and 1 to avoid any confusion in model input. The function also expands image dimensions to the expected input shape of the model.

Model Loading:
The project is based on the core TensorFlow Hub model arbitrary-image-stylization-v1-256. It is pretrained for arbitrary style transfer; hence, any style can be applied to any content image without the necessity of retraining. It receives as input tensors corresponding to a content image and a style-image and outputs the stylized image.

Style Transfer Execution:
Afterward, once both images are loaded and preprocessed, the model is invoked on them. The model extracts the content features internally from the content image; it also obtains style features from the style image and blends the two, resulting in the stylized image tensor.

Post-processing and Saving the Output:
The output tensor is post-processed to change pixel values to a normal image format (uint8), and then the image format is converted from RGB to BGR so that OpenCV can save it properly. Now the stylized image is ready to be saved.

Visualization:
Matplotlib is used to present the final advantage in a new window, permitting the user to immediately perform a visual inspection of the result.

Implementation Details
Setting the environment variable TF_CPP_MIN_LOG_LEVEL to '3' suppresses TensorFlow verbose logging messages that would otherwise litter the console output.

Loading images uses TensorFlow I/O to load and decode images efficiently.

Perfect coding errors are encountered at every crucial stage (loading images, inference, saving, and displaying images) to ensure either graceful failure or proper informative error messages.

Applications and Use Cases
Neural style transfer finds its applications in:

Artistic content creation: Converting photographs into paintings of famous painters like Van Gogh or Picasso.

Graphic design and advertising: Quick producing of stylized images for creative campaigns.

Entertainment and media: Creating novel VFXs for games, movies, or environments.

Education and research: Investigating deep learning feature representations or artistic styles.

Challenges and Considerations
The quality of the stylized image greatly depends on the style and content images one chooses. 

Also, training or processing can be computationally heavy; hence, one would ideally need a GPU for anything practically useful. 

Preserving content structure while the highly intricate styles are being applied is yet another challenge; research in this area is still ongoing.

Conclusion
This work serves to demonstrate the possibility of performing creativity with the pre-trained deep networks like neural style transfer. From the perspective of a layman, TensorFlow Hub hides all the low-level stuff concerning neural network deployment so that artistic images can be created in just a few lines of code. Being modular, it is easy to extend for batch processing or as a useful building block for bigger multimedia applications.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/df5a2808-7044-45c9-8767-36b2e45e2da0)
