indices_F = []

# K16, K20, K36, K55 (Column 'أ', index 0)
indices_F.append((14, 0))  # K16
indices_F.append((18, 0))  # K20
indices_F.append((34, 0))  # K36
indices_F.append((53, 0))  # K55

# L8, L20, L33, L36, L39, L43, L48, L54 (Column 'ب', index 1)
indices_F.append((6, 1))   # L8
indices_F.append((18, 1))  # L20
indices_F.append((31, 1))  # L33
indices_F.append((34, 1))  # L36
indices_F.append((37, 1))  # L39
indices_F.append((41, 1))  # L43
indices_F.append((46, 1))  # L48
indices_F.append((52, 1))  # L54

# M10, M14 to M17, M30, M42, M47 to M48 (Column 'ج', index 2)
indices_F.append((8, 2))   # M10
for row in range(12, 16):  # M14 to M17
    indices_F.append((row, 2))
indices_F.append((28, 2))  # M30
indices_F.append((40, 2))  # M42
indices_F.append((45, 2))  # M47
indices_F.append((46, 2))  # M48

# N5, N7 to N9, N12, N15 to N16, N18, N22 to N23, N25 to N26, N28, N34 (Column 'ح', index 3)
indices_F.append((3, 3))   # N5
for row in range(5, 8):    # N7 to N9
    indices_F.append((row, 3))
indices_F.append((10, 3))  # N12
indices_F.append((13, 3))  # N15
indices_F.append((14, 3))  # N16
indices_F.append((16, 3))  # N18
indices_F.append((20, 3))  # N22
indices_F.append((21, 3))  # N23
indices_F.append((23, 3))  # N25
indices_F.append((24, 3))  # N26
indices_F.append((26, 3))  # N28
indices_F.append((32, 3))  # N34

# O7, O9, O16, O18, O22, O24, O30, O40, O43 to O44 (Column 'د', index 4)
indices_F.append((5, 4))   # O7
indices_F.append((7, 4))   # O9
indices_F.append((14, 4))  # O16
indices_F.append((16, 4))  # O18
indices_F.append((20, 4))  # O22
indices_F.append((22, 4))  # O24
indices_F.append((28, 4))  # O30
indices_F.append((38, 4))  # O40
indices_F.append((41, 4))  # O43
indices_F.append((42, 4))  # O44

# P4, P10, P12, P24, P34, P45, P49, P54 (Column 'ز', index 5)
indices_F.append((2, 5))   # P4
indices_F.append((8, 5))   # P10
indices_F.append((10, 5))  # P12
indices_F.append((22, 5))  # P24
indices_F.append((32, 5))  # P34
indices_F.append((43, 5))  # P45
indices_F.append((47, 5))  # P49
indices_F.append((52, 5))  # P54

# Q2, Q7 to Q9 (Column 'ط', index 6)
indices_F.append((0, 6))   # Q2
for row in range(5, 8):    # Q7 to Q9
    indices_F.append((row, 6))

# R21 to R22, R40 (Column 'ه', index 7)
indices_F.append((19, 7))  # R21
indices_F.append((20, 7))  # R22
indices_F.append((38, 7))  # R40

# S2 (Column 'و', index 8)
indices_F.append((0, 8))   # S2

# T44 (Column 'ي', index 9)
indices_F.append((42, 9))  # T44


indices_K_positive = []

# N29 (Column 'ح', index 3)
indices_K_positive.append((27, 3))

# O49 (Column 'د', index 4)
indices_K_positive.append((47, 4))

# S8 (Column 'و', index 8)
indices_K_positive.append((6, 8))

# S21 (Column 'و', index 8)
indices_K_positive.append((19, 8))

# P19 (Column 'ز', index 5)
indices_K_positive.append((17, 5))

# P24
indices_K_positive.append((22, 5))

# P31
indices_K_positive.append((29, 5))

# Q23 (Column 'ط', index 6)
indices_K_positive.append((21, 6))

# T52 (Column 'ي', index 9)
indices_K_positive.append((50, 9))


indices_K_negative = []

# K4 (Column 'أ', index 0)
indices_K_negative.append((2, 0))

# L56 (Column 'ب', index 1)
indices_K_negative.append((54, 1))

# M19 (Column 'ج', index 2)
indices_K_negative.append((17, 2))

# M28, M34
indices_K_negative.append((26, 2))
indices_K_negative.append((32, 2))

# O52, O54 to O55 (Column 'د', index 4)
indices_K_negative.append((50, 4))
indices_K_negative.append((52, 4))
indices_K_negative.append((53, 4))

# R44 to R45, R53 (Column 'ه', index 7)
indices_K_negative.append((42, 7))
indices_K_negative.append((43, 7))
indices_K_negative.append((51, 7))

# S9, S21, S34 to S35, S44, S47 (Column 'و', index 8)
indices_K_negative.append((7, 8))
indices_K_negative.append((19, 8))
indices_K_negative.append((32, 8))
indices_K_negative.append((33, 8))
indices_K_negative.append((42, 8))
indices_K_negative.append((45, 8))

# P30, P32 (Column 'ز', index 5)
indices_K_negative.append((28, 5))
indices_K_negative.append((30, 5))

# Q32, Q38 to Q39 (Column 'ط', index 6)
indices_K_negative.append((30, 6))
indices_K_negative.append((36, 6))
indices_K_negative.append((37, 6))


indices_Hs = []

# K2 to K3 (Column 'أ', index 0)
indices_Hs.append((0, 0))  # K2
indices_Hs.append((1, 0))  # K3

# K5 to K6 (Column 'أ', index 0)
indices_Hs.append((3, 0))  # K5
indices_Hs.append((4, 0))  # K6

