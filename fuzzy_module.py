import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Input dan Output Variabel Fuzzy
usia = ctrl.Antecedent(np.arange(10, 81, 1), 'usia')
kebugaran = ctrl.Antecedent(np.arange(0, 3, 1), 'kebugaran')  # 0: Pemula, 1: Menengah, 2: Lanjutan
intensitas = ctrl.Consequent(np.arange(0, 11, 1), 'intensitas')

# 2. Membership Functions
usia['muda'] = fuzz.trimf(usia.universe, [10, 20, 35])
usia['dewasa'] = fuzz.trimf(usia.universe, [30, 45, 60])
usia['tua'] = fuzz.trimf(usia.universe, [55, 70, 80])

kebugaran['pemula'] = fuzz.trimf(kebugaran.universe, [0, 0, 1])
kebugaran['menengah'] = fuzz.trimf(kebugaran.universe, [0, 1, 2])
kebugaran['lanjutan'] = fuzz.trimf(kebugaran.universe, [1, 2, 2])

intensitas['ringan'] = fuzz.trimf(intensitas.universe, [0, 2, 4])
intensitas['sedang'] = fuzz.trimf(intensitas.universe, [3, 5, 7])
intensitas['berat'] = fuzz.trimf(intensitas.universe, [6, 8, 10])

# 3. Fuzzy Rules    
rule1 = ctrl.Rule(usia['muda'] & kebugaran['pemula'], intensitas['sedang'])
rule2 = ctrl.Rule(usia['muda'] & kebugaran['menengah'], intensitas['berat'])
rule3 = ctrl.Rule(usia['muda'] & kebugaran['lanjutan'], intensitas['berat'])

rule4 = ctrl.Rule(usia['dewasa'] & kebugaran['pemula'], intensitas['ringan'])
rule5 = ctrl.Rule(usia['dewasa'] & kebugaran['menengah'], intensitas['sedang'])
rule6 = ctrl.Rule(usia['dewasa'] & kebugaran['lanjutan'], intensitas['berat'])

rule7 = ctrl.Rule(usia['tua'] & kebugaran['pemula'], intensitas['ringan'])
rule8 = ctrl.Rule(usia['tua'] & kebugaran['menengah'], intensitas['ringan'])
rule9 = ctrl.Rule(usia['tua'] & kebugaran['lanjutan'], intensitas['sedang'])

# 4. Buat sistem fuzzy
intensitas_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9
])
intensitas_simulasi = ctrl.ControlSystemSimulation(intensitas_ctrl)

# 5. Fungsi wrapper
def fuzzy_rekomendasi_latihan(usia_pengguna, level_kebugaran):
    # mapping level kebugaran
    mapping_kebugaran = {'Pemula': 0, 'Menengah': 1, 'Lanjutan': 2}
    level = mapping_kebugaran.get(level_kebugaran, 0)

    intensitas_simulasi.input['usia'] = usia_pengguna
    intensitas_simulasi.input['kebugaran'] = level
    intensitas_simulasi.compute()

    skor = intensitas_simulasi.output['intensitas']

    if skor < 4:
        return "Latihan ringan seperti stretching, jalan cepat, yoga"
    elif skor < 7:
        return "Latihan sedang seperti jogging, bodyweight workout, circuit training"
    else:
        return "Latihan berat seperti HIIT, angkat beban intens, sprint interval"
