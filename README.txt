1. Otevreni algoritmu ZDO2014juna_rak_hejdova_hog ve vhodnem programu (Spyder, Python(x, y)).
2. Otevreni algoritmu rozpoznej_znacku ve stejnem programu jako ZDO2014juna_rak_hejdova_hog.
3. V algoritmu rozpoznej_znacku nastaveni cesty v img = skimage.io.imread('cesta_ke_zjistovane_znacce')
k pozadovane znacce,kterou chceme zjistit.
4. Spustit algoritmus rozpoznej_znacku.
5. Probehne algoritmus rozpoznej_znacku s navaznosti na algoritmus ZDO2014juna_rak_hejdova_hog a bude vyhodocena 
vstupni znacka. To vse za predpokladu, ze existuje soubor ZDO2014sample_solution.pkl a je ulozeny ve stejnem 
adresari jako oba algoritmy.
6. Pokud neexistuje soubor ZDO2014sample_solution.pkl, je nutne ho vytvorit. K vytvoreni dojde samotnym spustenim
algoritmu ZDO2014juna_rak_hejdova_hog. Je vsak potreba zajistit trenovaci data a cestu k nim zadat v posledni casti
algoritmu: zn.train(datadir='cesta_k_trenovacim_datum')