# K11 (Column 'أ', index 0)
indices_Hs.append((9, 0))  # K11

# K13 to K17 (Column 'أ', index 0)
for row in range(11, 16):
    indices_Hs.append((row, 0))  # K13 to K17

# K32 to K33 (Column 'أ', index 0)
indices_Hs.append((30, 0))  # K32
indices_Hs.append((31, 0))  # K33

# K37 (Column 'أ', index 0)
indices_Hs.append((35, 0))  # K37

# K41, K43, K45 (Column 'أ', index 0)
indices_Hs.append((39, 0))  # K41
indices_Hs.append((41, 0))  # K43
indices_Hs.append((43, 0))  # K45

# K47 to K49 (Column 'أ', index 0)
for row in range(45, 48):
    indices_Hs.append((row, 0))  # K47 to K49

# K51, K56 (Column 'أ', index 0)
indices_Hs.append((49, 0))  # K51
indices_Hs.append((54, 0))  # K56

# L9 to L11 (Column 'ب', index 1)
for row in range(7, 10):
    indices_Hs.append((row, 1))  # L9 to L11

# L13, L16 to L19, L21 (Column 'ب', index 1)
indices_Hs.append((11, 1))  # L13
for row in range(14, 18):
    indices_Hs.append((row, 1))  # L16 to L19
indices_Hs.append((19, 1))  # L21

# L28 to L29 (Column 'ب', index 1)
indices_Hs.append((26, 1))  # L28
indices_Hs.append((27, 1))  # L29

# M18 (Column 'ج', index 2)
indices_Hs.append((16, 2))  # M18





indices_D_positive = []

# K2 to K3 (Column 'أ', index 0)
indices_D_positive.append((0, 0))  # K2
indices_D_positive.append((1, 0))  # K3

# K5 (Column 'أ', index 0)
indices_D_positive.append((3, 0))  # K5

# K7, K9, K16, K19, K24 to K25, K28, K41 (Column 'أ', index 0)
indices_D_positive.append((5, 0))  # K7
indices_D_positive.append((7, 0))  # K9
indices_D_positive.append((14, 0))  # K16
indices_D_positive.append((17, 0))  # K19
indices_D_positive.append((22, 0))  # K24
indices_D_positive.append((23, 0))  # K25
indices_D_positive.append((26, 0))  # K28
indices_D_positive.append((39, 0))  # K41

# L3, L13, L19, L29, L31 (Column 'ب', index 1)
indices_D_positive.append((1, 1))  # L3
indices_D_positive.append((11, 1))  # L13
indices_D_positive.append((17, 1))  # L19
indices_D_positive.append((27, 1))  # L29
indices_D_positive.append((29, 1))  # L31

# M18 (Column 'ج', index 2)
indices_D_positive.append((16, 2))  # M18

# O11, O19 (Column 'د', index 4)
indices_D_positive.append((9, 4))  # O11
indices_D_positive.append((17, 4))  # O19

# R27, R37, R43 (Column 'ه', index 7)
indices_D_positive.append((25, 7))  # R27
indices_D_positive.append((35, 7))  # R37
indices_D_positive.append((41, 7))  # R43

# S35, S37, S39, S40, S43, S45 to S46, S52 (Column 'و', index 8)
indices_D_positive.append((33, 8))  # S35
indices_D_positive.append((35, 8))  # S37
indices_D_positive.append((37, 8))  # S39
indices_D_positive.append((38, 8))  # S40
indices_D_positive.append((41, 8))  # S43
indices_D_positive.append((43, 8))  # S45
indices_D_positive.append((44, 8))  # S46
indices_D_positive.append((50, 8))  # S52

# P8, P13, P19, P24, P39 (Column 'ز', index 5)
indices_D_positive.append((6, 5))   # P8
indices_D_positive.append((11, 5))  # P13
indices_D_positive.append((17, 5))  # P19
indices_D_positive.append((22, 5))  # P24
indices_D_positive.append((37, 5))  # P39

# N44, N56 (Column 'ح', index 3)
indices_D_positive.append((42, 3))  # N44
indices_D_positive.append((54, 3))  # N56

# Q28, Q35, Q38, Q40 (Column 'ط', index 6)
indices_D_positive.append((26, 6))  # Q28
indices_D_positive.append((33, 6))  # Q35
indices_D_positive.append((36, 6))  # Q38
indices_D_positive.append((38, 6))  # Q40

# T51 to T52 (Column 'ي', index 9)
indices_D_positive.append((49, 9))  # T51
indices_D_positive.append((50, 9))  # T52


indices_D_negative = []

# K4 (Column 'أ', index 0)
indices_D_negative.append((2, 0))  # K4

# L4 to L5, L7, L9, L37 (Column 'ب', index 1)
indices_D_negative.append((2, 1))   # L4
indices_D_negative.append((3, 1))   # L5
indices_D_negative.append((5, 1))   # L7
indices_D_negative.append((7, 1))   # L9
indices_D_negative.append((35, 1))  # L37

# M32, M34, M49 (Column 'ج', index 2)
indices_D_negative.append((30, 2))  # M32
indices_D_negative.append((32, 2))  # M34
indices_D_negative.append((47, 2))  # M49

# O23, O50 (Column 'د', index 4)
indices_D_negative.append((21, 4))  # O23
indices_D_negative.append((48, 4))  # O50

# P26, P32 to P33, P38 (Column 'ز', index 5)
indices_D_negative.append((24, 5))  # P26
indices_D_negative.append((30, 5))  # P32
indices_D_negative.append((31, 5))  # P33
indices_D_negative.append((36, 5))  # P38

# Q5 (Column 'ط', index 6)
indices_D_negative.append((3, 6))   # Q5






indices_Hy_positive = []

