import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from fpdf import FPDF


class ChecklistApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Diagnóstico de Celular")

        tk.Label(root, text="Modelo de celular:").grid(row=0, column=0, sticky="w")
        self.model_entry = tk.Entry(root)
        self.model_entry.grid(row=0, column=1, columnspan=3, sticky="we", pady=5)

        self.items = [
            "¿Enciende correctamente?",
            "¿Pantalla táctil funciona?",
            "¿Micrófono funciona?",
            "¿Altavoz funciona?",
            "¿Cámara frontal?",
            "¿Cámara trasera?",
            "¿WiFi conecta?",
            "¿Bluetooth funciona?",
            "¿Sensor de proximidad?",
            "¿Puerto de carga funciona?",
            "¿Lector de huellas?",
            "¿FaceID / Reconocimiento facial?",
            "¿Batería mantiene carga?",
        ]

        self.vars = []
        for i, item in enumerate(self.items, start=1):
            tk.Label(root, text=item).grid(row=i, column=0, sticky="w")
            var = tk.StringVar(value="No verificado")
            tk.Radiobutton(root, text="Funciona", variable=var, value="Funciona").grid(row=i, column=1)
            tk.Radiobutton(root, text="Falla", variable=var, value="Falla").grid(row=i, column=2)
            self.vars.append(var)

        tk.Button(root, text="Generar informe", command=self.generate_report).grid(
            row=len(self.items) + 1, column=0, columnspan=3, pady=10
        )

    def generate_report(self) -> None:
        model = self.model_entry.get().strip() or "Desconocido"
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        results = [f"- {item} {var.get()}" for item, var in zip(self.items, self.vars)]
        text_content = [
            "Informe de Diagnóstico",
            f"Modelo: {model}",
            f"Fecha: {now.strftime('%d/%m/%Y %H:%M')}",
            "",
            "Resultados:",
            *results,
            "",
        ]

        txt_file = f"informe_{date_str}.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write("\n".join(text_content))

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Informe de Diagnóstico", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Modelo: {model}", ln=True)
        pdf.cell(0, 10, f"Fecha: {now.strftime('%d/%m/%Y %H:%M')}", ln=True)
        pdf.ln(10)
        for line in results:
            pdf.cell(0, 10, line, ln=True)
        pdf_file = f"informe_{date_str}.pdf"
        pdf.output(pdf_file)

        messagebox.showinfo("Informe", f"Informe guardado como {txt_file} y {pdf_file}")


if __name__ == "__main__":
    root = tk.Tk()
    ChecklistApp(root)
    root.mainloop()
