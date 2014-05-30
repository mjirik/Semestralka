# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import skimage
import skimage.feature
dir(skimage.feature)
#import skimage.feature.hog

from skimage.feature import hog


import skimage.data
import skimage.color
import skimage.exposure
import skimage.transform
import glob
import os
import numpy as np
#import urllib
import pickle
import sklearn
import sklearn.naive_bayes
import time

#Nastaveni logovani
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Znacky:
    """
    M. Jiřík
    I. Pirner
    P. Zimmermann
    Takto bude vytvořeno vaše řešení. Musí obsahovat funkci
    'rozpoznejZnacku()', která má jeden vstupní parametr. Tím je obraz. Doba
    trváná funkce je omezena na 1 sekundu. Tato funkce rovněž musí obsahovat
    ukázkový režim. V něm je pomocí obrázků vysvětleno, jak celá věc pracuje.
    #"""
    def __init__(self):
        # Toto mi umožňuje zapínat a vypínat různé části příznakového vektoru
        self.grayLevelFeatures = False
        self.colorFeatures = False  # rozpoznávání podle barvy
        self.hogFeatures = True # rozpoznávání podle hog
        self.labels = None

        # Načítání natrénovaných parametrů klasifikátoru ze souboru atd.
        path_to_script = os.path.dirname(os.path.abspath(__file__))
        classifier_path = os.path.join(path_to_script,
                                       "ZDO2014sample_solution.pkl")
        try:
            saved = pickle.load(open(classifier_path,  "rb"))
            self.clf = saved[0]
            self.labels = saved[1]
            # Ukazka logovani
            logger.debug("Ukazka loggovani, nacteni klasifikatoru ok")
        except:
            logger.error("Problems with file " + "ZDO2014sample_solution.pkl")
        pass

    def one_file_features(self, im, demo=False):
        """
        Zde je kontruován vektor příznaků pro klasfikátor
        """

        fd = np.array([])

        img = skimage.color.rgb2gray(im)

        # graylevel
         # HoG algorithm
        if self.hogFeatures:
            height, width = img.shape
            size = height*width
            pomer = height/width

            if size>4100:
                if pomer<0.6 or pomer<1.4:
                    # ctvercovy obrazek
                    imr = skimage.transform.resize(img, [64, 64])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(8,8),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 64x64 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()
                elif pomer<0.6:
                    # siroky obrazek
                    imr = skimage.transform.resize(img, [32, 64])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(8,4),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 32x64 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()
                else:
                     # vysoky obrazek
                    imr = skimage.transform.resize(img, [64, 32])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(4,8),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 64x32 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()
            else:
                if pomer<0.6 or pomer<1.4:
                    # ctvercovy obrazek
                    imr = skimage.transform.resize(img, [32, 32])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(4,4),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 32x32 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()
                elif pomer<0.6:
                    # siroky obrazek
                    imr = skimage.transform.resize(img, [16, 32])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(4,2),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 16x32 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()
                else:
                     # vysoky obrazek
                    imr = skimage.transform.resize(img, [32, 16])
                    fd, hog_image = hog(imr, orientations=9, pixels_per_cell=(2,4),
                        cells_per_block=(3,3), visualise=True, normalise=False)
                    if demo:
                        plt.imshow(imr)
                        plt.suptitle('Zmenseni obrazu na velikost 32x16 pixelu.')
                        plt.show()
                        plt.imshow(hog_image)
                        plt.suptitle('Analyza obrazu algoritmem HoG, rozdeleny na 8x8 bloku.')
                        plt.show()


        if self.grayLevelFeatures:
#            imr = skimage.transform.resize(img, [9, 9])
#            glfd = imr.reshape(-1)
#            fd = np.append(fd, glfd)
#
#            if demo:
#                plt.imshow(imr)
#                plt.show()
            pass

        #fd.append(hsvft[:])
        if self.colorFeatures:
            #fd = np.append(fd, colorft)
            pass

        #print hog_image
        return fd

    # nacitani z adresare
    def readImageDir(self, path):
        dirs = glob.glob(os.path.join(os.path.normpath(path), '*'))
        labels = []
        #nlabels = []
        files = []

        #i = 0
        for onedir in dirs:

            #print onedir
            base, lab = os.path.split(onedir)
            if os.path.isdir(onedir):
                filesInDir = glob.glob(os.path.join(onedir, '*'))
                for onefile in filesInDir:
                    labels.append(lab)
                    files.append(onefile)
                    #nlabels.append(i)

        return files, labels

    def train(self, datadir='C:/Python27/Lib/site-packages/xy/ZDO2014sample_solution-master/zdo2014-training3/zdo2014-training3/'):
        tfiles, tlabels = self.readImageDir(datadir)

        # trénování by trvalo dlouho, tak si beru jen každý druhý obrázek
#        tfiles = tfiles[::2]
#        tlabels = tlabels[::2]

        featuresAll = []
        i = 0

        for fl in tfiles:
            i = i + 1
            logger.debug(i)
            im = skimage.io.imread(fl)
            fv = self.one_file_features(im)
            featuresAll.append(fv)

        featuresAll = np.array(featuresAll)

        # Trénování klasifikátoru

        labels, inds = np.unique(tlabels, return_inverse=True)

        #from sklearn import svm
        #clf = svm.SVC()
        clf = sklearn.naive_bayes.GaussianNB()

        clf.fit(featuresAll, inds)
        self.clf = clf
        self.labels = labels

        # ulozime do souboru pomocí modulu pickle
        # https://wiki.python.org/moin/UsingPickle

        # je potřeba zachovat i původní labely
        saved = [clf, labels]
        pickle.dump(saved, open("ZDO2014sample_solution.pkl", "wb"))

    def rozpoznejZnacku(self, image, demo=False):

        # Nějaký moc chytrý kód

        class_index = self.clf.predict(self.one_file_features(image, demo))
        # tady převedeme číselnou hodnotu do textového popisku
        retval = self.labels[class_index]

        return retval[0]

    def kontrola(self, datadir=None):
        """
        Jednoduché vyhodnocení výsledků
        """

        obrazky, reseni = self.readImageDir(datadir)

        vysledky = []

        for i in range(0, len(obrazky)):
            cas1 = time.clock()
            im = skimage.io.imread(obrazky[i])
            result = self.rozpoznejZnacku(im)

            cas2 = time.clock()

            if((cas2 - cas1) >= 1.0):
                print "cas vyprsel"
                result = 0

            vysledky.append(result)

        hodnoceni = np.array(reseni) == np.array(vysledky)
        skore = np.sum(hodnoceni.astype(np.int)) / np.float(len(reseni))

        print skore

# <codecell>

# následující zápis zařídí spuštění při volání z příkazové řádky.
# Pokud bude modul jen includován, tato část se nespustí. To je požadované
# chování
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    zn = Znacky()
# Natrenujeme na cele sade
    zn.train(datadir='/home/mjirik/data/zdo2014/zdo2014-training3/')
# Otestujeme na 1. sade
    zn.kontrola('/home/mjirik/data/zdo2014/zdo2014-training1/')


# <codecell>

#print clf