# K2 to K3, K6, K11 to K13, K16 to K18, K32 to K33, K41, K43, K45 to K47, K56 (Column 'أ', index 0)
indices_Hy_positive.append((0, 0))  # K2
indices_Hy_positive.append((1, 0))  # K3
indices_Hy_positive.append((4, 0))  # K6
indices_Hy_positive.append((9, 0))  # K11
indices_Hy_positive.append((10, 0))  # K12
indices_Hy_positive.append((11, 0))  # K13
indices_Hy_positive.append((14, 0))  # K16
indices_Hy_positive.append((15, 0))  # K17
indices_Hy_positive.append((16, 0))  # K18
indices_Hy_positive.append((30, 0))  # K32
indices_Hy_positive.append((31, 0))  # K33
indices_Hy_positive.append((39, 0))  # K41
indices_Hy_positive.append((41, 0))  # K43
indices_Hy_positive.append((43, 0))  # K45
indices_Hy_positive.append((44, 0))  # K46
indices_Hy_positive.append((45, 0))  # K47
indices_Hy_positive.append((54, 0))  # K56

# L2, L10 to L13, L28 to L29, L49 (Column 'ب', index 1)
indices_Hy_positive.append((0, 1))   # L2
indices_Hy_positive.append((8, 1))   # L10
indices_Hy_positive.append((9, 1))  # L11
indices_Hy_positive.append((10, 1))  # L12
indices_Hy_positive.append((11, 1))  # L13
indices_Hy_positive.append((26, 1))  # L28
indices_Hy_positive.append((27, 1))  # L29
indices_Hy_positive.append((47, 1))  # L49

# M18, M44, M52 (Column 'ج', index 2)
indices_Hy_positive.append((16, 2))  # M18
indices_Hy_positive.append((42, 2))  # M44
indices_Hy_positive.append((50, 2))  # M52

# O39, O45, O49 (Column 'د', index 4)
indices_Hy_positive.append((37, 4))  # O39
indices_Hy_positive.append((43, 4))  # O45
indices_Hy_positive.append((47, 4))  # O49

# S8, S40, S50 (Column 'و', index 8)
indices_Hy_positive.append((6, 8))   # S8
indices_Hy_positive.append((38, 8))  # S40
indices_Hy_positive.append((48, 8))  # S50

# P13, P22 (Column 'ز', index 5)
indices_Hy_positive.append((11, 5))  # P13
indices_Hy_positive.append((20, 5))  # P22

# N55 (Column 'ح', index 3)
indices_Hy_positive.append((53, 3))  # N55

# Q28 (Column 'ط', index 6)
indices_Hy_positive.append((26, 6))  # Q28

# T52 (Column 'ي', index 9)
indices_Hy_positive.append((50, 9))  # T52

indices_Hy_negative = []

# K4 (Column 'أ', index 0)
indices_Hy_negative.append((2, 0))  # K4

# L41 (Column 'ب', index 1)
indices_Hy_negative.append((39, 1))  # L41

# M26, M34, M43 (Column 'ج', index 2)
indices_Hy_negative.append((24, 2))  # M26
indices_Hy_negative.append((32, 2))  # M34
indices_Hy_negative.append((41, 2))  # M43

# O53, O55 (Column 'د', index 4)
indices_Hy_negative.append((51, 4))  # O53
indices_Hy_negative.append((53, 4))  # O55

# R24, R44 to R45, R54 to R55 (Column 'ه', index 7)
indices_Hy_negative.append((22, 7))  # R24
indices_Hy_negative.append((42, 7))  # R44
indices_Hy_negative.append((43, 7))  # R45
indices_Hy_negative.append((52, 7))  # R54
indices_Hy_negative.append((53, 7))  # R55

# S6, S10, S26, S34 (Column 'و', index 8)
indices_Hy_negative.append((4, 8))   # S6
indices_Hy_negative.append((8, 8))   # S10
indices_Hy_negative.append((24, 8))  # S26
indices_Hy_negative.append((32, 8))  # S34

# P30, P41, P51 (Column 'ز', index 5)
indices_Hy_negative.append((28, 5))  # P30
indices_Hy_negative.append((39, 5))  # P41
indices_Hy_negative.append((49, 5))  # P51

# N11 (Column 'ح', index 3)
indices_Hy_negative.append((9, 3))  # N11






indices_Pd_positive = []

# K5 (Column 'أ', index 0)
indices_Pd_positive.append((5 - 2, 0))  # K5

# L43 (Column 'ب', index 1)
indices_Pd_positive.append((43 - 2, 1))  # L43

# L48:L50 (Column 'ب', index 1)
for row in range(48, 51):  # Rows 48 to 50 inclusive
    indices_Pd_positive.append((row - 2, 1))  # L48 to L50

# L52:L54 (Column 'ب', index 1)
for row in range(52, 55):  # Rows 52 to 54 inclusive
    indices_Pd_positive.append((row - 2, 1))  # L52 to L54

# L56 (Column 'ب', index 1)
indices_Pd_positive.append((56 - 2, 1))  # L56

# M7:M8 (Column 'ج', index 2)
for row in range(7, 9):  # Rows 7 to 8 inclusive
    indices_Pd_positive.append((row - 2, 2))  # M7 to M8

# M13 (Column 'ج', index 2)
indices_Pd_positive.append((13 - 2, 2))  # M13

# M36 (Column 'ج', index 2)
indices_Pd_positive.append((36 - 2, 2))  # M36

# M48 (Column 'ج', index 2)
indices_Pd_positive.append((48 - 2, 2))  # M48

# O31, O33, O39, O45 (Column 'د', index 4)
indices_Pd_positive.append((31 - 2, 4))  # O31
indices_Pd_positive.append((33 - 2, 4))  # O33
indices_Pd_positive.append((39 - 2, 4))  # O39
indices_Pd_positive.append((45 - 2, 4))  # O45

