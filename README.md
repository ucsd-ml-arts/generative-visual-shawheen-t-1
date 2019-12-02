# Project 3 Generative Visual

Shawheen Tosifian, stosifia@ucsd.edu


## Abstract

The goal of this project was to create a DcGAN that would generate album artwork of from a respective decade (from the 50s to 00s). The choice of albums was inspired from the reference '1001 Albums to Listen to Before You Die. The album name were then roughly separated by decade and feed into an album cover scraping script included called get_albums.py which would grab the album cover of the desired resolution (ended up using 64x64) from the iTunes API. This collection albums was then used to train the Deep Convolutional GAN (DCGAN) to produce 'fake' album covers. Initially, the model was trained on individual decades but the results were beyond subpar so I then decided to train it on all the album covers at once, which still resulted in useless outputs. My guess is that due to low quantity of data, the network wasn't able to learn properly. The creative goal behind this project was to see if the network could pick up on certain color schemes and patterns present in album covers of each decade and stylistically recreate them.



## Model/Data

- All the training data used in this project is in the 64x64 folder, sorted by decade (Xs), with image at 64x64. Folders containing (XXs) have higher resolution images (500x500) which were not used.


## Code

Your code for generating your project:
- Python: get_albums.py <- for scraping covers
- Jupyter notebooks: DCGAN_AlbumArt.ipynb

## Results

Documentation of your results in an appropriate format, both links to files and a brief description of their contents:
- image files (`.jpg`, `.png` or whatever else is appropriate)
- move files (uploaded to youtube or vimeo due to github file size limits)
- ... some other form

## Technical Notes

Install (pip) CoverPy to scrape album covers from iTunes

