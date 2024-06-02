import struct
import time

def getSample(path):
    """
    EXERCICE 1
    Cette fonction retourne les deux voies du fichier dans les
    listes A1 et A2
    """
    with open(path,"rb") as f:
        data = f.read()
        A1 = []
        A2 = []
        i = 44
        while i < len(data):
            x1,x2 = struct.unpack_from("h h",data,i)
            A1.append(x1)
            A2.append(x2)
            i += 4
    return A1,A2

def getHeader(path):
    """
    Cette fonction renvoie le header du fichier
    """
    with open(path, "rb") as f:
        header = f.read(44)
    return header

def makeSample():
    """
    EXERCICE 2
    Cette fonction recrée le fichier son à partir des deux 
    voies.
    """
    header = getHeader("the_wall.wav")
    A1, A2 = getSample("the_wall.wav")
    with open("myfile.wav","wb") as f:
        f.write(header)
        for i in range(len(A1)):
            s = struct.pack("hh",A1[i],A2[i])
            f.write(s)

def reduceFile():
    """
    EXERCICE 3
    Cette fonction recrée le signal à partir des deux voies, en
    enlevant un echantillon sur deux. Ceci conduit à la réduction par
    deux de la durée du fichier
    """
    A1, A2 = getSample("the_wall.wav")

    header = getHeader("the_wall.wav")[:40]
    header += struct.pack("I",len(A1)//2*4)
    header = header[:4] + struct.pack("I",len(A1)//2*4+44) + header[8:]
    with open("myfile2.wav","wb") as f:
        f.write(header)
        for i in range(0,len(A1),2):
            s = struct.pack("hh",A1[i],A2[i])
            f.write(s)


def reduceFile2():
    """
    EXERCICE 3 - autre version
    Cette fonction recrée le signal à partir des deux voies, en
    enlevant un echantillon sur deux. NEANMOINS, ELLE MODIFIE LE HEADER
    AFIN QUE LE FICHIER SOIT LU AVEC LA MEME DUREE, CE QUI ALTERE
    GRANDEMENT LA QUALITE DU SON
    """
    A1, A2 = getSample("the_wall.wav")
    header = getHeader("the_wall.wav")[:40]
    header += struct.pack("I",len(A1)//2*4)
    header = header[:4] + struct.pack("I",len(A1)//2*4+44) + header[8:]
    sample_rate = struct.unpack("I",header[24:28])[0]
    header = header[:24] + struct.pack("I",sample_rate//2) + header[28:]
    mult = struct.unpack("I",header[28:32])[0]
    header = header[:28] + struct.pack("I",int(mult/2)) + header[32:]
    with open("myfile3.wav","wb") as f:
        f.write(header)
        for i in range(0,len(A1),2):
            s = struct.pack("hh",A1[i],A2[i])
            f.write(s)

def interpolate():
    """
    EXERCICE 4
    Cette fonction recrée le signal à partir des deux voies, en
    interpolant le signal pour multiplier le nombre de valeurs par deux.
    Ceci conduit à la l'augmentation par deux de la durée du fichier
    """
    A3, A4 = getSample("the_wall.wav")
    A1 = []
    A2 = []
    for i in range(0,len(A3)-1):
        A1.append(A3[i])
        A2.append(A4[i])
        A1.append((A3[i]+A3[i+1])/2)
        A2.append((A4[i]+A4[i+1])/2)
    A1.append(A3[-1])
    A2.append(A4[-1])

    header = getHeader("the_wall.wav")[:40]
    header += struct.pack("I",(len(A1)*2-1)*4)
    header = header[:4] + struct.pack("I",(len(A1)*2-1)*2*4+44) + header[8:]

    with open("myfile4.wav","wb") as f:
        f.write(header)
        for i in range(len(A1)):
            s = struct.pack("hh",int(A1[i]),int(A2[i]))
            f.write(s)


def interpolate2():
    """
    EXERCICE 4 - autre version
    Cette fonction recrée le signal à partir des deux voies, en
    interpolant le signal pour multiplier le nombre de valeurs par deux.
    NEANMOINS, ELLE MODIFIE LE HEADER AFIN QUE LE FICHIER SOIT LU AVEC
    LA MEME DUREE, CE QUI (EN THEORIE) AMELIORE LA QUALITE DU SON.
    """
    A3, A4 = getSample("the_wall.wav")
    A1 = []
    A2 = []
    for i in range(0,len(A3)-1):
        A1.append(A3[i])
        A2.append(A4[i])
        A1.append((A3[i]+A3[i+1])/2)
        A2.append((A4[i]+A4[i+1])/2)
    A1.append(A3[-1])
    A2.append(A4[-1])
    
    header = getHeader("the_wall.wav")[:40]
    header += struct.pack("I",(len(A1)*2-1)*4)
    header = header[:4] + struct.pack("I",(len(A1)*2-1)*2*4+44) + header[8:]

    sample_rate = struct.unpack("I",header[24:28])[0]
    header = header[:24] + struct.pack("I",sample_rate*2) + header[28:]
    mult = struct.unpack("I",header[28:32])[0]
    header = header[:28] + struct.pack("I",int(mult*2)) + header[32:]

    with open("myfile5.wav","wb") as f:
        f.write(header)
        for i in range(len(A1)):
            s = struct.pack("hh",int(A1[i]),int(A2[i]))
            f.write(s)


def cadence(x):
    """
    EXERCICE 5
    Cette fonction multiplie la durée d'un son par un facteur f,
    tout en gardant le meme nombre de valeurs par voies.
    """
    with open("the_wall.wav","rb") as f:
        data = f.read()
    
    sample_rate = struct.unpack("I",data[24:28])[0]
    mult = struct.unpack("I",data[28:32])[0]
    data = data[:24] + struct.pack("I",int(sample_rate*x)) + struct.pack("I",int(mult*x)) + data[32:]
    
    with open("myfile6.wav","wb") as f:
        f.write(data)

def echo(delay,decay,k):
    # Exercice 6
    """
    delay est le temps entre un son et sa réplique, decay, le facteur
    multiplicatif de son intensité, et k le nombre de répliques d'un son
    """
    assert type(k) == int
    N = 0
    for i in range(0,k+1):
        N += pow(decay,i)
    A1, A2 = getSample("the_wall.wav")
    header = getHeader("the_wall.wav")
    sample_rate = struct.unpack("I",header[24:28])[0]
    duration = len(A1)/sample_rate # en secondes

    def phi(t,L):
        n = int(t*sample_rate)
        try:
            return (L[n+1]-L[n])*(sample_rate*t-n)+L[n]
        except:
            return L[-1]
    
    M = len(A1)
    last = time.time()
    q = 0
    for i in range(len(A1)):
        if q < k:
            q = int(i // (sample_rate*delay))
        X = 0
        Y = 0
        for j in range(q+1):
            X += phi(i/sample_rate-delay*j,A1)*pow(decay,j)
            Y += phi(i/sample_rate-delay*j,A2)*pow(decay,j)
        X = round(X/N)
        Y = round(Y/N)
        A1[i] = X
        A2[i] = Y
        if time.time() - last > 10:
            print("\n\n")
            print(f"Iterations : {i}/{M}")
            r = i/M
            print(f"{round(r*100)}% done\n")
            s = "["+"#"*round(r*20)
            s += "-"*(20-len(s)+1)+"]"
            print(s)
            print("\n")
            last = time.time()
        

    with open("myfile7.wav","wb") as f:
        f.write(header)
        for i in range(len(A1)):
            s = struct.pack("hh",A1[i],A2[i])
            f.write(s)


"""
ATTENTION : executer ces fonctions conduit a la creation de fichiers
(assez lourds)
"""
# Exercice 3
#reduceFile()

# Exercice 3 - autre version
#reduceFile2()

# Exercice 4
#interpolate()

# Exercice 4 - autre version
#interpolate2()

# Exercice 5
#cadence(2)

# Exercice 6, attention, cet appel peut prendre du temps et consommer
# beaucoup de ressources, pour alléger l'appel, mettre k a 1
#echo(0.3,1,2)
            