# R13, R18, R38, R47, R51 (Column 'ه', index 7)
indices_Pd_positive.append((13 - 2, 7))  # R13
indices_Pd_positive.append((18 - 2, 7))  # R18
indices_Pd_positive.append((38 - 2, 7))  # R38
indices_Pd_positive.append((47 - 2, 7))  # R47
indices_Pd_positive.append((51 - 2, 7))  # R51

# S8, S37, S40, S51 (Column 'و', index 8)
indices_Pd_positive.append((8 - 2, 8))   # S8
indices_Pd_positive.append((37 - 2, 8))  # S37
indices_Pd_positive.append((40 - 2, 8))  # S40
indices_Pd_positive.append((51 - 2, 8))  # S51

# P5, P13, P19, P31 (Column 'ز', index 5)
indices_Pd_positive.append((5 - 2, 5))   # P5
indices_Pd_positive.append((13 - 2, 5))  # P13
indices_Pd_positive.append((19 - 2, 5))  # P19
indices_Pd_positive.append((31 - 2, 5))  # P31

# P54:P56 (Column 'ز', index 5)
for row in range(54, 57):  # Rows 54 to 56 inclusive
    indices_Pd_positive.append((row - 2, 5))  # P54 to P56

# N4, N13, N27, N32 (Column 'ح', index 3)
indices_Pd_positive.append((4 - 2, 3))    # N4
indices_Pd_positive.append((13 - 2, 3))   # N13
indices_Pd_positive.append((27 - 2, 3))   # N27
indices_Pd_positive.append((32 - 2, 3))   # N32

# Q13:Q14 (Column 'ط', index 6)
for row in range(13, 15):  # Rows 13 to 14 inclusive
    indices_Pd_positive.append((row - 2, 6))  # Q13 to Q14

# Q28, Q31 (Column 'ط', index 6)
indices_Pd_positive.append((28 - 2, 6))  # Q28
indices_Pd_positive.append((31 - 2, 6))  # Q31

indices_Pd_negative = []

# O3 (Column 'د', index 4)
indices_Pd_negative.append((3 - 2, 4))  # O3

# O52 (Column 'د', index 4)
indices_Pd_negative.append((52 - 2, 4))  # O52

# R44:R45 (Column 'ه', index 7)
for row in range(44, 46):  # Rows 44 to 45 inclusive
    indices_Pd_negative.append((row - 2, 7))  # R44 to R45

# S6, S9 (Column 'و', index 8)
indices_Pd_negative.append((6 - 2, 8))  # S6
indices_Pd_negative.append((9 - 2, 8))  # S9

# P26 (Column 'ز', index 5)
indices_Pd_negative.append((26 - 2, 5))  # P26

# Q27 (Column 'ط', index 6)
indices_Pd_negative.append((27 - 2, 6))  # Q27






# Initialize the lists for positive and negative indices
indices_Mf_positive = []
indices_Mf_negative = []

# Mapping of columns to indices:
# K: 0, L: 1, M: 2, N: 3, O: 4, P: 5, Q: 6, R: 7, S: 8, T: 9

# Positive Indices:

# K10 (Column 'K', index 0)
indices_Mf_positive.append((10 - 2, 0))  # K10

# L26 (Column 'L', index 1)
indices_Mf_positive.append((26 - 2, 1))  # L26

# M4, M11, M13 (Column 'M', index 2)
indices_Mf_positive.append((4 - 2, 2))   # M4
indices_Mf_positive.append((11 - 2, 2))  # M11
indices_Mf_positive.append((13 - 2, 2))  # M13

# O17:O18 (Column 'O', index 4)
for row in range(17, 19):  # Rows 17 to 18 inclusive
    indices_Mf_positive.append((row - 2, 4))  # O17 to O18

# O40 (Column 'O', index 4)
indices_Mf_positive.append((40 - 2, 4))  # O40

# R4 (Column 'R', index 7)
indices_Mf_positive.append((4 - 2, 7))   # R4

# R34:R36 (Column 'R', index 7)
for row in range(34, 37):  # Rows 34 to 36 inclusive
    indices_Mf_positive.append((row - 2, 7))  # R34 to R36

# R50 (Column 'R', index 7)
indices_Mf_positive.append((50 - 2, 7))  # R50

# S16, S47, S53 (Column 'S', index 8)
indices_Mf_positive.append((16 - 2, 8))  # S16
indices_Mf_positive.append((47 - 2, 8))  # S47
indices_Mf_positive.append((53 - 2, 8))  # S53

# N3, N39 (Column 'N', index 3)
indices_Mf_positive.append((3 - 2, 3))   # N3
indices_Mf_positive.append((39 - 2, 3))  # N39

# Q41, Q45:Q46, Q51, Q54 (Column 'Q', index 6)
indices_Mf_positive.append((41 - 2, 6))  # Q41
for row in range(45, 47):  # Rows 45 to 46 inclusive
    indices_Mf_positive.append((row - 2, 6))  # Q45 to Q46
indices_Mf_positive.append((51 - 2, 6))  # Q51
indices_Mf_positive.append((54 - 2, 6))  # Q54

# T2, T6 (Column 'T', index 9)
indices_Mf_positive.append((2 - 2, 9))   # T2
indices_Mf_positive.append((6 - 2, 9))   # T6

# T12:T13 (Column 'T', index 9)
for row in range(12, 14):  # Rows 12 to 13 inclusive
    indices_Mf_positive.append((row - 2, 9))  # T12 to T13

# T19:T20 (Column 'T', index 9)
for row in range(19, 21):  # Rows 19 to 20 inclusive
    indices_Mf_positive.append((row - 2, 9))  # T19 to T20

