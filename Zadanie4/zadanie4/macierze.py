macierz = []
with open('macierz.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        macierz.append(int_list)
print("Macierz początkowa:", macierz)


def PostacNormalnaSchodkowa(m):
    if not m:
        return
    wiodacy = 0
    IleRzedow = len(m)
    IleKolumn = len(m[0])
    for r in range(IleRzedow):
        if wiodacy >= IleKolumn:
            return
        i = r
        while m[i][wiodacy] == 0:
            i += 1
            if i == IleRzedow:
                i = r
                wiodacy += 1
                if IleKolumn == wiodacy:
                    return
        m[i], m[r] = m[r], m[i]
        lv = m[r][wiodacy]
        m[r] = [mrx / float(lv) for mrx in m[r]]
        for i in range(IleRzedow):
            if i != r:
                lv = m[i][wiodacy]
                m[i] = [iv - lv * rv for rv, iv in zip(m[r], m[i])]
        wiodacy += 1


PostacNormalnaSchodkowa(macierz)

counter1 = 0
i = 0
row_len = len(macierz[0])
while i < len(macierz):
    counter2 = 0
    for j in macierz[i]:
        if j != 0.0 or j != -0.0:
            counter2 += 1
    if counter2 == 1 and macierz[i][row_len-1] != 0.0:
        print("Układ jest sprzeczny.")
        break
    elif counter2 == 0:
        print("Układ ma nieskończenie wiele rozwiązań.")
        break
    else:
        counter1 += 1
    i += 1

if counter1 == len(macierz):
    print("Układ ma jedno rozwiązanie:", macierz)
