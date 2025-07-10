from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Formulário de Geometria – Vestibular UEM", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Geometria Plana
pdf.chapter_title("1. Geometria Plana – Áreas e Perímetros")
pdf.chapter_body("""
Quadrado: A = l²
Retângulo: A = b · h
Paralelogramo: A = b · h
Triângulo: A = (b · h)/2
Trapézio: A = [(B + b) · h]/2
Losango: A = (D · d)/2
Círculo: A = π · r²
Circunferência (comprimento): C = 2π · r

Polígonos Regulares:
- Perímetro: P = n · l
- Ângulo interno: α = [(n - 2) · 180°]/n
- Soma dos ângulos internos: S = (n - 2) · 180°
""")

# Geometria Espacial
pdf.chapter_title("2. Geometria Espacial – Volumes e Áreas")
pdf.chapter_body("""
Volumes:
Cubo: V = a³
Paralelepípedo: V = a · b · c
Prisma: V = A_b · h
Cilindro: V = π · r² · h
Cone: V = (1/3) · π · r² · h
Pirâmide: V = (1/3) · A_b · h
Esfera: V = (4/3) · π · r³

Áreas Totais:
Cubo: A = 6 · a²
Paralelepípedo: A = 2(ab + bc + ac)
Cilindro: A = 2π · r(h + r)
Cone: A = π · r (g + r)
Esfera: A = 4π · r²
""")

# Geometria Analítica
pdf.chapter_title("3. Geometria Analítica – Fórmulas Essenciais")
pdf.chapter_body("""
Distância entre dois pontos: d = √[(x₂ - x₁)² + (y₂ - y₁)²]
Ponto médio: M = ((x₁ + x₂)/2 , (y₁ + y₂)/2)

Equações da reta:
- Forma reduzida: y = mx + b
- Forma geral: Ax + By + C = 0
- Coeficiente angular (entre dois pontos): m = (y₂ - y₁)/(x₂ - x₁)
- Condições:
  * Retas paralelas: m₁ = m₂
  * Retas perpendiculares: m₁ · m₂ = -1

Equação da circunferência: (x - a)² + (y - b)² = r²
""")

pdf.output("Formulario-Geometria-UEM.pdf")