# T24:T27 (Column 'T', index 9)
for row in range(24, 28):  # Rows 24 to 27 inclusive
    indices_Mf_positive.append((row - 2, 9))  # T24 to T27

# T32:T33 (Column 'T', index 9)
for row in range(32, 34):  # Rows 32 to 33 inclusive
    indices_Mf_positive.append((row - 2, 9))  # T32 to T33

# T35, T41, T55 (Column 'T', index 9)
indices_Mf_positive.append((35 - 2, 9))  # T35
indices_Mf_positive.append((41 - 2, 9))  # T41
indices_Mf_positive.append((55 - 2, 9))  # T55

# Negative Indices:

# K44 (Column 'K', index 0)
indices_Mf_negative.append((44 - 2, 0))  # K44

# M34, M37, M46 (Column 'M', index 2)
indices_Mf_negative.append((34 - 2, 2))  # M34
indices_Mf_negative.append((37 - 2, 2))  # M37
indices_Mf_negative.append((46 - 2, 2))  # M46

# O37, O48, O51 (Column 'O', index 4)
indices_Mf_negative.append((37 - 2, 4))  # O37
indices_Mf_negative.append((48 - 2, 4))  # O48
indices_Mf_negative.append((51 - 2, 4))  # O51

# R10, R17 (Column 'R', index 7)
indices_Mf_negative.append((10 - 2, 7))  # R10
indices_Mf_negative.append((17 - 2, 7))  # R17

# P31, P41 (Column 'P', index 5)
indices_Mf_negative.append((31 - 2, 5))  # P31
indices_Mf_negative.append((41 - 2, 5))  # P41

# Q5, Q50, Q52 (Column 'Q', index 6)
indices_Mf_negative.append((5 - 2, 6))   # Q5
indices_Mf_negative.append((50 - 2, 6))  # Q50
indices_Mf_negative.append((52 - 2, 6))  # Q52

# T8, T11, T30 (Column 'T', index 9)
indices_Mf_negative.append((8 - 2, 9))   # T8
indices_Mf_negative.append((11 - 2, 9))  # T11
indices_Mf_negative.append((30 - 2, 9))  # T30





# Initialize the lists for positive and negative indices
indices_Pa_positive = []
indices_Pa_negative = []

# Columns mapping:
# K: 0, L: 1, M: 2, N: 3, O: 4, P: 5, Q: 6, R: 7, S: 8, T: 9

# Positive Indices:

# K10, K23, K37 (Column 'K', index 0)
indices_Pa_positive.append((10 - 2, 0))  # K10
indices_Pa_positive.append((23 - 2, 0))  # K23
indices_Pa_positive.append((37 - 2, 0))  # K37

# L55 (Column 'L', index 1)
indices_Pa_positive.append((55 - 2, 1))  # L55

# O34, O36 (Column 'O', index 4)
indices_Pa_positive.append((34 - 2, 4))  # O34
indices_Pa_positive.append((36 - 2, 4))  # O36

# R13, R38 (Column 'R', index 7)
indices_Pa_positive.append((13 - 2, 7))  # R13
indices_Pa_positive.append((38 - 2, 7))  # R38

# S11, S36, S52 (Column 'S', index 8)
indices_Pa_positive.append((11 - 2, 8))  # S11
indices_Pa_positive.append((36 - 2, 8))  # S36
indices_Pa_positive.append((52 - 2, 8))  # S52

# P7, P10, P13, P17, P35 (Column 'P', index 5)
indices_Pa_positive.append((7 - 2, 5))   # P7
indices_Pa_positive.append((10 - 2, 5))  # P10
indices_Pa_positive.append((13 - 2, 5))  # P13
indices_Pa_positive.append((17 - 2, 5))  # P17
indices_Pa_positive.append((35 - 2, 5))  # P35

# P53:P56 (Column 'P', index 5)
for row in range(53, 57):  # Rows 53 to 56 inclusive
    indices_Pa_positive.append((row - 2, 5))  # P53 to P56

# N4:N5 (Column 'N', index 3)
for row in range(4, 6):  # Rows 4 to 5 inclusive
    indices_Pa_positive.append((row - 2, 3))  # N4 to N5

# N7:N10 (Column 'N', index 3)
for row in range(7, 11):  # Rows 7 to 10 inclusive
    indices_Pa_positive.append((row - 2, 3))  # N7 to N10

# N12, N15, N17 (Column 'N', index 3)
indices_Pa_positive.append((12 - 2, 3))  # N12
indices_Pa_positive.append((15 - 2, 3))  # N15
indices_Pa_positive.append((17 - 2, 3))  # N17

# N26:N27 (Column 'N', index 3)
for row in range(26, 28):  # Rows 26 to 27 inclusive
    indices_Pa_positive.append((row - 2, 3))  # N26 to N27

# N50 (Column 'N', index 3)
indices_Pa_positive.append((50 - 2, 3))  # N50

# Negative Indices:

# O47, O51 (Column 'O', index 4)
indices_Pa_negative.append((47 - 2, 4))  # O47
indices_Pa_negative.append((51 - 2, 4))  # O51

# O53:O56 (Column 'O', index 4)
for row in range(53, 57):  # Rows 53 to 56 inclusive
    indices_Pa_negative.append((row - 2, 4))  # O53 to O56

# P51 (Column 'P', index 5)
indices_Pa_negative.append((51 - 2, 5))  # P51

# T42 (Column 'T', index 9)
indices_Pa_negative.append((42 - 2, 9))  # T42






# Initialize the lists for positive and negative indices
indices_Pt_positive = []
indices_Pt_negative = []

# Positive Indices:

