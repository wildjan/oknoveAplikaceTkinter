def format(t):
    """
    Vstup: t v desetinach sekundy
    Vystup: 'M:SS.D'
    """
    dec = t % 10
    sec = (t / 10) % 60
    min = t / 600
    vysledek = "{:}:{:02}.{:}".format(min, sec, dec)
    print vysledek
    decs = str(dec)
    secs = "{:02}".format(sec)
    if len(secs) == 1:
        secs = "0" + secs
    mins = str(min)
    return mins + ":" + secs + "." + decs

# testovani fce
cas = 1234
format(cas)

cas = 1821
#print format(cas)