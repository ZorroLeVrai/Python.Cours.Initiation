liste_vide = []
ma_liste = [2,1,3]
print(ma_liste)   #[2, 1, 3]
ma_liste.sort()
print(ma_liste)   #[1, 2, 3]
ma_liste.append(4)
print(ma_liste)   #[1, 2, 3, 4]
ma_liste.extend([5,6])
print(ma_liste)   #[1, 2, 3, 4, 5, 6]
ma_liste.remove(4)
print(ma_liste)   #[1, 2, 3, 5, 6]
ma_liste.pop()
print(ma_liste)   #[1, 2, 3, 5]