# K7 (Column 'K', index 0)
indices_Pt_positive.append((7 - 2, 0))  # K7

# K23:K24 (Column 'K', index 0)
for row in range(23, 25):  # K23 to K24
    indices_Pt_positive.append((row - 2, 0))

# K28, K41 (Column 'K', index 0)
indices_Pt_positive.append((28 - 2, 0))  # K28
indices_Pt_positive.append((41 - 2, 0))  # K41

# L3, L12, L28, L31 (Column 'L', index 1)
indices_Pt_positive.append((3 - 2, 1))   # L3
indices_Pt_positive.append((12 - 2, 1))  # L12
indices_Pt_positive.append((28 - 2, 1))  # L28
indices_Pt_positive.append((31 - 2, 1))  # L31

# M42 (Column 'M', index 2)
indices_Pt_positive.append((42 - 2, 2))  # M42

# R51 (Column 'R', index 7)
indices_Pt_positive.append((51 - 2, 7))  # R51

# S4:S5 (Column 'S', index 8)
for row in range(4, 6):  # S4 to S5
    indices_Pt_positive.append((row - 2, 8))

# S11, S32 (Column 'S', index 8)
indices_Pt_positive.append((11 - 2, 8))  # S11
indices_Pt_positive.append((32 - 2, 8))  # S32

# S36:S37 (Column 'S', index 8)
for row in range(36, 38):  # S36 to S37
    indices_Pt_positive.append((row - 2, 8))

# S40, S45, S47 (Column 'S', index 8)
indices_Pt_positive.append((40 - 2, 8))  # S40
indices_Pt_positive.append((45 - 2, 8))  # S45
indices_Pt_positive.append((47 - 2, 8))  # S47

# S50:S51 (Column 'S', index 8)
for row in range(50, 52):  # S50 to S51
    indices_Pt_positive.append((row - 2, 8))

# P21:P23 (Column 'P', index 5)
for row in range(21, 24):  # P21 to P23
    indices_Pt_positive.append((row - 2, 5))

# P36:P37 (Column 'P', index 5)
for row in range(36, 38):  # P36 to P37
    indices_Pt_positive.append((row - 2, 5))

# P42:P44, P46 (Column 'P', index 5)
for row in range(42, 45):  # P42 to P44
    indices_Pt_positive.append((row - 2, 5))
indices_Pt_positive.append((46 - 2, 5))  # P46

# N14, N29, N31, N33, N53, N56 (Column 'N', index 3)
indices_Pt_positive.append((14 - 2, 3))  # N14
indices_Pt_positive.append((29 - 2, 3))  # N29
indices_Pt_positive.append((31 - 2, 3))  # N31
indices_Pt_positive.append((33 - 2, 3))  # N33
indices_Pt_positive.append((53 - 2, 3))  # N53
indices_Pt_positive.append((56 - 2, 3))  # N56

# Q14, Q24, Q26, Q28, Q33, Q36, Q38, Q40 (Column 'Q', index 6)
indices_Pt_positive.append((14 - 2, 6))  # Q14
indices_Pt_positive.append((24 - 2, 6))  # Q24
indices_Pt_positive.append((26 - 2, 6))  # Q26
indices_Pt_positive.append((28 - 2, 6))  # Q28
indices_Pt_positive.append((33 - 2, 6))  # Q33
indices_Pt_positive.append((36 - 2, 6))  # Q36
indices_Pt_positive.append((38 - 2, 6))  # Q38
indices_Pt_positive.append((40 - 2, 6))  # Q40

# Negative Indices:

# L34 (Column 'L', index 1)
indices_Pt_negative.append((34 - 2, 1))  # L34

# T42 (Column 'T', index 9)
indices_Pt_negative.append((42 - 2, 9))  # T42




# Initialize the lists for positive and negative indices
indices_Sc_positive = []
indices_Sc_negative = []

# Positive Indices:

# K20:K23 (Column 'K', index 0)
for row in range(20, 24):  # K20 to K23
    indices_Sc_positive.append((row - 2, 0))

# K26:K28 (Column 'K', index 0)
for row in range(26, 29):  # K26 to K28
    indices_Sc_positive.append((row - 2, 0))

# K31, K37:K39 (Column 'K', index 0)
indices_Sc_positive.append((31 - 2, 0))  # K31
for row in range(37, 40):  # K37 to K39
    indices_Sc_positive.append((row - 2, 0))

# K42:K45, K49 (Column 'K', index 0)
for row in range(42, 46):  # K42 to K45
    indices_Sc_positive.append((row - 2, 0))
indices_Sc_positive.append((49 - 2, 0))  # K49

# L37, L51 (Column 'L', index 1)
indices_Sc_positive.append((37 - 2, 1))  # L37
indices_Sc_positive.append((51 - 2, 1))  # L51

# M6, M7, M11, M12 (Column 'M', index 2)
indices_Sc_positive.append((6 - 2, 2))   # M6
indices_Sc_positive.append((7 - 2, 2))   # M7
indices_Sc_positive.append((11 - 2, 2))  # M11
indices_Sc_positive.append((12 - 2, 2))  # M12

# M14:M17 (Column 'M', index 2)
for row in range(14, 18):  # M14 to M17
    indices_Sc_positive.append((row - 2, 2))

# M48, M52:M54 (Column 'M', index 2)
indices_Sc_positive.append((48 - 2, 2))  # M48
for row in range(52, 55):  # M52 to M54
    indices_Sc_positive.append((row - 2, 2))

# O33:O34 (Column 'O', index 4)
for row in range(33, 35):  # O33 to O34
    indices_Sc_positive.append((row - 2, 4))

# R18, R21, R23, R25 (Column 'R', index 7)
indices_Sc_positive.append((18 - 2, 7))  # R18
indices_Sc_positive.append((21 - 2, 7))  # R21
indices_Sc_positive.append((23 - 2, 7))  # R23
indices_Sc_positive.append((25 - 2, 7))  # R25

# R38:R39, R41, R43 (Column 'R', index 7)
for row in range(38, 40):  # R38 to R39
    indices_Sc_positive.append((row - 2, 7))
indices_Sc_positive.append((41 - 2, 7))  # R41
indices_Sc_positive.append((43 - 2, 7))  # R43

# S19, S36, S40, S43, S45, S50 (Column 'S', index 8)
indices_Sc_positive.append((19 - 2, 8))  # S19
indices_Sc_positive.append((36 - 2, 8))  # S36
indices_Sc_positive.append((40 - 2, 8))  # S40
indices_Sc_positive.append((43 - 2, 8))  # S43
indices_Sc_positive.append((45 - 2, 8))  # S45
indices_Sc_positive.append((50 - 2, 8))  # S50

# P8, P10:P12, P21:P22, P35, P48, P52, P54, P56 (Column 'P', index 5)
indices_Sc_positive.append((8 - 2, 5))   # P8
for row in range(10, 13):  # P10 to P12
    indices_Sc_positive.append((row - 2, 5))
for row in range(21, 23):  # P21 to P22
    indices_Sc_positive.append((row - 2, 5))
indices_Sc_positive.append((35 - 2, 5))  # P35
indices_Sc_positive.append((48 - 2, 5))  # P48
indices_Sc_positive.append((52 - 2, 5))  # P52
indices_Sc_positive.append((54 - 2, 5))  # P54
indices_Sc_positive.append((56 - 2, 5))  # P56

# N9, N12:N14, N17, N21, N28, N31, N33, N54, N56 (Column 'N', index 3)
indices_Sc_positive.append((9 - 2, 3))   # N9
for row in range(12, 15):  # N12 to N14
    indices_Sc_positive.append((row - 2, 3))
indices_Sc_positive.append((17 - 2, 3))  # N17
indices_Sc_positive.append((21 - 2, 3))  # N21
indices_Sc_positive.append((28 - 2, 3))  # N28
indices_Sc_positive.append((31 - 2, 3))  # N31
indices_Sc_positive.append((33 - 2, 3))  # N33
indices_Sc_positive.append((54 - 2, 3))  # N54
indices_Sc_positive.append((56 - 2, 3))  # N56

# Q3:Q4, Q24, Q28, Q36 (Column 'Q', index 6)
for row in range(3, 5):  # Q3 to Q4
    indices_Sc_positive.append((row - 2, 6))
indices_Sc_positive.append((24 - 2, 6))  # Q24
indices_Sc_positive.append((28 - 2, 6))  # Q28
indices_Sc_positive.append((36 - 2, 6))  # Q36

# Negative Indices:

# M19 (Column 'M', index 2)
indices_Sc_negative.append((19 - 2, 2))  # M19

# T42 (Column 'T', index 9)
indices_Sc_negative.append((42 - 2, 9))  # T42


# Initialize the lists for positive and negative indices
indices_Ma_positive = []
indices_Ma_negative = []

# Positive Indices:

# K20:K23, K38 (Column 'K', index 0)
for row in range(20, 24):  # K20 to K23
    indices_Ma_positive.append((row - 2, 0))
indices_Ma_positive.append((38 - 2, 0))  # K38

# L4, L38, L41, L51 (Column 'L', index 1)
indices_Ma_positive.append((4 - 2, 1))   # L4
indices_Ma_positive.append((38 - 2, 1))  # L38
indices_Ma_positive.append((41 - 2, 1))  # L41
indices_Ma_positive.append((51 - 2, 1))  # L51

# M4, M7, M25, M32 (Column 'M', index 2)
indices_Ma_positive.append((4 - 2, 2))   # M4
indices_Ma_positive.append((7 - 2, 2))   # M7
indices_Ma_positive.append((25 - 2, 2))  # M25
indices_Ma_positive.append((32 - 2, 2))  # M32

# O8, O27, O34:O36, O45, O50 (Column 'O', index 4)
indices_Ma_positive.append((8 - 2, 4))   # O8
indices_Ma_positive.append((27 - 2, 4))  # O27
for row in range(34, 37):  # O34 to O36
    indices_Ma_positive.append((row - 2, 4))
indices_Ma_positive.append((45 - 2, 4))  # O45
indices_Ma_positive.append((50 - 2, 4))  # O50

# R2, R8, R12, R16, R32, R49 (Column 'R', index 7)
indices_Ma_positive.append((2 - 2, 7))   # R2
indices_Ma_positive.append((8 - 2, 7))   # R8
indices_Ma_positive.append((12 - 2, 7))  # R12
indices_Ma_positive.append((16 - 2, 7))  # R16
indices_Ma_positive.append((32 - 2, 7))  # R32
indices_Ma_positive.append((49 - 2, 7))  # R49

# S15 (Column 'S', index 8)
indices_Ma_positive.append((15 - 2, 8))  # S15

# P20:P22, P38, P48, P51 (Column 'P', index 5)
for row in range(20, 23):  # P20 to P22
    indices_Ma_positive.append((row - 2, 5))
indices_Ma_positive.append((38 - 2, 5))  # P38
indices_Ma_positive.append((48 - 2, 5))  # P48
indices_Ma_positive.append((51 - 2, 5))  # P51

# N20, N27 (Column 'N', index 3)
indices_Ma_positive.append((20 - 2, 3))  # N20
indices_Ma_positive.append((27 - 2, 3))  # N27

# Q35 (Column 'Q', index 6)
indices_Ma_positive.append((35 - 2, 6))  # Q35

# T45, T55 (Column 'T', index 9)
indices_Ma_positive.append((45 - 2, 9))  # T45
indices_Ma_positive.append((55 - 2, 9))  # T55

# Negative Indices:

# M28 (Column 'M', index 2)
indices_Ma_negative.append((28 - 2, 2))  # M28

# R44:R45 (Column 'R', index 7)
for row in range(44, 46):  # R44 to R45
    indices_Ma_negative.append((row - 2, 7))

# S9 (Column 'S', index 8)
indices_Ma_negative.append((9 - 2, 8))   # S9

# P17, P27, P31 (Column 'P', index 5)
indices_Ma_negative.append((17 - 2, 5))  # P17
indices_Ma_negative.append((27 - 2, 5))  # P27
indices_Ma_negative.append((31 - 2, 5))  # P31

# N48 (Column 'N', index 3)
indices_Ma_negative.append((48 - 2, 3))  # N48



# Initialize the lists for positive and negative indices
indices_Si_positive = []
indices_Si_negative = []

# Positive Indices:

# K37:K39 (Column 'K', index 0)
for row in range(37, 40):  # K37 to K39
    indices_Si_positive.append((row - 2, 0))

# L7, L23 (Column 'L', index 1)
indices_Si_positive.append((7 - 2, 1))   # L7
indices_Si_positive.append((23 - 2, 1))  # L23

# M21, M26, M56 (Column 'M', index 2)
indices_Si_positive.append((21 - 2, 2))  # M21
indices_Si_positive.append((26 - 2, 2))  # M26
indices_Si_positive.append((56 - 2, 2))  # M56

# O51, O54, O55 (Column 'O', index 4)
indices_Si_positive.append((51 - 2, 4))  # O51
indices_Si_positive.append((54 - 2, 4))  # O54
indices_Si_positive.append((55 - 2, 4))  # O55

# R19, R24, R27:R31, R33:R37, R39 (Column 'R', index 7)
indices_Si_positive.append((19 - 2, 7))  # R19
indices_Si_positive.append((24 - 2, 7))  # R24
for row in range(27, 32):  # R27 to R31
    indices_Si_positive.append((row - 2, 7))
for row in range(33, 38):  # R33 to R37
    indices_Si_positive.append((row - 2, 7))
indices_Si_positive.append((39 - 2, 7))  # R39

# R44:R45, R47:R48, R50, R52, R56 (Column 'R', index 7)
for row in range(44, 46):  # R44 to R45
    indices_Si_positive.append((row - 2, 7))
for row in range(47, 49):  # R47 to R48
    indices_Si_positive.append((row - 2, 7))
indices_Si_positive.append((50 - 2, 7))  # R50
indices_Si_positive.append((52 - 2, 7))  # R52
indices_Si_positive.append((56 - 2, 7))  # R56

# S3:S7, S9:S10, S32, S35, S37, S42, S46 (Column 'S', index 8)
for row in range(3, 8):    # S3 to S7
    indices_Si_positive.append((row - 2, 8))
for row in range(9, 11):   # S9 to S10
    indices_Si_positive.append((row - 2, 8))
indices_Si_positive.append((32 - 2, 8))  # S32
indices_Si_positive.append((35 - 2, 8))  # S35
indices_Si_positive.append((37 - 2, 8))  # S37
indices_Si_positive.append((42 - 2, 8))  # S42
indices_Si_positive.append((46 - 2, 8))  # S46

# P19, P36 (Column 'P', index 5)
indices_Si_positive.append((19 - 2, 5))  # P19
indices_Si_positive.append((36 - 2, 5))  # P36

# N52, N53 (Column 'N', index 3)
indices_Si_positive.append((52 - 2, 3))  # N52
indices_Si_positive.append((53 - 2, 3))  # N53

# Q26:Q30, Q39, Q42 (Column 'Q', index 6)
for row in range(26, 31):  # Q26 to Q30
    indices_Si_positive.append((row - 2, 6))
indices_Si_positive.append((39 - 2, 6))  # Q39
indices_Si_positive.append((42 - 2, 6))  # Q42

# T34 (Column 'T', index 9)
indices_Si_positive.append((34 - 2, 9))  # T34

# Negative Indices:

# M49 (Column 'M', index 2)
indices_Si_negative.append((49 - 2, 2))  # M49

# O3, O35, O36, O38, O46 (Column 'O', index 4)
indices_Si_negative.append((3 - 2, 4))   # O3
indices_Si_negative.append((35 - 2, 4))  # O35
indices_Si_negative.append((36 - 2, 4))  # O36
indices_Si_negative.append((38 - 2, 4))  # O38
indices_Si_negative.append((46 - 2, 4))  # O46

# S31 (Column 'S', index 8)
indices_Si_negative.append((31 - 2, 8))  # S31

# P25, P43 (Column 'P', index 5)
indices_Si_negative.append((25 - 2, 5))  # P25
indices_Si_negative.append((43 - 2, 5))  # P43

# N13, N19 (Column 'N', index 3)
indices_Si_negative.append((13 - 2, 3))  # N13
indices_Si_negative.append((19 - 2, 3))  # N19

# Q22 (Column 'Q', index 6)
indices_Si_negative.append((22 - 2, 6))  # Q22

# T25, T33 (Column 'T', index 9)
indices_Si_negative.append((25 - 2, 9))  # T25
indices_Si_negative.append((33 - 2, 9))  # T33


indices_Mf_gender = []
indices_Mf_gender.append((49, 2))  # M51
indices_Mf_gender.append((50, 2))  # M52
indices_Mf_gender.append((52, 2))  # M54
indices_Mf_gender.append((1, 4))   # O3
indices_Mf_gender.append((4, 4))   # O6